## Configuration of new/replacement Accelnet Servo Driver modules

When any new, never-been-used-in-the-ATA Accelnet Servo Driver modules are replaced in a DriveBox, the module(s) must be configured
before it will function correctly in an ATA antenna.  A DriveBox contains 2 modules, one for each axis motor (az and el), and each
has a separate configuration.

A configuration read/write utility `accelnet.py` is available on the ControlBox, as well as the two configuration data files present
in this folder.

## Post-replacement Procedure
Assuming one or both modules have been replaced in a DriveBox, and the DriveBox is installed in an antenna 
(or otherwise interfaced to a ControlBox), log into the ControlBox as _ataant_.  The `accelnet.py` utility is in `~/ata-boxes/utils`.

```
ataant@ant5c:~/ata-boxes/utils$ python3 accelnet.py -h
usage: accelnet [-h] {read,write} {az,el} [filename]

Accelnet module utility

positional arguments:
  {read,write}
  {az,el}
  filename

optional arguments:
  -h, --help    show this help message and exit
```

### Test if Accelnet servo driver is alive and communicating
A quick test to verify that the Accelnet module is powered and communicating over serial is just to readout its current configuration.

```
ataant@ant5c:~/$ cd ata-boxes/utils

# Test if az module is alive
ataant@ant5c:~/ata-boxes/utils$ python3 accelnet.py read az

# Also test el module as well
ataant@ant5c:~/ata-boxes/utils$ python3 accelnet.py read el
```
The commands should produce a lengthy register dump of addresses from 0x00 to 0xff like this excerpt:
```
f0x00 v 526
f0x01 v 100
f0x02 v 242
...
f0xfd e 9
f0xfe e 9
f0xff e 9
```

### Programming new configuration
Configuration files for both axes are located in the same `~/ata-boxes/utils` directory.

***Note that you must use python3 and not python!***
```
# Configure az module
ataant@ant5c:~/ata-boxes/utils$ python3 accelnet.py write az accelnet-az.dat

# Configure el module
ataant@ant5c:~/ata-boxes/utils$ python3 accelnet.py write el accelnet-el.dat
```
It is only necessary to configure new Accelnet modules that have been replaced.  I have seen cases where a module lost its configuration and was 
made to work again by reconfiguring, but I believe that complete failure followed soon after.


To read out a drive amplifier status fast and per axis run:

 ~obs/tkoumrian/drivebox.sh 3c az 
