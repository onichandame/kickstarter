# Linux Kickstarter

Installs and configures several useful tools used in a fresh-installed Linux environment.

# Author

Xiao Zhang

# Mode

There are 2 pre-set modes defining different sets of tools to be installed.
- desktop: environment for everyday use
- server: environment for robust, long-running server not often interferred by human

## Desktop

triggered by `--desktop`

installs the following things if not found:
- gcc
- make
- cmake
- g++
- python3
- vim(with all plugins)
- node(for vim plugin YCM)
- docker

## Server

triggered by `--server`

### Initialization
installs the following things:
- gcc
- g++
- make
- cmake
- node
- vim(with basic plugins)
- python3
- docker

# Pre-requisite

bash 4+, apt/yum to install packages through package manager

sudo permission as many packages need to be installed with root permission.

# Usage

1. clone this repo to your home directory. Normally it is **$HOME**.
2. make sure you have backed up *.bashrc*, *.vimrc* and *.vim/* before proceeding
3. read *configure.sh* before proceeding as you should never trust a script before reading it
4. run *.\/configure.sh* with mode

note1: only the first specified mode has effect, the latter modes will be ignored.
note2: `--bashrc` needs to be specified if $HOME/.bashrc needs to be overwritten
