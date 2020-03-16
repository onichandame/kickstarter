#!/usr/bin/env bash

PACK_MAN=
if [ -n "$(command -v apt)" ]
then
  PACK_MAN=apt
elif [ -n "$(command -v dnf)" ]
then
  PACK_MAN=dnf
elif [ -n "$(command -v yum)" ]
then
  PACK_MAN=yum
fi

REQUIREMENTS="./prequirements.txt"

while IFS= read -r line
do
  sudo $PACK_MAN install $line -y
done < "$REQUIREMENTS"
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python configure.py $@
