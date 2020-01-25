import sys
import argparse
from .static_decorator import static_decorator

@static_decorator(_argv_={})
def get_argv():
    if not get_argv._argv_:
        parser = argparse.ArgumentParser(description = 'mode')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--server', action='store_true')
        group.add_argument('--desktop', action='store_true')
        parser.add_argument('--init', help='overwrite neovim config and bashrc', action='store_true', required=False)
        get_argv._argv_ = parser.parse_args(sys.argv[1:])
    return get_argv._argv_
