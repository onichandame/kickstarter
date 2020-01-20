from apps import apps
import subprocess
from jobqueue.jobqueue import JobQueue
from common.get_packman import get_packman
from common.get_os import *
from common.terminate import terminate
from common.get_argv import get_argv

def install_apps():
    queue = JobQueue()
    cmd = []
    if get_os() == OS.WIN32:
        cmd=[get_packman(), 'install'] + apps
    else:
        cmd=[get_packman(), 'install', '-y'] + apps
    if queue.run(cmd, stdout=subprocess.PIPE):
        terminate('installation failed')
    if get_argv().desktop:
        print('all done! now set alias for nvim and initiates it by following :h nvim-from-vim. the template configuration file init.vim is in this repo')
