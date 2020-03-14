from requests import get
from stat import S_IRWXU
from os import path, chmod, mkdir
from os.path import exists, join
from prompter import prompt, yesno

from .get_os import get_os, OS
from .get_home import get_home

class KeyUrl():

    def __init__(self):
        self._username = ''

    def __call__(self):
        if not self.username:
            self.get_username()
        return self.url

    def get_username(self):
        self.username = prompt('Enter your username:', suffix='\r\n > ')

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def url(self):
        return 'https://api.github.com/users/{}/keys'.format(self.username)

def install_keys():
    if not yesno('import SSH keys from Github?', default='yes'):
        return False
    key_dir = join(get_home(), '.ssh')
    key_file = join(key_dir, 'authorized_keys')

    if not exists(key_dir):
        mkdir(key_dir)
    if not exists(key_file):
        with open(key_file, 'w') as f:
            f.write('')
    cur_keys = []
    with open(key_file, 'r') as f:
        cur_keys.append(f.read())

    new_keys = []
    url = KeyUrl()
    got_keys = get(url()).json()
    for key in got_keys:
        if key['key'] not in cur_keys:
            new_keys.append(key['key'])

    if new_keys:
        with open(key_file, 'a') as f:
            for key in new_keys:
                f.write(key+'\n')

    chmod(key_file, S_IRWXU)
    chmod(key_dir, S_IRWXU)
    return True
