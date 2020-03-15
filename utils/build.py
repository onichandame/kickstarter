from rstr import rstr
from string import digits, ascii_lowercase, ascii_uppercase
from os import mkdir
from os.path import join, dirname, exists
from subprocess import Popen, DEVNULL
from shutil import rmtree
from concurrent.futures import ThreadPoolExecutor, as_completed
from git import Repo
from tqdm import tqdm
from enum import Enum

from .terminate import terminate

from .apps import apps, Type

class TempFolder():

    _root_ = join(dirname(__file__), '_temp_')
    _subdirs_ = []

    def __call__(self):
        self.add_new_subdir()
        if not exists(self._root_):
            mkdir(self._root_)
        sub_dir = join(self._root_, self._subdirs_[-1])
        if exists(sub_dir):
            raise Exception('temp folder not reset. Remove {} manually and retry'.format(self._root_))
        return sub_dir

    def reset(self):
        if exists(self._root_):
            rmtree(self._root_)

    def add_new_subdir(self):
        max_retries = 5
        retry_count = 0
        while True:
            retry_count += 1
            if retry_count > max_retries:
                raise Exception('cannot generate an unused subdir. check if random is working as expected')
            new_subdir = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
            if new_subdir not in self._subdirs_:
                self._subdirs_.append(new_subdir)
                break

temp_folder_gen = TempFolder()

class BuildJob(tqdm):

    def __init__(self, name, config):
        self.stages = {
            'download': {
                'desc': 'downloading {}'.format(name)
            },
            'configure': {
                'desc': 'configuring {}'.format(name)
            },
            'build': {
                'desc': 'building {}'.format(name)
            },
            'postbuild': {
                'desc': 'running post-build task of {}'.format(name)
            }
        }
        self.name = name
        self.config = config
        self.root_dir = temp_folder_gen()
        self.src_dir = join(self.root_dir, 'src')
        self.executable = ''
        self.config_script = ''
        self.build_script = ''
        self.postbuild_script = ''
        self.progressbar = tqdm(desc='', total=1)

        mkdir(self.root_dir)
        self.download()
        self.configure()
        self.build()
        self.postbuild()
        self.progressbar.close()

    def download(self):
        def update_progress(self, code, cur, tot, message):
            self.progressbar.total = tot
            self.progressbar.n = cur
            self.progressbar.update(0)
        self.progressbar.desc = self.stages['download']['desc']
        repo = Repo.clone_from(self.config['repo'], self.src_dir, progress=update_progress, multi_options=[
            '-b {}'.format(self.config['tag']),
            '--depth=1'
        ])

    def configure(self):
        self.progressbar.desc = self.stages['configure']['desc']
        self.progressbar.total = 1
        self.progressbar.n = 0
        if 'configure' in self.config:
            if Popen(config['configure'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=self.src_dir).wait():
                raise Exception('{} failed configuring'.format(self.name))
        self.progressbar.n = 1

    def build(self):
        self.progressbar.desc = self.stages['build']['desc']
        self.progressbar.total = 1
        self.progressbar.n = 0
        if 'build' in self.config:
            if Popen(config['build'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=self.src_dir).wait():
                raise Exception('{} failed building'.format(self.name))
        self.progressbar.n = 1

    def postbuild(self):
        self.progressbar.desc = self.stages['postbuild']['desc']
        self.progressbar.total = 1
        self.progressbar.n = 0
        if 'postbuild' in self.config:
            if Popen(config['postbuild'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=self.src_dir).wait():
                raise Exception('{} failed post-build script'.format(self.name))
        self.progressbar.n = 1

def build():
    def get_itrs():
        names = []
        configs = []
        for name, config in apps().items():
            names.append(name)
            configs.append(config)
        return [names, configs]

    temp_folder_gen.reset()
    with ThreadPoolExecutor() as executor:
        jobs = executor.map(BuildJob, *get_itrs())
        for job in jobs:
            try:
                job.result()
            except Exception as e:
                terminate('build job failed. see above for details')
