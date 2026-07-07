# 01/23/2024 to 01/26/2024
## WR Switch
- Between 01/23/2024 and 01/26/2024, the NRDZ system underwent some changes and improvements.
- The White Rabbit (WR) network switch needed to be upgraded from version 5.0.1 to 6.0.1: https://ohwr.org/project/wrs-lj-hw/wikis/Downloads.
- The WR tech support that can be reached through email with timingsupport@nav-timing.safrangroup.com were very helpful.
- They initially gave me the wrong firmware image for update. We specifically needed the low jitter images that are associated with this network switch.
- To update the firmware, copy the tar binaries file to the /update partition on the switch as wrs-firmware.tar then reboot the switch, and it should be good.
- If it doesn't startup well oor has issues such as repeatedly rebooting, then the wrong firmware image was used.
- More details can be found in the user's and developers manual here: https://ohwr.org/project/wr-switch-sw/wikis/uploads/9c5b7da86c14f4380e1f57813f74140d/wrs-user-manual-v6.1.pdf and https://ohwr.org/project/wr-switch-sw/wikis/uploads/06189a542dc563f95d9387654bd2c7f2/wrs-developer-manual-6.1.pdf
- These manuals are not for the specific firmware version. Unfortunately, the specific manual doesn't exist. The steps should be and so far have been the same though.
- The WR switch has currently successfully been updated to version 6.0.1.
- During debugging of the WR Switch, the IP address was found out by direclty connecting to the serial management port on the switch. Using Putty on windows with the serial port name found in the device settings (COM3 in my case) and a baud rate of 115200, I was able to connect with the WR switch.
- By connecting to it this way, the IP address shows up in the switch name on the terminal. The switch could then be accessed remotely over the network with ssh.

## Sensor Deployment
- Fixes and improvement to the sensors have also been  made.
- The GATE sensor has had the fixed EMI box and preamplifier box from CU Boulder deployed. The antenna joint has also been glued to prevent it from bending and deployed at the sensor station.
- The NORTH sensor antenna joint has also been glued to prevent it from bending and deployed at the sensor station.
- The CHIME EMI box and preamplifier box have also been deployed. The wideband amplifier in the EMI box was replaced and the LNA in the preamplifier box was also replaced. Both boxes were tested before they were deployed.
- The preamplifier box of the sensor neighboring the GATE sensor was drenched in rain water so still needs to be replaced.
- All sensors are currently connected to the WR switch except for the OFFICE sensor which is on it's own pipeline.
