from os import system

from .get_os import get_os, OS
from .get_packman import get_packman
from .apps import apps, Type

def get_apps():
    _apps = []
    for name, app in apps().items():
        if app['type'] == Type.PACKMAN:
            _apps.append(name)
        if app['type'] == Type.SOURCE and 'dependency' in app:
            for dep in app['dependency'].keys():
                _apps.append(dep)
    return list(dict.fromkeys(_apps))

def prebuild():
    apps = []
    for app in get_apps():
        apps.append(app)
    packman = '{} install'.format(get_packman())
    if get_os() != OS.WIN32:
        packman += ' -y'
    system('{} {}'.format(packman, ' '.join(apps)))
