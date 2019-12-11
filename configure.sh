#!/usr/bin/env bash

# global flag switching on/off features

declare -A CONF
FLAG[CMAKE]=
FLAG[MAKE]=
FLAG[GCC]=
FLAG[PYTHON]=
FLAG[PYTHON3]=
FLAG[VIM]=
FLAG[FANCY_VIM]=
FLAG[CXX]=
FLAG[BASHRC]=

main(){

  declare -A ARGS
  ARGS[DESKTOP]=true
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
  ARGS[BASHRC]=

  # parse arguments
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
    then
      if [ -z "${ARGS[SERVER]}"]
      then
        ARGS[SERVER]=true
        ARGS[DESKTOP]=false
        ARGS[DEFAULT]=true
      fi
    elif [ "$PARAM" = "--default" ]
    then
      if [ -z "${ARGS[DEFAULT]}" ]
      then
        ARGS[DEFAULT]=true
        ARGS[DESKTOP]=false
        ARGS[SERVER]=false
      fi
    elif [ "$PARAM" = "--no-cmake" ]
    then
      if [ -z "${ARGS[CMAKE]}" ]
      then
        ARGS[CMAKE]=false
      fi
    elif [ "$PARAM" = "--no-make" ]
    then
      if [ -z "${ARGS[MAKE]}" ]
      then
        ARGS[MAKE]=false
      fi
    elif [ "$PARAM" = "--no-gcc" ]
    then
      if [ -z "${ARGS[GCC]}" ]
      then
        ARGS[GCC]=false
      fi
    elif [ "$PARAM" = "--g++" ]
    then
      if [ -z "${ARGS[GXX]}" ]
      then
        ARGS[GCC]=true
      fi
    elif [ "$PARAM" = "--python" ]
    then
      if [ -z "${ARGS[PYTHON]}" ]
      then
        ARGS[PYTHON]=true
      fi
    elif [ "$PARAM" = "--python3" ]
    then
      if [ -z "${ARGS[PYTHON3]}" ]
      then
        ARGS[PYTHON3]=true
      fi
    elif [ "$PARAM" = "--vim" ]
    then
      if [ -z "${ARGS[VIM]}" ]
      then
        ARGS[VIM]=true
      fi
    elif [ "$PARAM" = "--fancy-vim" ]
    then
      if [ -z "${ARGS[FANCY_VIM]}" ]
      then
        ARGS[FANCY_VIM]=true
      fi
    elif [ "$PARAM" = "--bashrc" ]
    then
      if [ -z "${ARGS[BASHRC]}" ]
      then
        ARGS[BASHRC]=true
      fi
    fi
  done

  # finalize arguments
  if [ "${ARGS[DEFAULT]}" = true ]
  then
    if [ -z "${ARGS[GCC]}" ]
    then
      ARGS[GCC]=true
    fi
    if [ -z "${ARGS[MAKE]}" ]
    then
      ARGS[MAKE]=true
    fi
    if [ -z "${ARGS[CMAKE]}" ]
    then
      ARGS[CMAKE]=true
    fi
  fi
  if [ "${ARGS[DESKTOP]} " = true ]
  then
    if [ -z "${ARGS[GXX]} " ]
    then
      ARGS[GXX]=true
    fi
    if [ -z "${ARGS[PYTHON3]} " ]
    then
      ARGS[PYTHON3]=true
    fi
    if [ -z "${ARGS[VIM]} " ]
    then
      ARGS[VIM]=true
    fi
    if [ -z "${ARGS[FANCY_VIM]} " ]
    then
      ARGS[FANCY_VIM]=true
    fi
  fi
  if [ "${ARGS[SERVER]} " = true ]
  then
    if [ -z "${ARGS[GXX]} " ]
    then
      ARGS[GXX]=true
    fi
    if [ -z "${ARGS[PYTHON]} " ]
    then
      ARGS[PYTHON]=true
    fi
    if [ -z "${ARGS[PYTHON3]} " ]
    then
      ARGS[PYTHON3]=true
    fi
    if [ -z "${ARGS[VIM]} " ]
    then
      ARGS[VIM]=true
    fi
  fi

  # populate flags
  if [ "${ARGS[CMAKE]} " = true ]
  then
    FLAG[CMAKE]=true
  fi
  if [ "${ARGS[MAKE]} " = true ]
  then
    FLAG[MAKE]=true
  fi
  if [ "${ARGS[GCC]} " = true ]
  then
    FLAG[GCC]=true
  fi
  if [ "${ARGS[PYTHON]} " = true ]
  then
    FLAG[PYTHON]=true
  fi
  if [ "${ARGS[PYTHON3]} " = true ]
  then
    FLAG[PYTHON3]=true
  fi
  if [ "${ARGS[VIM]} " = true ]
  then
    FLAG[VIM]=true
  fi
  if [ "${ARGS[FANCY_VIM]} " = true ]
  then
    FLAG[FANCY_VIM]=true
  fi
  if [ "${ARGS[CXX]} " = true ]
  then
    FLAG[CXX]=true
  fi
  if [ "${ARGS[BASHRC]} " = true ]
  then
    FLAG[BASHRC]=true
  fi

  # check package manager
  if [ -z "$(command -v apt)" ] && [ -z "$(command -v yum)" ]
  then
    echo "no package manager is found. support for this situation has yet been implemented"
    exit 1
  fi

  # install packages
  install_pkg

  # install vim
  if [ "$FLAG[VIM]" = true ]
  then
    install_vim
  fi

  # copy .bashrc
  if [ "$FLAG[BASHRC]" = true ]
  then
    cp -f .bashrc $HOME/.bashrc
  fi

  echo "Your environment has been set. Happy Linuxing!"
}

install_pkg () {
  # comprehend list of packages
  PACKAGES=""
  if [ "${FLAG[GCC]}" = true ]
  then
    PACKAGES+="cmake "
  fi
  if [ "${FLAG[MAKE]}" = true ]
  then
    PACKAGES+="make "
  fi
  if [ "${FLAG[CMAKE]}" = true ]
  then
    PACKAGES+="cmake "
  fi
  if [ "${FLAG[PYTHON]}" = true ]
  then
    PACKAGES+="python "
  fi
  if [ "${FLAG[PYTHON3]}" = true ]
  then
    PACKAGES+="python3 "
  fi
  if [ -n "$(command -v apt)" ]
  then
    if [ "${FLAG[CXX]}" = true ]
    then
      PACKAGES+="g++ "
    fi
  elif [ -n "$(command -v yum)" ]
  then
    if [ "${FLAG[CXX]}" = true ]
    then
      PACKAGES+="gcc-c++ "
    fi
  fi

  # get package manager
  PACK_MAN=
  if [ -n "$(command -v apt)" ]
  then
    PACK_MAN="apt"
  elif [ -n "$(command -v yum)" ]
  then
    PACK_MAN="yum"
  fi

  sudo $PACK_MAN install $PACKAGES -y
}

install_vim () {
  if [ "${FLAG[VIM]}" != true ]
  then
    return 1
  fi
  git submodule update --remote --init vim
  cd vim
  if [ "${FLAG[FANCY_VIM]}" = true ]
  then
    python3 configure.py --fancy-vim
  else
    python3 configure.py
  fi
  if [ $? -ne 0 ]
  then
    cd -
    echo "Vim installation failed. Try debugging it or contact the author"
    exit 1
  fi
  cd -
}

main "$@"; exit
