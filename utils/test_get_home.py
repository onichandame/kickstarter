from unittest import TestCase
from unittest.mock import patch

from .get_home import get_home as subject
from .get_os import OS

class TestGetHome(TestCase):

    def test_win(self):
        homedrive = 'qwdghfdfgdasgdfagd'
        homepath = 'hgfsdgfafsdgafdsg'
        with patch(__package__+'.get_home.get_os', return_value=OS.WIN32), patch.dict(__package__+'.get_home.environ', HOMEDRIVE=homedrive, HOMEPATH=homepath):
            self.assertEqual(subject(), homedrive + homepath)

    def test_linux(self):
        home = 'ghfdgddfgdegdfegdfsgregdfgdf'
        with patch(__package__+'.get_home.get_os', return_value=OS.CENTOS), patch.dict(__package__+'.get_home.environ', HOME=home):
            self.assertEqual(subject(), home)
