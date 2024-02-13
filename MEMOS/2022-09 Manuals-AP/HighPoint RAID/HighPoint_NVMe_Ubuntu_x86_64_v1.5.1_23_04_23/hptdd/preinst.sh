#!/bin/sh
# Pre installation for debian 3.1 installation

# THis is the module name. Should be valid.
HPTMOD=hptnvme

#
# Do NOT edit the following in most cases
#

if test "${HPTMOD}set" = "set" ; then
	echo "Error! Which module to install?";
	exit 1;
fi

FLOPPY=$( dirname $0 )

RELEASE=$( uname -r )
if [ "`uname -m`" = "x86_64" ];then
    ARCH=x86_64
else
    ARCH=i386
fi

# modprobe sd_mod >/dev/null 2>/dev/null

if test $HPTMOD = "hptmv" || test $HPTMOD = "hptmv6" || test $HPTMOD = "rr174x" || test $HPTMOD = "rr2310_00"; then
	find /lib/modules/${RELEASE} -name 'sata_mv.*' -delete > /dev/null 2>&1
	find /lib/modules/${RELEASE} -name 'sata_mv.*' -exec rm {} \;
	modprobe -r sata_mv 2> /dev/null
fi
if test $HPTMOD = "rr272x_1x" || test $HPTMOD = "rr274x_3x" || test $HPTMOD = "rr276x" || test $HPTMOD = "rr278x"; then
	find /lib/modules/${RELEASE} -name 'mvsas.*' -delete > /dev/null 2>&1
	find /lib/modules/${RELEASE} -name 'mvsas.*' -exec rm {} \;
	modprobe -r mvsas 2> /dev/null
fi
if test $HPTMOD = "hptmviop" || test $HPTMOD = "hptiop"; then
	find /lib/modules/${RELEASE} -name 'hptiop.*' -delete > /dev/null 2>&1
	find /lib/modules/${RELEASE} -name 'hptiop.*' -exec rm {} \;
	modprobe -r $HPTMOD 2> /dev/null
fi
if test $HPTMOD = "hpt374" || test $HPTMOD = "hpt37x2"; then
	find /lib/modules/${RELEASE} -name 'pata_hpt3*.*' -delete > /dev/null 2>&1
	find /lib/modules/${RELEASE} -name 'hpt366.*' -delete > /dev/null 2>&1
	find /lib/modules/${RELEASE} -name 'pata_hpt3*.*' -exec rm {} \;
	find /lib/modules/${RELEASE} -name 'hpt366.*' -exec rm {} \;
	modprobe -r hpt366 2> /dev/null
	modprobe -r pata_hpt366 2> /dev/null
	modprobe -r pata_hpt37x 2> /dev/null
	modprobe -r pata_hpt3x2n 2> /dev/null
	modprobe -r pata_hpt3x3 2> /dev/null
fi

if ! cp ${FLOPPY}/60-persistent-storage-hptblock.rules /etc/udev/rules.d/ ; then
	echo "ERROR! Failed to install udev rule for hptblock."
	exit 1
fi

chmod 644 /etc/udev/rules.d/60-persistent-storage-hptblock.rules

if [ -f /usr/share/grub-installer/grub-installer ]; then
	sed -i.bak s'#nvme#hptblock#'g /usr/share/grub-installer/grub-installer
	sed -i s'#hptblock\[0\-9\]\[0\-9\]\*n\[0\-9\]\[0\-9\]\*\\#hptblock\[0\-9\]\[0\-9\]\*n\[0\-9\]\[0\-9\]\*p\\#'g  /usr/share/grub-installer/grub-installer
	sed -i s'#hptblock\[0\-9\]\\+n\[0\-9\]\\+\\#hptblock\[0\-9\]\\+n\[0\-9\]\\+p\\#'g /usr/share/grub-installer/grub-installer

else
	(
		while [ ! -f /usr/bin/grub-installer ]; do sleep 10; done
		ls -d /sys/block/hptblock* | while read line; do
			name=`basename $line`
			dev=`cat $line/dev`
			tgt=`echo $name | sed s'#p\$##g'`
			maj=`echo $dev | cut -d: -f1` 
			min=`echo $dev | cut -d: -f2` 
			mknod /dev/$tgt b $maj $min 
		done 
		sleep 10
		sed -i.bak s'#nvme#hptblock#'g /usr/bin/grub-installer
	) &
fi

udevadm control --reload
sleep 1
udevadm trigger
sleep 1

zcat ${FLOPPY}/boot/$HPTMOD${RELEASE}${ARCH}.ko.gz > /tmp/$HPTMOD.ko
insmod /tmp/$HPTMOD.ko >/dev/null 2>/dev/null

if ( lsmod | grep $HPTMOD -s -q );then
  echo "This step succeeded!"
else
  echo "Error! This step failed!"
fi

