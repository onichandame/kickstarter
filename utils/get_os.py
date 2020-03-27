from sys import platform
from .terminate import terminate

from enum import Enum

class OS(Enum):
    UNKNOWN = 0
    WIN32   = 1
    LINUX   = 2

def get_os():
    _os_ = OS.UNKNOWN
    os_str = platform
    if 'win32' in os_str:
        _os_= OS.WIN32
    elif 'linux' in os_str:
        _os_ = OS.LINUX
    return _os_
