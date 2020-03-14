from os import environ

from .get_os import get_os, OS

def get_home():
    if get_os() == OS.WIN32:
        return environ['HOMEDRIVE'] + environ['HOMEPATH']
    else:
        return environ['HOME']
