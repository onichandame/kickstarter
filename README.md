# System Manager

Auto management of any system can be acieved using this script. Currently only Linux is supported.

# Author

Xiao Zhang

# Architecture

A system is defined as:
- An integrated bunch of different utilities delevering a service
- Consisting of hardware part and software part
- Hardware part is a general purpose computer with several peripherals
- Software part is composed of OS and applications

The jobs this module is responsible of is managing the applications running on the system. Hardware and OS management is out of the scope.

A complete management utility must provides the following functions:
1. Initialization of the system
2. Auto backup of sensitive data
3. Monitoring the system status
4. Auto-restart on failure
5. Rollback to previous version if several retries of step 4 failed

Based on the purposes of the systems, several modes are provided.

# Mode

Each mode corresponds to one use case. For example, if you just fresh installed a Linux desktop and wished to have vim configured, run `./configure --desktop`

## Desktop

triggered by `--desktop`

### Initialization
installs the following things if not found:
- gcc
- make
- cmake
- g++
- python3
- vim(with all plugins)
- node(for vim plugin YCM)

### Backup
  Backup the entire $HOME directory after specifying the storage location

  backup requires tar, gzip, rsync to function

### Monitor
  No monitoring process is run as it is desktop which is controlled directly by human.

### Auto-restart
  Nothing is done for the above reason

### Rollback
  Nothing is done for the above reason

## Node Server

triggered by `--node`

### Initialization
installs the following things:
- gcc
- g++
- make
- cmake
- node
- vim(with basic plugins)
- python3

### Backup
  Backup the entire $HOME directory after specifying the storage location

  backup requires tar, gzip, rsync to function

### Monitor

### Auto-restart

### Rollback

## PostgreSQL Server

triggered by `--pgsql`

### Initialization
installs the fowllowing things:
- gcc
- g++
- make
- cmake
- vim(with basic plugins)
- python3
- bison
- flex
- openssl
- readline
- pgsql

### Backup
  Backup the entire $HOME directory after specifying the storage location

  backup requires tar, gzip, rsync to function

### Monitor

### Auto-restart

### Rollback

# Pre-requisite

bash 4+, apt/yum if you want to install packages through package manager

# Usage

1. clone this repo to your home directory. Normally it is **$HOME**.
2. make sure you have backed up *.bashrc*, *.vimrc* and *.vim/* before proceeding
3. read *configure.sh* before proceeding as you should never trust a script before reading it
4. run *.\/configure.sh* with mode

note1: only the first specified mode has effect, the latter modes will be ignored.
note2: `--bashrc` needs to be specified if $HOME/.bashrc needs to be installed
