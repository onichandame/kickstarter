from .get_argv import get_argv
from .get_os import get_os, OS

from enum import Enum

class Type(Enum):
    SOURCE  = 0
    PACKMAN =1

def apps():
    _apps = {
        'python3': {
            'type': Type.PACKMAN
        }
    }
    if get_argv().desktop:
        _apps['neovim'] = {
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
            ],
            # 'build': 'make CMAKE_BUILD_TYPE=Release', # failed downloading luarocks. switch back when fixed
            'build': 'make',
            'postbuild': 'make install'
        }
        if get_os() == OS.CENTOS:
            _apps['neovim']['dependency'].append({
                'name': 'gcc-c++',
                'type': Type.PACKMAN
            })
        elif get_os() == OS.UBUNTU:
            _apps['neovim']['dependency'].append({
                'name': 'g++',
                'type': Type.PACKMAN
            })
    return _apps
