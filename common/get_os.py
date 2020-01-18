import sys
from .static_decorator import static_decorator
from .terminate import terminate

from enum import Enum
class OS(Enum):
    UNKNOWN=-1
    WIN32=1
    LINUX=2

@static_decorator(_os_='')
def get_os():
    if not get_os._os_:
        os_str=sys.platform
        if 'win32' in os_str:
            get_os._os_=OS.WIN32
        elif 'linux' in os_str:
            get_os._os_=OS.LINUX
        else:
            terminate('The current OS is not supported!')
    return get_os._os_
