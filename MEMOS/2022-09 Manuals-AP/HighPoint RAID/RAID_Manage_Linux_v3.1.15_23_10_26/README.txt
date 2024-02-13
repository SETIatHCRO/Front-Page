HighPoint Web RAID Management Software (WebGUI&CLI) for Linux
Copyright (C) 2023 HighPoint Technologies, Inc. All rights reserved.

Last updated on Oct 26, 2023

HighPoint Web RAID Management Software (WebGUI&CLI) is used to monitor and configure
your hard disks and RAID arrays attached to HighPoint RAID controllers.

This file is divided into the following major sections:

1. Files Listing
2. System Requirements
3. Installing the Software Package
4. Running the Management Software
5. Rivision History

1. Files Listing
------------------
        README.txt                                   This file
        RAID_Manage_Linux_v3.1.15_23_10_26.bin        Install file
        HPT_CLI_Guide.pdf                            CLI User Manual

2. System Requirements
------------------------

        The software package must be installed on system with supported HighPoint
        RAID controllers installed, and the device driver must be loaded to run
        the service.
   
        A web browser with XML support is required on the client side, e.g. Internet
        Explorer 6.0, Mozilla or FireFox.
        
        Only 64 bit systems are supported.

3. Installing the Software Package
------------------------------------

        To install the packge, you must log on as root.
        
        Start your terminal and input the command:
                # ./RAID_Manage_Linux_vx.x.x_x_x_x.bin

        The following files will be installed/configured:
   
                /usr/bin/hptsvr            - service program
                /usr/bin/hptraidconf       - command line program(CLI)
                /etc/rc.d/init.d/hptdaemon - service control script
                /usr/share/hpt/webguiroot  - data files

        You can use command "rpm -e hptsvr-https" or "dpkg -r hptsvr" to uninstall the software.
     

4. Running the Management Software
------------------------------------
        a. RUN WEBGUI
                To run the WebGUI, start your browser and enter the following URL address:
   
                           http://localhost:7402
       
                If you are accessing WebGUI on a remote system please change "localhost"
                to the server address.
        b. RUN hptraidconf(CLI)
                To run the CLI, start your terminal and input the command:
                           hptraidconf

                And you can enter a complete command with parameters at the shell prompt and receive
                one output result on the screen at a time.
                           hptraidconf -u {username} -p {password} {command}
                Example:
                           #hptraidconf -u RAID -p hpt query controllers 

        If you can't connect to local system or CLI, please check if hptsvr is running on
        the system. If not, start it manually by running "hptsvr".
   
        If you can't connect to a remote system, check if hptsvr is running on that
        system and you can access the remote system via TCP/IP connection. If you
        have firewall configured, make sure TCP port 7402 is not blocked.


