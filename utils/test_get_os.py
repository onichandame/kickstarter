from unittest import TestCase
from unittest.mock import patch

from .randomstring import randomstring
from .get_os import get_os as subject, OS

class TestGetOS(TestCase):

    def test_run(self):
        self.assertIn(subject(), OS)

    def test_win(self):
        with patch(__package__+'.get_os.platform', 'win32'):
            self.assertEqual(subject(), OS.WIN32)

    def test_linux(self):
        with patch(__package__+'.get_os.platform', 'linux'):
            self.assertEqual(subject(), OS.LINUX)

    def test_other_os(self):
        with patch(__package__+'.get_os.platform', randomstring()):
            self.assertEqual(subject(), OS.UNKNOWN)
