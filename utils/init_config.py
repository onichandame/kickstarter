from os import mkdir
from os.path import join, dirname, exists
from shutil import copyfile

from .get_os import get_os, OS
from .get_argv import get_argv
from .get_home import get_home

def init_bashrc():
    if get_os() != OS.WIN32 and get_argv().bashrc:
        bashrc = join(get_home(), '.bashrc')
        copyfile(join(dirname(__file__), 'bashrc'), bashrc)
        return True
    return False

def init_vimrc():
    if get_argv().vimrc:
        vimrc_dir = ''
        vimrc = ''
        if get_os() == OS.WIN32:
            vimrc_dir = join(get_home(), 'AppData', 'Local', 'nvim')
        else:
            vimrc_dir = join(get_home(), '.config', 'nvim')
        if not exists(vimrc_dir):
            mkdir(vimrc_dir)
        vimrc = join(vimrc_dir, 'init.vim')
        copyfile(join(dirname(__file__), 'init.vim'), vimrc)
        return True
    return False

def init_config():
    init_bashrc()
    init_vimrc()
