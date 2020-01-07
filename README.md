# Home Directory

This repo contains basic configuration files for a Linux environment.

This script basically installs and configures several essential tools using your system's default package manager or build from source. Several modes can be chosen

# Author

Xiao Zhang

# Mode

Each mode corresponds to one use case. For example, if you just fresh installed a Linux desktop and wished to have vim configured, run `.\/configure --desktop`

## Desktop

triggered by `--desktop`

installs the following things:
- gcc
- make
- cmake
- g++
- python3
- vim
- node(for vim plugin YCM)

configures as described below:
- vim: install all plugins

## Node Server

triggered by `--node`

installs the following things:
- gcc
- g++
- make
- cmake
- node
- vim
- python3

configures as described below:
- vim: installs basic plugins

## PostgreSQL Server

triggered by `--pgsql`

installs the fowllowing things:
- gcc
- g++
- make
- cmake
- vim
- python3
- bison
- flex
- openssl
- readline
- pgsql

configures as described below:
- pgsql: start on reboot

# Pre-requisite

bash 4+, apt/yum if you want to install packages through package manager

# Usage

1. clone this repo to your home directory. Normally it is **$HOME**.
2. make sure you have backed up *.bashrc*, *.vimrc* and *.vim/* before proceeding
3. read *configure.sh* before proceeding as you should never trust a script before reading it
4. run *.\/configure.sh* with arguments

# Configuration

- **--desktop** Default. Enables all defaults and adds g++, python3, vim and desktop vim configuration
- **--server** If specified, enables all defaults and adds g++, python, python3, vim and server vim configuration
- **--default** If specified, enables only cmake, gcc and make
- **--no-cmake** If specified, don't try to install cmake
- **--no-make** If specified, don't try to install make
- **--no-gcc** If specified, don't try to install gcc
- **--g++** If specified, installs g++
- **--python** If specified enables python2
- **--python3** If specified enables python3
- **--vim** If specified installs vim
- **--fancy-vim** If specified installs vim and configures vim for normal desktop user
- **--bashrc** If specified, overwrite your bashrc.

note1: if multiple options from *default*, *desktop* and *server* are specified, only the first one takes effect.

note2: if a meta option conflicts with a basic option, the basic option overloads the meta one. e.g. when *desktop* and *no-gcc* are both specified, all *desktop* options will be enabled but gcc.

note3: if any of *desktop*, *fancy-vim* o
