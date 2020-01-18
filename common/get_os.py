import sys
from .static_decorator import static_decorator
from .terminate import terminate

from enum import Enum
class OS(Enum):
    UNKNOWN=-1
    WIN32=1
    UBUNTU=2
    CENTOS=2

@static_decorator(_os_='')
def get_os():
    if not get_os._os_:
        os_str=sys.platform
        if 'win32' in os_str:
            get_os._os_=OS.WIN32
        elif 'linux' in os_str:
            import distro
            dist_str = distro.linux_distribution()[0].lower()
            if 'ubuntu' in dist_str:
                get_os._os_ = OS.UBUNTU
            elif 'centos' in dist_str:
                get_os._os_ = OS.CENTOS
            else:
                terminate('current distro {} is not supported!'.format(dist_str))
        else:
            terminate('The current OS is not supported!')
    return get_os._os_
