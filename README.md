# Kickstarter

Installs and configures several useful tools for different environments.

Warning: When run on Linux, sudo permission is required therefore **please read the script before running!**

# Author

Xiao Zhang

# Usage
Ubuntu18+ or CentOS 7+
```
./configure.sh --desktop
```
Windows 10
```
.\configure.ps1 --desktop
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

# Pre-requisite

## Windows

- powershell 5+ with core modules
- .Net 4.5+

## Linux

bash 4+, apt/yum to install packages through package manager

sudo permission as many packages need to be installed with root permission.

# Usage

1. clone this repo.
2. make sure you have backed up *.bashrc*, *.vimrc*, *_vimrc*, *.vim/* and *vimfiles/* before proceeding. They are normally found under your $HOME directory.
3. read the script before proceeding as you should never trust a script before reading it
4. run *.\/configure.sh* with mode

note1: only the first specified mode has effect, the latter modes will be ignored.
note2: `--bashrc` needs to be specified if $HOME/.bashrc needs to be overwritten
