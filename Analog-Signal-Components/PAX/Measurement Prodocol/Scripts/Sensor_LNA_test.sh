#!/bin/sh

host=pax
port=23
pass='help'

echo open ${host} ${port}
sleep 2
echo ${pass}
sleep 2
echo "lnabiaslatch"
sleep 1
echo "getvg x"
sleep 1
echo "getvd x"
sleep 1
echo "getvm x"
sleep 1
echo "getid x"
sleep 1
echo "lnabiaslatch"
sleep 1
echo "getvg y"
sleep 1
echo "getvd y"
sleep 1
echo "getvm y"
sleep 1
echo "getid y"
sleep 1
echo "lnabiasoff"
sleep 1
echo "getonboardtemp"
sleep 1
echo "getsoftwareversion"
sleep 1
