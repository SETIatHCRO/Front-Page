HighPoint NVMe Controller Linux Software Package Installation Guide
Copyright (C) 2024 HighPoint Technologies, Inc. All rights reserved.

Last updated on Dec 10, 2024

1. Overview
2. File List
3. Software Version
4. Installation
5. Management Software Usage
6. Driver Uninstallation
7. Management Uninstalltion
8. Driver Revision History
9. Management Revision History
10. Technical Support And Service

#############################################################################
1. Overview
#############################################################################

  This package contains Linux driver code and management software for HighPoint
  NVMe RAID controller.
  You can use it to build the driver module for custom Linux kernels.

  NO WARRANTY

  THE DRIVER SOURCE CODE HIGHPOINT PROVIDED IS FREE OF CHARGE, AND THERE IS
  NO WARRANTY FOR THE PROGRAM. THERE ARE NO RESTRICTIONS ON THE USE OF THIS
  FREE SOURCE CODE. HIGHPOINT DOES NOT PROVIDE ANY TECHNICAL SUPPORT IF THE
  CODE HAS BEEN CHANGED FROM ORIGINAL SOURCE CODE.

  LIMITATION OF LIABILITY

  IN NO EVENT WILL HIGHPOINT BE LIABLE FOR DIRECT, INDIRECT, SPECIAL,
  INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF OR
  INABILITY TO USE THIS PRODUCT OR DOCUMENTATION, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGES. IN PARTICULAR, HIGHPOINT SHALL NOT HAVE
  LIABILITY FOR ANY HARDWARE, SOFTWARE, OR DATA STORED USED WITH THE
  PRODUCT, INCLUDING THE COSTS OF REPAIRING, REPLACING, OR RECOVERING
  SUCH HARDWARE, OR DATA.

