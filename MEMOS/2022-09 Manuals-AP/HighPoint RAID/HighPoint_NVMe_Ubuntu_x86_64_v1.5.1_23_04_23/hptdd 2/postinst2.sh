#!/bin/bash
# THis is the module name. Should be valid.
HPTMOD=hptnvme

#
# Do NOT edit the following in most cases
#
RELEASES=$( ls /lib/modules/ )

if which mkinitramfs >/dev/null 2>/dev/null ; then
	mkinitrd=mkinitramfs
else
	mkinitrd=mkinitrd
fi

#udevadm control --reload
#sleep 1
#udevadm trigger
#sleep 1

if [ -f /etc/${mkinitrd}/modules ]; then # debian 3.1, ubuntu 5.10 (6.x? 7.x?)
	cat /etc/${mkinitrd}/modules | grep "^$HPTMOD" -s -q || echo $HPTMOD >> /etc/${mkinitrd}/modules
elif [ -f /etc/initramfs-tools/modules ]; then # debian 4.0
	cat /etc/initramfs-tools/modules | grep "^$HPTMOD" -s -q || echo $HPTMOD >> /etc/initramfs-tools/modules
else
	echo "Error!!! No initrd config file found, no initrd file generated."
	exit 1
fi

#if which update-initramfs >/dev/null 2>/dev/null ; then
#  update-initramfs -u -k all
#else
  for RELEASE in ${RELEASES}; do
	depmod -a ${RELEASE} >/dev/null 2>/dev/null
	if [ -f /boot/initrd.img-${RELEASE} ]; then
	  mv /boot/initrd.img-${RELEASE} -f /boot/initrd.img-${RELEASE}.hpt.bak
	fi
	${mkinitrd} -o /boot/initrd.img-${RELEASE} ${RELEASE}
  done
#fi

if [ ! -d /etc/default/grub.d ]; then
	mkdir /etc/default/grub.d
fi

echo "GRUB_CMDLINE_LINUX=\"intel_iommu=off amd_iommu=off\"" > /etc/default/grub.d/90_iommuoff.cfg

update-grub

cp /etc/fstab{,.orig}

cat /etc/fstab.orig | grep ^/dev/hptblock | cut -d\  -f1 | while read line; do
	uuid=`blkid -o export $line | grep ^UUID= | cut -d= -f2`
	if [ "$uuid" != "" ]; then
		sed -i s"#^$line #/dev/disk/by-uuid/$uuid #" /etc/fstab
	fi
done 

name="vmlinuz-$(uname -r)"
cfg=$( ls /boot/grub/grub.cfg )
cp ${cfg} ${cfg}.bak
j=0
k=0
if test "${cfg}" = ""; then
	echo "ERROR!!! Cannot find grub.cfg."
fi
msg=$(grep -n -E "^[[:space:]]*set default" ${cfg} | grep -v '\$')
if test "${msg}" != ""; then
	curno=$(echo $msg | cut -d= -f2 | cut -d\  -f2 | sed s'#\"##'g)
	curlineno=$(echo $msg | cut -d: -f1)
fi
p=(`grep -n -E '^[[:space:]]*(menuentry|submenu|}|\{)[[:space:]]*' "${cfg}" | cut -d: -f1`)
subcount=-1
insub=0
for s in ${p[@]}; do
    if sed -n ${s}p ${cfg} | grep -s -q ^[[:space:]]*submenu; then
      insub=1
      j=$(expr $j + 1)
      k=0
      subcount=0
    elif sed -n ${s}p ${cfg} | grep -s -q ^[[:space:]]*menuentry[[:space:]]; then
      if test $insub -eq 1; then
        k=$(expr $k + 1)
        subcount=$(expr $subcount + 1)
      else
        j=$(expr $j + 1)
      fi
      line=(`sed -n "${s},/}/p" "${cfg}" | grep ^[[:space:]]*linux | tail -1`)
      #echo ${line[@]}
      kernel=$(basename "${line[1]}")
      if test "${kernel}" = "${name}"; then
        #echo "setdefaultkernel: final no $no line $curlineno j $j k $k subcount $subcount insub $insub $line[1] ${kernel} ${name}"
        j=$(expr $j - 1)
        if test $insub -eq 1; then
          k=$(expr $k - 1)
          no="$j>$k"
        else
          no="$j"
        fi
        #echo "no [$no] <${curno}>"
        if test "${curno}" = "${no}"; then
          echo "setdefaultkernel:No change."
        elif test "${curno}" = ""; then
          sed -i 4a"sed default=\"${no}\"" "${cfg}"
        elif test "${curlineno}" != ""; then
          sed -i "${curlineno}"s"#${curno}#${no}#" "${cfg}"
        else
          line=$(grep -n "^set default" ${cfg} | cut -d: -f1)
          sed -i "${line}"s"#${curno}#${no}#" "${cfg}"
        fi
      fi
    elif sed -n ${s}p ${cfg} | grep -s -q ^[[:space:]]*\}; then
      if test $insub -eq 1; then
        subcount=$(expr $subcount - 1)
        if test $subcount -eq -1; then
          insub=0
          k=0
        fi
      fi
    fi
done

exit 0
