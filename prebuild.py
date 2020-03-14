from concurrent.futures import ThreadPoolExecutor
from os import system

from utils.get_os import get_os, OS
from utils.get_packman import get_packman

class GetApps():
    def __call__(self):
        _apps_ = [
            'docker',
            'make',
            'cmake',
            'gcc',
            'docker'
        ]
        if get_os() == OS.CENTOS:
            _apps_.append('gcc-c++')
        elif get_os() == OS.UBUNTU:
            _apps_.append('g++')
        return _apps_

get_apps = GetApps()

def prebuild():
    executable = get_packman()
    for app in get_apps():
        command = ' '.join([
            executable,
            'install',
            app
        ])
        with ThreadPoolExecutor() as executor:
            results = [executor.submit(system, command)]
