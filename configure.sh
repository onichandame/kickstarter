#!/usr/bin/env bash

# global flag switching on/off features

declare -A APP_PACKMAN
declare -A APP_SOURCE

BASHRC=

main(){

  META=
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
    elif [ "$PARAM" = "--bashrc" ]
    then
      BASHRC=true
    fi
  done

  # unpack meta options
  if [ "$META" = desktop ]
  then
    APP_PACKMAN[GCC]=true
    APP_PACKMAN[MAKE]=true
    APP_PACKMAN[CMAKE]=true
    APP_PACKMAN[CXX]=true
    APP_PACKMAN[PYTHON3]=true
    APP_SOURCE[NODE]=true
    APP_SOURCE[VIM]=true
    APP_SOURCE[FANCY_VIM]=true
  elif [ "$META" = server ]
  then
    APP_PACKMAN[GCC]=true
    APP_PACKMAN[CXX]=true
    APP_PACKMAN[MAKE]=true
    APP_PACKMAN[CMAKE]=true
    APP_PACKMAN[PYTHON3]=true
    APP_PACKMAN[VIM]=true
  fi

  # check package manager
  if [ -z "$(command -v apt)" ] && [ -z "$(command -v yum)" ]
  then
    echo "no package manager is found. support for this situation has yet been implemented"
    exit 1
  fi

  # copy .bashrc
  if [ "$BASHRC" = true ]
  then
    echo "copying .bashrc to your home! Are you sure!(Y/y)"
    read -n1 COMMAND
    if [ "$COMMAND" = "Y" ] || [ "$COMMAND" = "y" ]
    then
      cp -f bashrc $HOME/.bashrc
    fi
  fi

  # install packages from docker
  install_docker

  # install packages from source
  install_src
}

install_src () {
  # comprehend list of packages by packman
  PACKAGES=""
  if [ "${APP_PACKMAN[GCC]}" = true ]
  then
    PACKAGES+="gcc "
  fi
  if [ "${APP_PACKMAN[CXX]}" = true ]
  then
    if [ -n "$(command -v apt)" ]
    then
      PACKAGES+="gcc "
    elif [ -n "$(command -v yum)" ]
    then
      PACKAGES+="gcc-c++ "
    fi
  fi
  if [ "${APP_PACKMAN[MAKE]}" = true ]
  then
    PACKAGES+="make "
  fi
  if [ "${APP_PACKMAN[CMAKE]}" = true ]
  then
    PACKAGES+="cmake "
  fi
  if [ "${APP_PACKMAN[PYTHON]}" = true ]
  then
    PACKAGES+="python "
  fi
  if [ "${APP_PACKMAN[PYTHON3]}" = true ]
  then
    PACKAGES+="python3 "
  fi
  if [ "${APP_PACKMAN[BISON]}" = true ]
  then
    PACKAGES+="bison "
  fi
  if [ "${APP_PACKMAN[FLEX]}" = true ]
  then
    PACKAGES+="flex "
  fi
  if [ "${APP_PACKMAN[OPENSSL]}" = true ]
  then
    if [ -n "$(command -v apt)" ]
    then
      PACKAGES+="openssl "
    elif [ -n "$(command -v yum)" ]
    then
      PACKAGES+="openssl-devel "
    fi
  fi
  if [ "${APP_PACKMAN[READLINE]}" = true ]
  then
    if [ -n "$(command -v apt)" ]
    then
      PACKAGES+="libreadline-dev "
    elif [ -n "$(command -v yum)" ]
    then
      PACKAGES+="readline-devel "
    fi
  fi
  if [ "${APP_PACKMAN[ZLIB]}" = true ]
  then
    if [ -n "$(command -v apt)" ]
    then
      PACKAGES+="zlib1g "
    elif [ -n "$(command -v yum)" ]
    then
      PACKAGES+="zlib-devel "
    fi
  fi
  if [ "${APP_PACKMAN[VIM]}" = true ]
  then
    PACKAGES+="vim "
  fi
  if [ "${APP_SOURCE[NODE]}" = true ]
  then
    PACKAGES+="nasm "
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

  PACKAGES=
  if [ "${APP_SOURCE[VIM]}" = true ]
  then
    PACKAGES+="--vim "
  fi
  if [ "${APP_SOURCE[FANCY_VIM]}" = true ]
  then
    PACKAGES+="--fancy-vim "
  fi
  if [ "${APP_SOURCE[NODE]}" = true ]
  then
    PACKAGES+="--node "
  fi

  if [ -n "$PACKAGES" ]
  then
    cd install_from_source
    python3 configure.py ${PACKAGES}
    if [ $? -ne 0 ]
    then
      cd -
      echo "Installation failed. Try removing all previously-installed applications then retry"
      exit 1
    fi
    cd -
  fi
}

install_docker() {
  if [ -n "$(command -v apt)" ]
  then
    sudo apt-get remove docker docker-engine docker.io containerd runc -y
    sudo apt-get update -y
    sudo apt-get install \
         apt-transport-https \
         ca-certificates \
         curl \
         gnupg-agent \
         software-properties-common -y
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ARCH="$(arch)"
				sudo add-apt-repository \
    "deb [arch=$ARCH] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io -y
  elif [ -n "$(command -v yum)" ]
  then
    sudo yum remove docker \
                    docker-client \
                    docker-client-latest \
                    docker-common \
                    docker-latest \
                    docker-latest-logrotate \
                    docker-logrotate \
                    docker-engine -y
				sudo yum install -y yum-utils \
                        device-mapper-persistent-data \
                        lvm2 -y
    sudo yum-config-manager \
         --add-repo \
         https://download.docker.com/linux/centos/docker-ce.repo
    sudo yum install docker-ce docker-ce-cli containerd.io -y
  fi
  echo Docker is now installed on the system. Try `docker run hello-world` to test its functionality
}

main "$@"; exit
