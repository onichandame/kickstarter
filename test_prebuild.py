from unittest import TestCase
from unittest.mock import patch

from prebuild import get_apps
from common.get_os import OS

class TestGetApps(TestCase):

    def test_run(self):
        self.assertTrue(type(get_apps()) == list)

    def test_ubuntu(self):
        with patch('prebuild.get_os', return_value=OS.UBUNTU):
            self.assertIn('g++', get_apps())
            self.assertNotIn('gcc-c++', get_apps())

    def test_centos(self):
        with patch('prebuild.get_os', return_value=OS.CENTOS):
            self.assertIn('gcc-c++', get_apps())
            self.assertNotIn('g++', get_apps())

    def test_win(self):
        with patch('prebuild.get_os', return_value=OS.WIN32):
            self.assertNotIn('gcc-c++', get_apps())
            self.assertNotIn('g++', get_apps())

class TestPrebuild(TestCase):
