from apps import apps
import subprocess
from jobqueue.jobqueue import JobQueue
from common.get_packman import get_packman
from common.get_os import *
from common.terminate import terminate

def install_apps():
    queue = JobQueue()
    cmd = []
    if get_os() == OS.WIN32:
        cmd=[get_packman(), 'install'] + apps
    else:
        cmd=[get_packman(), 'install', '-y'] + apps
    print(cmd)
    if queue.run(cmd, stdout=subprocess.PIPE):
        terminate('installation failed!')
