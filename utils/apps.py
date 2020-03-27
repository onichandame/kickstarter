from .get_argv import get_argv

from enum import Enum

class Type(Enum):
    SOURCE  = 0
    PACKMAN =1

deps = {
    'g++': {
        'default': 'g++',
        'dnf': 'gcc-g++',
        'yum': 'gcc-g++'
    },
    'ninja-build': {
        'default': 'ninja-build'
    },
    'libtool': {
        'default': 'libtool'
    },
    'gettext': {
        'default': 'gettext'
    },
    'autoconf': {
        'default': 'autoconf'
    },
    'automake': {
        'default': 'automake'
    },
    'unzip': {
        'default': 'unzip'
    },
    'patch': {
        'default': 'patch'
    },
    'gcc': {
        'default': 'gcc'
    },
    'make': {
        'default': 'make'
    },
    'cmake': {
        'default': 'cmake'
    },
    'nodejs': {
        'default': 'nodejs'
    },
    'python3': {
        'default': 'python3'
    }
}

def apps():
    _apps = {}
    if get_argv().desktop:
        _apps['neovim'] = {
            'type': Type.SOURCE,
            'repo': 'https://github.com/neovim/neovim.git',
            'tag': 'v0.4.3',
            'dependency': {
                'ninja-build': deps['ninja-build'],
                'libtool': deps['libtool'],
                'gettext': deps['libtool'],
                'autoconf': deps['autoconf'],
                'automake': deps['automake'],
                'unzip': deps['unzip'],
                'patch': deps['patch'],
                'gcc': deps['gcc'],
                'g++': deps['g++'],
                'make': deps['make'],
                'cmake': deps['cmake'],
                'nodejs': deps['nodejs'],
                'python3': deps['python3']
            },
            # 'build': 'make CMAKE_BUILD_TYPE=Release', # failed downloading luarocks. switch back when fixed
            'build': 'make',
            'postbuild': 'make install'
        }
    return _apps
