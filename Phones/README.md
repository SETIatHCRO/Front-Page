# Switch config:

Use "Voice VLAN" to put VLAN 22 on all access ports. This is advertised over LLDP. Add VLAN 22 as a tagged VLAN.
Set LLDP TLV interval to 5 seconds. Phones will pick up VLAN 22. Setting the LLDP TLV interval is essential,
otherwise phones don't wait long enough (default on switches is 30 seconds) to reliably get the LLDP message.

# Router config:

VLAN 22 is 10.1.22.0/24. DHCP must be enabled on this VLAN for phones to get an initial IPv4 address and their
provisioning data. Once phones are provisioned, they use a hardcoded static IPv4 address and send traffic
on VLAN 22.

Option 66 must be specified with the IPv4 address of the provisioning server, pbx1.hcro.org.
This is currently 10.1.22.10.

This is how the phones know how to contact the provisioning server.

# Vega 60G Setup

This is our analog gateway. It connects to the analog phone lines, and communicates over SIP to our FreePBX system.

Log in to webinterface on port 80 over given via DHCP. Default username/pw is "admin/admin"

Apply firmware upgrade.

https://sangomakb.atlassian.net/wiki/spaces/VG/pages/33456910/Registering+Vega+with+FreePBX+PJSIP+on+port+5060
Username: "vgw1"
Password is standard PBX line password, but we aren't using registration between VGW and PBX because there's
an unresolved issue preventing CallerID from being transmitted when using registration.

On Step 4 - FXO, port 1, "DID to Forward to SIP" is 5303352366 (or whatever Frontier line is plugged in).

Under "Expert Config -> Dial Plan -> Profile 23" (or whatever is the "To_FXO" dial plan):
Delete FXO_02 through FXO_04, leaving just FXO_01.
Delete FXS profile.

Under Expert Config -> SIP -> SIP Profile 1, change "From Header 'userinfo'" to "Calling Party". This allows
CID passthrough but prevents us from using registration/authentication. See:
https://community.freepbx.org/t/incoming-caller-id-vega-50-freepbx-how-can-i-get-this-working-pls/35898/5

This seems like an acceptable compromise for our environment.

Reboot the Vega gateway.

# FreePBX Setup

Connect via console (monitor, keyboard).
Download ISO and install FreePBX 16 with Asterisk 18 from here:
https://www.freepbx.org/downloads/

After install, log in via console and run updates:

```
yum update
fwconsole ma updateall
```

Connect to webinterface on port 80 over address given via DHCP.
Set admin username ("admin") and password.
Set security updates to "Email Only"

Log in. Activate. Activation is required for "commercial" modules, including free ones like System Administration.
Activation email:
apollak@seti.org

If you're reinstalling, you can check the FreePBX portal to get the installation ID, which you should re-use.

Skip all ads.

Set timezone.

Abort firewall setup. This system lives in a secured VLAN, and IMO the Sangoma firewall is buggy. Fail2Ban is still
enabled and running for all services.

Set the hostname and time zone using the sysadmin module.

Use System Admin module to set static IP:
10.1.22.10
Added to DNS as:
pbx1.hcro.org

## Enable TFTP on FreePBX

TFTP is used for provisioning the phones.

On the FreePBX server, edit `/etc/xinetd.d/tftp`.
Change `disable = yes` to `disable = no`.

Reboot.

Data added to `/tftpboot` will get served over TFTP. We have a whole series of scripts to handle putting the
right data there.

### SIP trunk registration

Settings -> Asterisk SIP Settings
Under "Codecs", unselect others and rearrange so that only g722 is selected and it's at the top.
Connectivity -> Trunks
Create new PJSIP named "sip_provider".
Username and Auth Username set to the same voip.ms value. Secret set to SIP provider's given value.
Server is our SIP provider's given value.
Context: "from-pstn-toheader" so Asterisk can get the DID number from the header.
Transport is UDP.
Save and "Apply Config" (red button in upper right).

Go to Reports -> Asterisk Info.
Scroll down to Registries -> PJSIP and make sure the trunk is "Registered".

### Outbound SIP configuration

Connectivity -> Outbound Routes
Create new route:
Route Name: "to_sip_provider"
Route CID: <observatory main number>
Override Extension: Yes
Trunk Sequence for Matched Routes: "sip_provider".
Dial Patterns. Do not include any prefix -- no prefix needed to access an outside line.
NXXNXXXXXX
1NXXNXXXXXX
4443
911

### Inbound SIP configuration

Connectivity -> Inbound Routes
Add new:
Description: from_sip_provider
Define the DID. This is passed in the SIP header and matched here,
and it's how FreePBX knows to use this particular inbound route.
Set destination to desired Ring Group.

### POTS trunk configuration

Connectivity -> Trunks
Create new pjsip trunk. Name: "vgw1". Set Outbound CallerID, Force Trunk CID.
Under pjsip settings, choose "Both" for authentication and "Receive" for Registration. Enter PBX for Secret.
Codecs should be "alaw" and "ulaw" only, as top 2 entries in list.

### Outbound POTS configuration

Connectivity -> Outbound Routes
Create new PJSIP: "to_vgw_pots1"
Set outbound CID (analog, so doesn't matter, but helps identify).
Set up dial patterns, just like above, but prefixed with "8". Use "8" to dial out over the analog line.

### Inbound POTS configuration

Connectivity -> Inbound Routes
Add new. Define the DID. This is passed from the Vega gateway. Pick a Ring Group.
Set prefix to "A:" to identify that the call came in over the analog line.

# Routine FreePBX Operations

*To provision phones to use newly-created extensions, see the "Phone Provisioning" section below.*

## Adding an Extension

Applications -> Extensions
Add new PJSIP:
Enter extension, display name (for internal Caller ID), common secret.
Leave Outbound CID and Emergency CID blank.
Set "Link to a Default User" to "None".
Under Advanced, set "Send Connected Line" to No.

## Adding a Ring Group

Applications -> Ring Groups
Add Ring Group (straightforward). Use "Terminate Call" for no-answer destination.

## Troubleshooting

Registration issue on phones? Maybe you set up the phone before adding the extension to FreePBX.

Check server. It will ban IPs that fail registration too many times in rapid succession.
iptables -L fail2ban-SIP

And delete entries with:
iptables -D fail2ban-SIP #

# Phone Provisioning / Adding Groups to On-Phone Directory

Prerequisite:
Create a file in `provisioning` called "secrets.yml" with content:

```
---

secrets:
  local_admin_password: "1234"
  local_user_password: "5678"
  sip_auth_password: "abcd"
```

This is so we don't check in sensitive secrets to git. This file is in .gitignore.

Update the `phone_config.yaml` file with the line or group information.

Run `generate_tftp_configs.py` to create all the XML files needed for provisioning. These are
stored in `tftp-out` (excluded from git repo).

Run `update_tftp_server.sh` to copy them to the production TFTP server.

At this point, the phone is ready to provision. Just make sure it lands on VLAN 22 via LLDP or directly configuring
an access port, and everything should be automatic from there.

Every phone will check for new provisioning data (phonebook, etc) once per day, overnight.

To speed this up, you can run `reboot_phone.py` to restart a specific phone by IP or line extension,
i.e. `reboot_phone.py 114`.

Or, you can reboot all phones campus-wide using `reboot_phone.py all`.

## Troubleshooting / factory resetting a phone

If a phone provision fails for some reason, and it's unrecoverable, just factory reset the phone using the
buttons on the phone itself. After a factory reset, it will reprovision. Most failures should be recoverable
if you fix the configuration file and reboot the phone. As long as it can reach the TFTP server, it should reprovision
with the corrected settings.