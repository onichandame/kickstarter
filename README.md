# Home Directory

This repo contains basic configuration files for a Linux environment.

This script basically installs several essential tools using your system's default package manager and installs vim from source. details of vim installation can be found at [README.md](https://github.com/onichandame/vim-configure/README.md)

# Author

Xiao Zhang

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
