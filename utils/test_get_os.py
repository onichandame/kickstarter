from unittest import TestCase
from unittest.mock import patch

from .get_os import get_os as subject, OS

class TestGetOS(TestCase):

    def test_run(self):
        self.assertIn(subject(), OS)

    def test_win(self):
        with patch(__package__+'.get_os.platform', 'win32'):
            self.assertEqual(subject(), OS.WIN32)

    def test_ubuntu(self):
        with patch(__package__+'.get_os.platform', 'linux'), patch(__package__+'.get_os.linux_distribution', return_value=['ubuntu']):
            self.assertEqual(subject(), OS.UBUNTU)

    def test_centos(self):
        with patch(__package__+'.get_os.platform', 'linux'), patch(__package__+'.get_os.linux_distribution', return_value=['centos']):
            self.assertEqual(subject(), OS.CENTOS)

    def test_other_os(self):
        with patch(__package__+'.get_os.platform', '!@#$'):
            self.assertEqual(subject(), OS.UNKNOWN)

    def test_other_linux(self):
        with patch(__package__+'.get_os.platform', 'linux'), patch(__package__+'.get_os.linux_distribution', return_value=['!@#$#%']):
            self.assertEqual(subject(), OS.UNKNOWN)
