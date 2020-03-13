from sys import platform
from .terminate import terminate
from distro import linux_distribution

from enum import Enum

class OS(Enum):
    UNKNOWN = 0
    WIN32   = 1
    UBUNTU  = 2
    CENTOS  = 3

class GetOS():

    def __call__(self, *args, **kwargs):
        _os_ = OS.UNKNOWN
        os_str = platform
        if 'win32' in os_str:
            _os_= OS.WIN32
        elif 'linux' in os_str:
            dist_str = linux_distribution()[0].lower()
            if 'ubuntu' in dist_str:
                _os_ = OS.UBUNTU
            elif 'centos' in dist_str:
                _os_ = OS.CENTOS
        return _os_

get_os = GetOS()
