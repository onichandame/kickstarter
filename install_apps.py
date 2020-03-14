import subprocess

from utils.prebuild import prebuild
from utils.build import build

def install_apps():
    prebuild()
    build()
