from sys import argv
from argparse import ArgumentParser

class GetArgv():

    def __init__(self):
        self._argv_ = []

    def __call__(self):
        parser = ArgumentParser(description='A tool for kicking-start you Linux!')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--server', action='store_true')
        group.add_argument('--desktop', action='store_true')
        parser.add_argument('--bashrc', help='overwrite bashrc', action='store_true', required=False)
        parser.add_argument('--vimrc', help='overwrite neovom config', action='store_true', required=False)
        self._argv_ = parser.parse_args(argv[1:])
        return self._argv_

get_argv = GetArgv()
