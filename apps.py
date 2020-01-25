from common.get_os import get_os, OS
from common.get_argv import get_argv

apps = []

if get_argv().desktop:
    apps.append('docker')
    apps.append('make')
    apps.append('cmake')
    apps.append('gcc')
    if get_os() == OS.UBUNTU:
        apps.append('g++')
    elif get_os() == OS.CENTOS:
        apps.append('gcc-c++')
