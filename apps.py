from common.get_os import get_os, OS
from common.get_argv import get_argv

apps = []

if get_os == OS.WIN32:
    apps.append('docker')
    if get_argv().desktop:
        apps.append('gcc')
        apps.append('make')
        apps.append('cmake')
        apps.append('neovim')
else:
    apps.append('docker')
    if get_argv().desktop:
        apps.append('gcc')
        if get_os == OS.UBUNTU:
            apps.append('g++')
        elif get_os == OS.CENTOS:
            apps.append('gcc-c++')
        apps.append('make')
        apps.append('cmake')
        apps.append('neovim')
