import subprocess

from .prebuild import prebuild
from .build import build

def install_apps():
    prebuild()
    build()
