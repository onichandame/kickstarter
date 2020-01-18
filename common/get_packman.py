from .get_os import *

def get_packman():
    if get_os() == OS.WIN32:
        return 'scoop.cmd'
    elif get_os() == OS.UBUNTU:
        return 'apt'
    elif get_os() == OS.CENTOS:
        return 'yum'
