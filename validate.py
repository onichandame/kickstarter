from utils.get_os import get_os, OS
from utils.get_argv import get_argv
from utils.terminate import terminate

def validate():
    check_args()
    check_os()

def check_args():
    get_argv()

def check_os():
    if check_os() == OS.UNKNOWN:
        terminate('currently only windows, ubuntu and centos is supported')
