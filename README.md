# Kickstarter

Installs and configures several useful tools for different environments.

Warning: When run on Linux, sudo permission is required therefore **please read the script before running!**

# Author

Xiao Zhang

# Usage

Ubuntu18+ or CentOS 7+

```bash
./configure.sh --desktop --bashrc --vimrc
```

# Mode

There are 4 pre-set modes defining different sets of tools to be installed.

- required:
  - desktop: environment for workstation
  - server: environment for production server
- optional:
  - bashrc: overwrites $HOME/.bashrc
  - vimrc: overwrites $HOME/.config/nvim/init.vim

# Common

Installed on both modes

- python3

## Desktop

triggered by `--desktop`

installs the following things if not found:

- gcc
- make
- cmake
- g++
- neovim(with all plugins)

## Server

triggered by `--server`

## Init

triggered by `--init`

installs the following things:

- bashrc
- init.vim(.vimrc equivalent for neovim)

# Pre-requisite

## Linux

bash 4+, CentOS or Ubuntu or the like.

sudo permission as many packages need to be installed with root permission.

# Roadmap

1. add neovim support for Ubuntu 18 and CentOS 7

2. add Qt for desktop, add node for both modes

3. add kubectl/kubeadm for server and minikube for desktop
