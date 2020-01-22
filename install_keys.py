import requests
import os, stat

from common.get_os import get_os, OS

url = 'https://api.github.com/users/onichandame/keys'
response = requests.get(url)

def install_keys():
    home = ''
    if get_os() == OS.WIN32:
        home = os.environ['HOMEDRIVE']+os.environ['HOMEPATH']
    else:
        home = os.environ['HOME']
    key_dir = os.path.join(home, '.ssh')
    key_file = os.path.join(key_dir, 'authorized_keys')

    if not os.path.exists(key_dir):
        os.mkdir(key_dir)
    if not os.path.exists(key_file):
        with open(key_file, 'w') as f:
            f.write('')
    cur_keys = ''
    with open(key_file, 'r') as f:
        cur_keys = f.read()

    new_keys = []
    for key in response.json():
        if key['key'] not in cur_keys:
            new_keys.append(key['key'])

    with open(key_file, 'a') as f:
        for key in new_keys:
            f.write(key+'\r\n')

    os.chmod(key_file, stat.S_IRWXU)
    os.chmod(key_dir, stat.S_IRWXU)
