from os import system

from .get_os import get_os, OS
from .get_packman import get_packman
from .get_argv import get_argv

class GetApps():
    def __call__(self):
        _apps = [
            'make',
            'cmake',
            'gcc',
            'docker',
        ]
        if get_argv().desktop:
            _apps.append('nodejs')
        if get_os() == OS.CENTOS:
            _apps.append('gcc-c++')
        elif get_os() == OS.UBUNTU:
            _apps.append('g++')
        return _apps

get_apps = GetApps()

def prebuild():
    apps = []
    for app in get_apps():
        apps.append(app)
    packman = '{} install'.format(get_packman())
    if get_os() != OS.WIN32:
        packman += ' -y'
    system('{} {}'.format(packman, ' '.join(apps)))
