from unittest import TestCase
from unittest.mock import patch
from os import sep
from os.path import join

from .get_os import OS
from .randomstring import randomstring

from .get_home import get_home as subject

class TestGetHome(TestCase):

    def test_win(self):
        homedrive = randomstring()
        homepath = sep.join([ randomstring(), randomstring() ])
        user = randomstring()
        home = (homedrive+homepath).split(sep)
        home[-1] = user
        home = sep.join(home)
        with patch(__package__+'.get_home.get_os', return_value=OS.WIN32), patch.dict(__package__+'.get_home.environ', HOMEDRIVE=homedrive, HOMEPATH=homepath), patch(__package__+'.get_home.get_user', return_value=user):
            self.assertEqual(subject(), home)

    def test_linux(self):
        homepath = sep.join([ randomstring(), randomstring() ])
        user = randomstring()
        home = homepath.split(sep)
        home[-1] = user
        home = sep.join(home)
        with patch(__package__+'.get_home.get_os', return_value=OS.CENTOS), patch.dict(__package__+'.get_home.environ', HOME=homepath), patch(__package__+'.get_home.get_user', return_value=user):
            self.assertEqual(subject(), join(sep, 'home', user))