5. Revision History
---------------------
    v3.1.15 10/26/2023
         Optimze the display on the Physical page.
         Optimze Health Inspector Scheduler.
         Support temperature monitor task.
         Remove the RAID feature for a non-RAID board.
         Fix a bug where RAID could still be created with the wrong number of disks in CLI.
         Fix a bug that send non-standard NVMe commands frequently.

    v3.1.14 04/21/2023
         Support SED function.

    v3.1.13 12/05/2022
         Fix a bug that displayed the enclosure model name error.
         Fix a bug that hptsvr cannot startup on Rocky.

    v3.1.12 11/01/2022
         Add installation log.
         Modify CLI delete operation feedback exception.
         Modify CLI set operation feedback exception.
         Support for parsing of new versions of the BLF file format.
         Fix a problem with some products displaying the LOGICAL button.

    v3.1.11 09/28/2022
         Add crash information to diag.
         Support setting password to cli.
         Support remote control to cli.
         Disable clearing event.

    v3.1.10 09/27/2022
         Support different blf file versions.

    v3.1.9  09/16/2022
         Support cards with different RAID configurations.

    v3.1.8  08/05/2022
         Fix a bug that diag function cannot work normally.
         Display enclosure information synchronously with WEBGUI to cli.
         Optimize login steps to cli.

    v3.1.7  07/15/2022
	 Add MCU version display.
	 Only support firmware update using blf file format.
	 Add ver commmad to cli.
         Fix a bug that disk can be initialized when it is being in use to cli.

    v3.1.6  06/22/2022
          Fix a bug that ATA smart information displays error.
	  Improve CLI commmand input checking.
	  
    v3.1.5  06/10/2022
          Support UnionTech OS.
          Add program running log.
          Fix a bug that cannot stop init array to cli.
	  Fix a bug that cannot expand/migrated array to cli.

    v3.1.4  04/27/2022
          Support Kylin OS.
	  Fix some CLI commands display error.

    v3.1.3  04/15/2022
          Add Array WWN information.
          Add update MCU to WEBGUI.

    v3.1.2  04/01/2022
          Add BIOS and temperture information for controller and enclosure.
	  Add update BIOS/Firmware to cli.

    v3.1.1  03/24/2022
          Add extra information for controller and enclosure.

    v3.1.0  03/09/2022
          Add identify LED to cli.

    v3.0.8  01/12/2022
          Support SSD6200.

    v3.0.7  11/12/2021
          Support multi-board and multi-drive detection.
          Add error printing and suggestions to cli.
    
    v3.0.6  11/09/2021
          Fix a bug that WebGUI cannot be displayed normally after restarting
          system when the driver delays loading disks.
          Change RAID 1/0 to RAID 10.
          Support PCIe 4.0 and PCIe 5.0. 

    v3.0.4  05/13/2021
          Update openssl to 3.0 to fix the bug of email sending failure.
          32 bit systems are no longer supported.
          Fix a bug that failed to override the old version installation on Fedora 33.
    
    v3.0.3  05/10/2021
          Fix the Segmentation fault of hptraidconf.
    
    v3.0.2  04/07/2021
          Add the 'diag' command to hptraidconf to collect diagnostic information.
    
    v3.0.1  03/29/2021
          Fix the display of Recover view.
          Fix the version time of the saved Index view.
          
    v3.0.0  02/05/2021
          Support Diagnostic.
          Fix a bug that when Fedora 33 has the command 'dpkg', WebGUI cannot be installed successfully.
          Make diagnostic page browser compatible for IE, Chrome, Fire Fox and Opera.
          Diagnostic page support rr3740a/hptnvme/rr640xl/rr272x/ssd711x detection.
          
    v2.3.15  04/17/2020
          Fix a bug that when the libreadline version is higher than 7, WebGUI cannot be installed successfully.

    v2.3.14.1  07/26/2017
          Support NVMe.
          
    v2.3.11  08/08/2016
          Fix an upload recover list error.

    v2.3.10  07/24/2016
          Support RR840A.

    v2.3.8  05/25/2016
          Support RR3740A.

    v2.3.6  04/27/2016
	  Fix bugs about cli task.
	  Fix a installation bug.
          Hptcfg is out of use.

    v2.3.5  04/12/2015
          Support updating LCD firmware and screen message.
          Support auto login.

    v2.3.4  09/11/2015
          Support LCD firmware update.

    v2.3.3  01/09/2015
          Restrict password length to 8 characters.
          Support NewTek.

    v2.3.2.1  11/02/2015
          Auto remove old version WebGUI during installation.

    v2.3.2  19/12/2014
          Support 4Kn drive.

    v2.3.1  20/10/2014
          The tape's OS name in WebGUI logical page will be displayed as the tape's model number instead of "HPT DISK x_x".

    v2.3.0  28/09/2014
          Support SAS tape and media changer device.
          Support DV mode array.

    v2.2.6  13/01/2014
          Fix Issue Of EventLevel Show.
          Change the method of install software.

    v2.2.4  24/12/2013
          Fix sector size cannot be properly restored in Recover and so on.

    v2.2.2  09/12/2013
          Add CLI(hptraidconf) Program.
          
    v2.2.1  15/11/2013
          Add deb package.
          
    v2.2.0-13.1031  31/10/2013
          Add Support Rocket/DataCenter Series.
          Add Support SRC.
          
    v2.1.5-13.0409  09/04/2013
          Support EJ340.
          Support RS5345 PM.
          Support RS5315 PM.
          
    v2.1.4-12.0921  21/09/2012
          Add Support RR642L.
              
    v2.1.3-12.0829  29/08/2012
          Add Support RR4522.
          
    v2.1.2.12.0718 18/07/2012
          Add online help.
          Support for SMTP/SSL.
          Support for Recover.

    v2.1.11.0822 22/08/2011
         Support for EJ6172 Firmware Update.
         
    v2.0.11.0713 13/07/2011
         Support for OCE/ORLM.

    v2.0.0 Beta 29/4/2011
         Totally new GUI layout.
         Support for EJ220+rr2720.
