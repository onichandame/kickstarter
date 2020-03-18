# Kickstarter

Installs and configures several useful tools for different environments.

Warning: When run on Linux, sudo permission is required therefore **please read the script before running!**

# Author

Xiao Zhang

# Usage

Ubuntu18+ or CentOS 7+

```bash
sudo ./configure.sh --desktop --bashrc --vimrc
```

# Mode

There are 4 pre-set modes defining different sets of tools to be installed.

- required(must specify one of the two options):
  - desktop: environment for workstation
  - server: environment for production server
- optional(any number of the options can be specified):
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

1. add docker for desktop
2. add dummy mode for updating bashrc and vimrc
3. add kubernetes for server/desktop
4. pass github username as an argument
5. specify whether to install ssh keys by arguments
