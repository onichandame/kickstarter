import sys
import argparse
from .static_decorator import static_decorator

@static_decorator(_argv_={})
def get_argv():
    if not get_argv._argv_:
        parser = argparse.ArgumentParser(description = 'testing')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--server', action='store_const', const=Env.SERVER)
        group.add_argument('--desktop', action='store_const', const=Env.DESKTOP)
        get_argv._argv_ = parser.parse_args(sys.argv[1:])
    return get_argv._argv_

from enum import Enum
class Env(Enum):
    UNKNOWN=-1
    SERVER=1
    DESKTOP=2
