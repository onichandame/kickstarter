#!/usr/bin/env bash

declare -A CONF
CONF[PYTHON]=false
CONF[PYTHON3]=true
CONF[VIM]=true
CONF[FANCY_VIM]=true
CONF[CXX]=true

PACK_MAN=""
PACKAGES=("cmake" "gcc" "make")

main(){

  declare -A ARGS
  ARGS[DESKTOP]=
  ARGS[SERVER]=
  ARGS[DEFAULT]=
  ARGS[CMAKE]=
  ARGS[MAKE]=
  ARGS[GCC]=
  ARGS[GXX]=
  ARGS[PYTHON]=
  ARGS[PYTHON3]=
  ARGS[VIM]=
  ARGS[FANCY_VIM]=

  for PARAM in "$@"
  do
    if [ "$PARAM" = "--desktop" ]
    then
      if [ -z "${ARGS[DESKTOP]}" ]
      then
        ARGS[DESKTOP]=true
        ARGS[SERVER]=false
        ARGS[DEFAULT]=true
      fi
    elif [ "$PARAM" = "--server" ]
      if [ -z "${ARGS[SERVER]}"]
      then
        ARGS[DESKTOP]=false
        ARGS[SERVER]=true
        ARGS[DEFAULT]=true
      fi
    elif [ "$PARAM" = "--default" ]
      if [ -z "${ARGS[DEFAULT]}" ]
      then
        ARGS[DEFAULT]=true
        ARGS[DESKTOP]=false
        ARGS[SERVER]=false
      fi
    elif [ "$PARAM" = "--no-cmake" ]
      if [ -z "${ARGS[CMAKE]}" ]
      then
        ARGS[CMAKE]=false
      fi
    fi
  done

  exit 0
  
  # Comprehend list of packages
  if [ -n "$(command -v apt)" ]
  then
    PACK_MAN="apt"
    PACKAGES=$PACKAGES" python3-dev g++"
  elif [ -n "$(command -v yum)" ]
  then
  #  curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
    PACKAGES=$PACKAGES" python3-devel gcc-c++"
    PACK_MAN="yum"
  fi
  
  # Install packages
  if [ -z "$PACK_MAN" ]
  then
    echo "No package manager was found! ARE YOU SURE that python3.3+ development headers, python3.3+ and cmake are available on the system?"
    read -n 1 -p "(Y/y)" CHOICE
    if [ "$CHOICE" != "y" ] && [ "$CHOICE" != "Y" ]
    then
      exit 0
    fi
  else
    install_pkg
  fi
  
  # Install vim from source
  install_vim
  
  # Overwrite .bashrc
  echo "packages were installed! do you wish to overwrite .bashrc?"
  read -n 1 -p "(Y/y)" CHOICE
  if [ "$CHOICE" != "y" ] && [ "$CHOICE" != "Y" ]
  then
    exit 0
  else
    cp -f .bashrc $HOME/.bashrc
  fi
}

install_pkg () {
  sudo $PACK_MAN install $PACKAGES -y
}

install_vim () {
  git submodule update --init vim
  cd vim
  python3 configure.py
  if [ $? -ne 0 ]
  then
    cd -
    echo "Vim installation failed. Try debugging it or contact the author"
    exit 1
  fi
  cd -
}

main "$@"; exit
