#!/usr/bin/env bash

PACK_MAN=
if [ -n "$(command -v apt)" ]
then
  PACK_MAN=apt
elif [ -n "$(command -v yum)" ]
then
  PACK_MAN=yum
fi
sudo $PACK_MAN install python3 python3-pip -y
sudo python3 -m pip install distro
sudo python3 configure.py $@
