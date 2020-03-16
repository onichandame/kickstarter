from os import environ

def get_user():
    if 'SUDO_USER' in environ:
        return environ['SUDO_USER']
    return environ['USER']
