from .get_argv import get_argv

from enum import Enum

class Type(Enum):
    SOURCE  = 0
    PACKMAN =1

def apps():
    _apps = [
        {
            'name': 'python3',
            'type': Type.PACKMAN
        }
    ]
    if get_argv().desktop:
        _apps.append({
            'name': 'neovim',
            'type': Type.SOURCE,
            'repo': 'https://github.com/neovim/neovim.git',
            'tag': 'v0.4.3',
            'dependency': [
                {
                    'name': 'ninja-build',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'libtool',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'gettext',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'autoconf',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'automake',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'unzip',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'patch',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'gcc',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'make',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'cmake',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'nodejs',
                    'type': Type.PACKMAN
                },
                {
                    'name': 'python3',
                    'type': Type.PACKMAN
                }
            ]
        })
        if get_os() == OS.CENTOS:
            _apps[0]['dependency'].append({
                'name': 'gcc-c++',
                'type': Type.PACKMAN
            })
        elif get_os() == OS.UBUNTU:
            _apps[0]['dependency'].append({
                'name': 'g++',
                'type': Type.PACKMAN
            })
