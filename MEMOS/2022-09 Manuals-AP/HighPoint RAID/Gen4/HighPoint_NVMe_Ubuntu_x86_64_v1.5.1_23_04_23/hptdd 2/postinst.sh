#!/bin/sh
# Post installation for debian 3.1 installation

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

if [ ! -d /target/lib/modules/ ]; then
	echo "Error! Can not find any system module installation directory!";
	exit 1;
fi

RELEASES=$( ls /target/lib/modules/ )

if test "${RELEASES}set" = "set" ; then
	echo "Error! No kernel package has been installed!";
	exit 1;
fi

if [ "`/target/bin/uname -m`" = "x86_64" ];then
	ARCH=x86_64
else
	ARCH=i386
fi

for RELEASE in ${RELEASES}; do
	if [ -f ${FLOPPY}/boot/${HPTMOD}${RELEASE}${ARCH}.ko.gz ] ; then
		if test $HPTMOD = "hptmv" || test $HPTMOD = "hptmv6" || test $HPTMOD = "rr174x" || test $HPTMOD = "rr2310_00"; then
			find /target/lib/modules/${RELEASE} -name 'sata_mv.*' -delete > /dev/null 2>&1
			find /target/lib/modules/${RELEASE} -name 'sata_mv.*' -exec rm {} \;
		fi
		if test $HPTMOD = "rr272x_1x" || test $HPTMOD = "rr274x_3x" || test $HPTMOD = "rr276x" || test $HPTMOD = "rr278x" ; then
			find /target/lib/modules/${RELEASE} -name 'mvsas.*' -delete > /dev/null 2>&1
			find /target/lib/modules/${RELEASE} -name 'mvsas.*' -exec rm {} \;
		fi
		if test $HPTMOD = "hptiop"; then
			find /target/lib/modules/${RELEASE} -name 'hptiop.*' -delete > /dev/null 2>&1
			find /target/lib/modules/${RELEASE} -name 'hptiop.*' -exec rm {} \;
		fi
		if test $HPTMOD = "hpt374" || test $HPTMOD = "hpt37x2"; then
			find /target/lib/modules/${RELEASE} -name 'pata_hpt*.*' -delete > /dev/null 2>&1
			find /target/lib/modules/${RELEASE} -name 'hpt366.*' -delete > /dev/null 2>&1
			find /target/lib/modules/${RELEASE} -name 'pata_hpt*.*' -exec rm {} \;
			find /target/lib/modules/${RELEASE} -name 'hpt366.*' -exec rm {} \;
		fi
		zcat ${FLOPPY}/boot/$HPTMOD${RELEASE}${ARCH}.ko.gz > /target/lib/modules/${RELEASE}/kernel/drivers/scsi/${HPTMOD}.ko	
	fi
done

if ! cp ${FLOPPY}/60-persistent-storage-hptblock.rules /target/etc/udev/rules.d/ ; then
	echo "ERROR! Failed to install udev rule for hptblock."
	exit 1
fi

chmod 644 /target/etc/udev/rules.d/60-persistent-storage-hptblock.rules

cp $FLOPPY/hptdrv       /target/etc/initramfs-tools/scripts/init-top/
cp $FLOPPY/hptblock     /target/usr/share/initramfs-tools/hooks/
cp $FLOPPY/postinst2.sh /target/tmp/

chmod 644 /target/etc/udev/rules.d/60-persistent-storage-hptblock.rules

chmod 755 /target/etc/initramfs-tools/scripts/init-top/hptdrv \
	  /target/usr/share/initramfs-tools/hooks/hptblock \
	  /target/tmp/postinst2.sh

sync

mntdev=""
mntsys=""
mntproc=""

block=`mount | grep /target\  | cut -d\  -f1`
if test "$block"s = "s"; then
  echo "Error: empty block device, quit"
  mount
  exit 1 
fi
if [ ! -e /target/$block ] ; then
  mntdev="1"
  mount -o bind /dev /target/dev
fi

if [ ! -e /target/run/udev/control ] ; then
  mntrun="1"
  mount -o bind /run /target/run
fi

if [ ! -e /target/sys/bus/pci/rescan ] ; then
  mntsys="1"
  mount -t sysfs none /target/sys
fi

if [ ! -e /target/proc/version ] ; then
  mntproc="1"
  mount -t proc none /target/proc
fi

chroot /target /tmp/postinst2.sh

rm -f /target/tmp/postinst2.sh

if [ "$mntdev" != "" ]; then
  umount /target/dev
fi

if [ "$mntrun" != "" ]; then
  umount /target/run
fi

if [ "$mntsys" != "" ]; then
  umount /target/sys
fi

if [ "$mntproc" != "" ]; then
  umount /target/proc
fi

echo "We have completed the driver installation."

exit 0

