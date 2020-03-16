from os import environ, sep
from os.path import join

from .get_os import get_os, OS
from .get_user import get_user

def get_home():
    home = ''
    if get_os() == OS.WIN32:
        home = environ['HOMEDRIVE'] + environ['HOMEPATH']
    else:
        home = join(sep, 'home', 'user')
    home = home.split(sep)
    home[-1] = get_user()
    home = sep.join(home)
    return home
