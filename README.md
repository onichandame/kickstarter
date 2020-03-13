# Kickstarter

Installs and configures several useful tools for different environments.

Warning: When run on Linux, sudo permission is required therefore **please read the script before running!**

# Author

Xiao Zhang

# Usage

Ubuntu18+ or CentOS 7+

```bash
./configure.sh --desktop --init
```

Windows 10

```bash
.\configure.ps1 --desktop --init
```

# Mode

There are 2 pre-set modes defining different sets of tools to be installed.

- desktop: environment for everyday use and development
- server: environment for production

## Desktop

triggered by `--desktop`

installs the following things if not found:

- gcc
- make
- cmake
- g++
- python3
- neovim(with all plugins)
- docker

## Server

triggered by `--server`

installs the following things:

- python3
- docker

## Init

triggered by `--init`

installs the following things:

- bashrc
- init.vim(.vimrc equivalent for neovim)

# Pre-requisite

## Windows

- powershell 5+ with core modules
- .Net 4.5+

## Linux

bash 4+, apt/yum to install packages through package manager

sudo permission as many packages need to be installed with root permission.

# Roadmap

next subversion: add neovim support for Ubuntu 18 and CentOS 7

next minor version: add Qt for desktop, add node for both modes

next major version: not planned yet
