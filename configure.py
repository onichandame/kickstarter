from install_apps import install_apps
from install_keys import install_keys
from init_home import init_home
from common.get_os import get_os, OS
from common.terminate import terminate
from common.get_argv import get_argv

def main():
    check_args()
    check_os()
    install_apps()
    install_keys()
    init_home()

def check_args():
    get_argv()

def check_os():
    if check_os() == OS.UNKNOWN:
        terminate('currently only windows, ubuntu and centos is supported')

if __name__ == '__main__':
    main()
