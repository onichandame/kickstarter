import os
import shutil

from common.get_os import get_os, OS
from common.get_argv import get_argv

def init_home():
    if get_argv().init:
        bashrc = ''
        vimrc = ''
        if get_os() == OS.WIN32:
            vimrc = os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH'], 'AppData', 'Local', 'nvim', 'init.vim')
        else:
            vimrc = os.path.join(os.environ['HOME'], '.config', 'nvim', 'init.vim')
            bashrc = os.path.join(os.environ['HOME'], '.bashrc')

        if bashrc:
            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'bashrc'), bashrc)
        if vimrc:
            shutil.copyfile(os.path.join(os.path.dirname(__file__), 'init.vim'), vimrc)