#############################################################################
2. File List
#############################################################################

  |- README.txt                         : this file
  `- setup.bin                          : software for NVMe RAID controller

#############################################################################
3. Software Version
############################################################################# 

    Driver version:          v1.8.12.0
    RAID Management version: v3.2.3

#############################################################################
4. Installation
#############################################################################

  1)  Extract the software package to a temporary directory.

  2)  Change to the temporary directory.

  3)  Run the .bin file to install the driver package.

    # sh setup.bin

  NOTES:

    The installer requires super user's permission to run. So if you are not
  logged in as root, please supply the password of root to start the
  installation.

    The installer will check and install build tools if some of them is
  missing. A network connection is required to install the build tools. The
  following tools are checked by the installer:
  
    gcc
    make
    perl

    They are installed automatically when you select "Software Development
  Workstation" group in the installation of RHEL/CentOS 6.

    When packages are installed from network, it may take too long to complete
  the installation as it depends on the network speed. The packages could be
  installed first to omit the network issue by following command:

    # yum install gcc make perl

    If the installer failed to find or install the required build tools, the
  installation will be terminated without any change to the system.

    The installer will install folders and files to /usr/share/hptdrv/hptnvme.

    At the end of the installation, the installer will build driver module
  hptnvme for all kernels in the system.

    And the auto build script will be invoked to build driver module for
  kernels added automatically when system reboot or shutdown.

#############################################################################
5. Management Software Usage
#############################################################################

  a. RUN WEBGUI
    To run the WebGUI, start your browser and enter the following URL address:

            http://localhost:7402
       
    If you are accessing WebGUI on a remote system please change "localhost"
    to the server address.

  b. RUN hptraidconf(CLI)
    To run the CLI, start your terminal and input the command:
            hptraidconf

    And you can enter a complete command with parameters at the shell prompt
	and receive one output result on the screen at a time.
            hptraidconf -u {username} -p {password} {command}
       Example:
            #hptraidconf -u RAID -p hpt query controllers 

    If you can't connect to local system or CLI, please check if hptsvr is
	running on the system. If not, start it manually by running "hptsvr".
   
    If you can't connect to a remote system, check if hptsvr is running on that
    system and you can access the remote system via TCP/IP connection. If you
    have firewall configured, make sure TCP port 7402 is not blocked.

#############################################################################
6. Driver Uninstallation
#############################################################################

    Run hptuninhptnvme as root to uninstall driver for NVMe RAID controller.

    These command will delete all files installed to the system previously,
    except the package(s) installed to support driver compilation.

#############################################################################
7. Management Uninstallation
#############################################################################

    Run hptuninhptsvr as root to uninstall management for NVMe RAID controller.
    
#############################################################################
8. Driver Revision history
#############################################################################
    v1.8.12.0 12/10/2024
      * Support kernel 6.11.

    v1.8.1 06/21/2024
      * Support R7608A/R7628A/7528D.
      * Support kernel 6.9.0.
      * Support Debian 12.5.

    v1.8.0 05/22/2024
      * Support R7608A/R7628A/7528D.
   
    v1.6.7 08/04/2023
      * Perform controller reset when command timeout.
      * Speedup RAID1's foreground initialization.

    v1.6.6 07/27/2023
      * Resolve the compilation failure of an earlier version.

    v1.6.5 07/18/2023
      * Add proxmox and redhat user login reminder.
      * Fix a bug that the system may crash if the NVMe request size is greater
     	than 2M.
      * Fix a bug that WebGUI may display two enclosures for one adapter when
	    using NVMe system disks.
      * Improve AER shielding.

    v1.6.4 06/25/2023
      * Add a network connection prompt.
      * Support PLX temperature monitoring.
      * Support SSD7749 SED.

    v1.6.3 06/09/2023
      * Fix a bug that AER mask adjustment is not completed.
      * Support Rocky Linux 9.2.
      * Improve sequencial performance issue when AMD IOMMU enabled.

    v1.6.2 05/29/2023
      * Fix potential memory leaks under IOMMU-enabled platform.

    v1.6.1 05/16/2023
      * Dump BlockSID information.
 
    v1.6.0.1 05/10/2023
      * AER error report workaround.

    v1.6.0 04/20/2023
      * OPAL encryption function.
      * Support controller hotplug.

    v1.5.1 02/21/2023
      * Fix a bug that driver failed to load under IOMMU-enabled platform.

    v1.5.0 02/16/2023
      *Support getting a binary driver from server when driver compilation
	   fails.

    v1.4.8 12/04/2022
      * Support SSD7580B.

    v1.4.7 11/22/2022
      * Support kernel 6.0.0 and redhat 9.
      * Add new install message.

    v1.4.6 10/20/2022
      * Support kernel 5.19.0.
      * Provide instructions for compiling and loading driver in README.
      * Support iommu.
      * Support PVE 7.x installation.
      * Support Ubuntu 22.04.1 LTS server installation.
      * Support slackware 15.0.
      * Fix support for redhat 8.6.

    v1.4.5 07/22/2022
      * Add serial under hptblock when disk is legacy.
    
    v1.4.4 06/13/2022
      * Support kernel 5.18.0.
      * Support CentOS 9.

    v1.4.3 05/30/2022
      * Add US Linux background Server address.

    v1.4.2 05/12/2022
      * Support kernel 5.17.0.
      * Fixup IO timeout when loading driver in some circumstance.
      * Fix a bug that unsupported commands return incorrect status from kernel
        5.14.0.
      * Fix a bug that the driver cannot return to last good kernel if the
	    driver does not work in the new kernel.

    v1.4.1 03/04/2022
      * Update Linux background Server address.

    v1.4.0 03/01/2022
      * Support kernel 5.16.0.

    v1.3.5 12/22/2021
      * Support kernel 5.15.0.
	 
    v1.3.3 11/25/2021
      * Support IOMMU enabled DMA access.
      * Fixup compilation issue on RHEL 8u5.

    v1.3.2 10/27/2021
      * Support NVMe controller hotplug.
      * Support NVMe controller suspend/hibernate/resume.
      * Fixup compilation issue on linux kernel 5.14.0.

    v1.3.1 09/07/2021
      * Fixup wrong destination block address if the specified LBA of IO to
        RAID0 exceeds 4TB.

    v1.3.0 07/19/2021
      * Improve 4K IO performance.

    v1.2.24 01/05/2021
      * Support SSD7580.

    v1.2.23 01/04/2021
      * Enable 64K stripe size.

    v1.2.22 11/12/2020
      * Fixup IO performance issue.
      * Fixup compilation issue on linux kernel 5.8.0.

    v1.2.20 09/28/2020
      * Support SSD7540.
      * Support SSD7120.
      * Support SSD6540.

    v1.2.18 08/03/2020
      * Fix a bug that RAID not "hide" when deleted and rescan later.

    v1.2.17 07/16/2020
      * Support SSD7105.
      * Support SSD7180.
      * Support SSD7184.

    v1.2.16 07/14/2020
      * Support Ubuntu Live Server 20.04 installation.
      * Fix a bug that some NVMe device(s) failed to be probed when it is in D3
        power-saving mode.
      * Install libelf devel library on CentOS/RHEL system to pass driver
	    installation.

    v1.2.15 05/06/2020
      * Support SSD7505.

    v1.2.14 04/22/2020
      * Fixup system frozen when long time IO over RAID1.

    v1.2.13 03/16/2020
      * Fixup system crash IO under CentOS/RHEL 7.x when XFS created on target
	    Array(s).
      * Support SSD7202.

    v1.2.10 12/03/2019
      * Mddify makefile to support kernel 5.4.1.

    v1.2.9.1 11/28/2019
      * Disable iommu on Intel and AMD platform.
      * Ubuntu-Fix Format issue in graphical mode.

    v1.2.8 10/25/2019
      * Handle MSIX affinity.

    v1.2.6 05/15/2019
      * Support kernel 5.0.

    v1.2.5 05/15/2019
      * Fixup system crash if Toshiba NVMe controller installed.

    v1.2.4 04/29/2019
      * Support SSD7103.

    v1.2.2 04/25/2019
      * Support RAID10.

    v1.2.0 03/21/2019
      * NVMe controller hot replace.

    v1.0.0 01/10/2019
      * First Linux release.

#############################################################################
9. Management Revision history
#############################################################################
    v3.2.3  6/27/2024
      * The installation method has been updated to makeself installation.
      * Add additional information about enclosure , and fixed the error that
        the current link speed and Cryptographic Erace Capable were displayed.
      * Support displaying temperature, fan, and power consumption graphs. 
      * Support updating firmware for enclosure.
      * Support setting parameter for enclosure.
      * Support setting fan speed for enclosure.
      * Support identifying LED for device.
      * Display events for different enclsoures separately.
      * Support beeper control for for NVMe Controller.
      * Add a default task that check all disks every minute.
      * Remove the feature to set temperature threshold and temperature
        threshold is set to the Warning Composite Temperature Threshold of NVMe
        by default
	
    v3.1.15 10/25/2023
      * Optimze the display on the Physical page.
      * Optimze Health Inspector Scheduler.
      * Support temperature monitor task.
      * Remove the RAID feature for a non-RAID board.
      * Fix a bug where RAID could still be created with the wrong number of
        disks in CLI.
      * Fix a bug that send non-standard NVMe commands frequently.

    v3.1.14 04/21/2023
      * Support SED function.

    v3.1.13 12/05/2022
      * Fix a bug that displayed the enclosure model name error.
      * Fix a bug that hptsvr cannot startup on Rocky.

    v3.1.12 11/01/2022
      * Add installation log.
      * Modify CLI delete operation feedback exception.
      * Modify CLI set operation feedback exception.
      * Support for parsing of new versions of the BLF file format.
      * Fix a problem with some products displaying the LOGICAL button.

    v3.1.11 09/28/2022
      * Add crash information to diag.
      * Support setting password to cli.
      * Support remote control to cli.
      * Disable clearing event.

    v3.1.10 09/27/2022
      * Support different blf file versions.

    v3.1.9  09/16/2022
      * Support cards with different RAID configurations.

    v3.1.8  08/05/2022
      * Fix a bug that diag function cannot work normally.
      * Display enclosure information synchronously with WEBGUI to cli.
      * Optimize login steps to cli.

    v3.1.7  07/15/2022
      * Add MCU version display.
      * Only support firmware update using blf file format.
      * Add ver commmad to cli.
      * Fix a bug that disk can be initialized when it is being in use to cli.

    v3.1.6  06/22/2022
      * Fix a bug that ATA smart information displays error.
      * Improve CLI commmand input checking.
	  
    v3.1.5  06/10/2022
      * Support UnionTech OS.
      * Add program running log.
      * Fix a bug that cannot stop init array to cli.
      * Fix a bug that cannot expand/migrated array to cli.

    v3.1.4  04/27/2022
      * Support Kylin OS.
      * Fix some CLI commands display error.

    v3.1.3  04/15/2022
      * Add Array WWN information.
      * Add update MCU to WEBGUI.

    v3.1.2  04/01/2022
      * Add BIOS and temperture information for controller and enclosure.
      * Add update BIOS/Firmware to cli.

    v3.1.1  03/24/2022
      * Add extra information for controller and enclosure.

    v3.1.0  03/09/2022
      * Add identify LED to cli.

    v3.0.8  01/12/2022
      * Support SSD6200.

    v3.0.7  11/12/2021
      * Support multi-board and multi-drive detection.
      * Add error printing and suggestions to cli.
    
    v3.0.6  11/09/2021
      * Fix a bug that WebGUI cannot be displayed normally after restarting
      * system when the driver delays loading disks.
      * Change RAID 1/0 to RAID 10.
      * Support PCIe 4.0 and PCIe 5.0. 

    v3.0.4  05/13/2021
      * Update openssl to 3.0 to fix the bug of email sending failure.
      * 32 bit systems are no longer supported.
      * Fix a bug that failed to override the old version installation on
        Fedora 33.
    
    v3.0.3  05/10/2021
      * Fix the Segmentation fault of hptraidconf.
    
    v3.0.2  04/07/2021
      * Add 'diag' command to hptraidconf to collect diagnostic information.
    
    v3.0.1  03/29/2021
      * Fix the display of Recover view.
      * Fix the version time of the saved Index view.
          
    v3.0.0  02/05/2021
      * Support Diagnostic.
      * Fix a bug that when Fedora 33 has the command 'dpkg', WebGUI cannot be
        installed successfully.
      * Make diagnostic page browser compatible for IE, Chrome, Fire Fox and
        Opera.
      * Diagnostic page support rr3740a/hptnvme/rr640xl/rr272x/ssd711x
        detection.
          
    v2.3.15  04/17/2020
      * Fix a bug that when the libreadline version is higher than 7, WebGUI
        cannot be installed successfully.

    v2.3.14.1  07/26/2017
      * Support NVMe.
          
    v2.3.11  08/08/2016
      * Fix an upload recover list error.

    v2.3.10  07/24/2016
      * Support RR840A.

    v2.3.8  05/25/2016
      * Support RR3740A.

    v2.3.6  04/27/2016
	  * Fix bugs about cli task.
	  * Fix a installation bug.
      * Hptcfg is out of use.

    v2.3.5  04/12/2015
      * Support updating LCD firmware and screen message.
      * Support auto login.

    v2.3.4  09/11/2015
      * Support LCD firmware update.

    v2.3.3  01/09/2015
      * Restrict password length to 8 characters.
      * Support NewTek.

    v2.3.2.1  11/02/2015
      * Auto remove old version WebGUI during installation.

    v2.3.2  19/12/2014
      * Support 4Kn drive.

    v2.3.1  20/10/2014
      * The tape's OS name in WebGUI logical page will be displayed as the
        tape's model number instead of "HPT DISK x_x".

    v2.3.0  28/09/2014
      * Support SAS tape and media changer device.
      * Support DV mode array.

    v2.2.6  13/01/2014
      * Fix Issue Of EventLevel Show.
      * Change the method of install software.

    v2.2.4  24/12/2013
      * Fix sector size cannot be properly restored in Recover and so on.

    v2.2.2  09/12/2013
      * Add CLI(hptraidconf) Program.
          
    v2.2.1  15/11/2013
      * Add deb package.
          
    v2.2.0-13.1031  31/10/2013
      * Add Support Rocket/DataCenter Series.
      * Add Support SRC.
          
    v2.1.5-13.0409  09/04/2013
      * Support EJ340.
      * Support RS5345 PM.
      * Support RS5315 PM.
          
    v2.1.4-12.0921  21/09/2012
      * Add Support RR642L.
 
    v2.1.3-12.0829  29/08/2012
      * Add Support RR4522.
   
    v2.1.2.12.0718 18/07/2012
      * Add online help.
      * Support for SMTP/SSL.
      * Support for Recover.

    v2.1.11.0822 22/08/2011
      * Support for EJ6172 Firmware Update.
         
    v2.0.11.0713 13/07/2011
      * Support for OCE/ORLM.

    v2.0.0 Beta 29/4/2011
      * Totally new GUI layout.
      * Support for EJ220+rr2720.
        
#############################################################################
10. Technical support and service
#############################################################################

  If you have questions about installing or using your HighPoint product,
  check the user's guide or readme file first, and you will find answers to
  most of your questions here. If you need further assistance, please
  contact us. We offer the following support and information services:

  1)  The HighPoint Web Site provides information on software upgrades,
      answers to common questions, and other topics. The Web Site is
      available from Internet 24 hours a day, 7 days a week, at
      http://www.highpoint-tech.com.

  2)  For technical support, send e-mail to support@highpoint-tech.com and
      attach file /var/log/hptdrv.log if possible.

  NOTE: Before you send an e-mail, please visit our Web Site
        (http://www.highpoint-tech.com) to check if there is a new or 
        updated device driver for your system.

