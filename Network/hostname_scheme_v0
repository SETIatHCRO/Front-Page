# Hostname Scheme

This is a draft of the scheme I would like to implement for the hostnames at the ATA. This is a first draft so please speak up if you have any ideas or problems. Ideally, we would edit this until everyone agrees and then I (Daniel Richards) will implement it across the network(s).

I'm not married to any of the ideas in this document. If we collaborated on a scheme, it would be much more likely to stand the test of time.

There are a few things I want to address:
* Different naming schemes
* Unclear names (e.g. nsg-work1)
* Unwieldy names (e.g. dsa-ata-5-ipmi)

At breakthrough listen, then have a short and sweet naming scheme: 
| Name | Purpose | 
|---|---|
| blh |  headnode |
| bls00 |  The first storage node |
| blc02 |  The third compute engine  | 

I think we should follow a similar scheme with `si` (SETI Institute) instead of `bl` (Breakthrough Listen) and possibly `frb` (Jonathan's FRB machines)
| Name | Purpose | 
|---|---|
| sihead |  headnode (head instead of h is less confusing I think?) |
| sis0 |  The first storage node (single digits for now) |
| sic01 |  The second compute engine (also stands for churn)  | 

## Domains and Subdomains

All the SETI computers, including the DSA machines, should be in the ** .seti.hcro.org ** subnet.

## DSA (very open ended)

I like the idea of using FRB instead of DSA just because more people know what FRB stands for but this is really Jonathan's baby.

Debating not using hyphens. `frb-c2` vs. `frbc2` 

## Switches

Switch name = `sw` + `speed in Gigabits/s` + `subnet ID` So for the switch currently called `dsa-ata-40g-sw` it would be `sw40-frb`

> Maybe we should do something rack based? There are a few switches in the SPR just for daisy chaining between racks.

## IPMI

ipmi hostname = hostname + ‘x’ i.e. sihead’s ipmi port should be named `siheadx`
Not only is this easier to remember, it also helps with scripting. 

> Side note: I'll be adding the following ipmitool alias to the machines: `alias ipmitool='ipmitool -I lanplus -U ADMIN -P ADMIN -H'`

## Snaps

I think `si-snapNN` and `frb-snapNN` makes sense but I'm not crazy about hyphens.

## Mapping Old to New Scheme

Current names (from arp) and purposed names.
| New Hostname | Old Hostname | Example | 
|--|--|--|
| sihead | nsg-head | |
| sic01 | nsg-work1 | |
| sis1 | store1 | |
| frb-cN | dsa-ata-N | frb-c2 |
| frb-cNx | dsa-ata-N-ipmi | frb-c3x |
| sw40-frb | dsa-ata-40g-sw | sw40-frb |

## Authors

* **Daniel Richards** [github.com/dan-rds](mailto:github.com/dan-rds)

