#!/usr/bin/env bash

# global flag switching on/off features

declare -A FLAG
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
  META=desktop
  META_SET=

  # parse arguments
  for PARAM in "$@"
  do
    if [ "$PARAM" = "--desktop" ]
    then
      if [ -z "$META_SET" ]
      then
        META=desktop
        META_SET=true
      fi
    elif [ "$PARAM" = "--server" ]
    then
      if [ -z "$META_SET"]
      then
        META=server
        META_SET=true
      fi
    elif [ "$PARAM" = "--default" ]
    then
      if [ -z "$META_SET" ]
      then
        META=default
        META_SET=true
      fi
    elif [ "$PARAM" = "--no-cmake" ]
    then
        FLAG[CMAKE]=false
    elif [ "$PARAM" = "--no-make" ]
    then
        FLAG[MAKE]=false
    elif [ "$PARAM" = "--no-gcc" ]
    then
        FLAG[GCC]=false
    elif [ "$PARAM" = "--g++" ]
    then
        FLAG[GCC]=true
    elif [ "$PARAM" = "--python" ]
    then
        FLAG[PYTHON]=true
    elif [ "$PARAM" = "--python3" ]
    then
        FLAG[PYTHON3]=true
    elif [ "$PARAM" = "--vim" ]
    then
        FLAG[VIM]=true
    elif [ "$PARAM" = "--fancy-vim" ]
    then
        FLAG[FANCY_VIM]=true
    elif [ "$PARAM" = "--bashrc" ]
    then
        FLAG[BASHRC]=true
    fi
  done

  # unpack meta options
  if [ -z "${FLAG[GCC]}" ]
  then
    FLAG[GCC]=true
  fi
  if [ -z "${FLAG[MAKE]}" ]
  then
    FLAG[MAKE]=true
  fi
  if [ -z "${FLAG[CMAKE]}" ]
  then
    FLAG[CMAKE]=true
  fi
  if [ "$META" = desktop ]
  then
    if [ -z "${FLAG[GXX]}" ]
    then
      FLAG[GXX]=true
    fi
    if [ -z "${FLAG[PYTHON3]}" ]
    then
      FLAG[PYTHON3]=true
    fi
    if [ -z "${FLAG[VIM]}" ]
    then
      FLAG[VIM]=true
    fi
    if [ -z "${FLAG[FANCY_VIM]}" ]
    then
      FLAG[FANCY_VIM]=true
    fi
  elif [ "$META" = server ]
  then
    if [ -z "${FLAG[GXX]}" ]
    then
      FLAG[GXX]=true
    fi
    if [ -z "${FLAG[PYTHON]}" ]
    then
      FLAG[PYTHON]=true
    fi
    if [ -z "${FLAG[PYTHON3]}" ]
    then
      FLAG[PYTHON3]=true
    fi
    if [ -z "${FLAG[VIM]}" ]
    then
      FLAG[VIM]=true
    fi
  fi

  # check package manager
  if [ -z "$(command -v apt)" ] && [ -z "$(command -v yum)" ]
  then
    echo "no package manager is found. support for this situation has yet been implemented"
    exit 1
  fi

  # install packages
  install_pkg

  # copy .bashrc
  if [ "${FLAG[BASHRC]}" = true ]
  then
    echo "copying .bashrc to your home! Are you sure!(Y/y)"
    read -n1 COMMAND
    if [ "$COMMAND" = "Y" ] || [ "$COMMADN" = "y" ]
    then
      cp -f .bashrc $HOME/.bashrc
    fi
  fi

  # install vim
  if [ "${FLAG[VIM]}" = true ]
  then
    install_vim
  fi

  echo "Your environment has been set. Happy Linuxing!"
}

install_pkg () {
  # comprehend list of packages
  PACKAGES=""
  if [ "${FLAG[GCC]}" = true ]
  then
    PACKAGES+="gcc "
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
    if [ "${FLAG[PYTHON]}" = true ]
    then
      PACKAGES+="python-dev "
    fi
    if [ "${FLAG[PYTHON3]}" = true ]
    then
      PACKAGES+="python3-dev "
    fi
  elif [ -n "$(command -v yum)" ]
  then
    if [ "${FLAG[CXX]}" = true ]
    then
      PACKAGES+="gcc-c++ "
    fi
    if [ "${FLAG[PYTHON]}" = true ]
    then
      PACKAGES+="python-devel "
    fi
    if [ "${FLAG[PYTHON3]}" = true ]
    then
      PACKAGES+="python3-devel "
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
  git submodule update --remote --init --recursive
  if [ "$?" -ne 0 ]
  then
    echo "fetching submodule failed"
    exit 1
  fi
  cd install_from_source
  if [ "${FLAG[FANCY_VIM]}" = true ]
  then
    python3 configure.py --vim --fancy-vim
  else
    python3 configure.py --vim --no-fancy-vim
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
