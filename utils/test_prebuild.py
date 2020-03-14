from unittest import TestCase
from unittest.mock import patch

from .prebuild import get_apps as subject1, prebuild as subject2
from .get_os import OS

class TestGetApps(TestCase):

    def test_run(self):
        self.assertTrue(type(subject1()) == list)

    def test_common(self):
        with patch(__package__+'.prebuild.get_os', return_value=OS.UBUNTU):
            self.assertIn('make', subject1())
            self.assertIn('cmake', subject1())
            self.assertIn('gcc', subject1())
            self.assertIn('docker', subject1())
        with patch(__package__+'.prebuild.get_os', return_value=OS.CENTOS):
            self.assertIn('make', subject1())
            self.assertIn('cmake', subject1())
            self.assertIn('gcc', subject1())
            self.assertIn('docker', subject1())
        with patch(__package__+'.prebuild.get_os', return_value=OS.WIN32):
            self.assertIn('make', subject1())
            self.assertIn('cmake', subject1())
            self.assertIn('gcc', subject1())
            self.assertIn('docker', subject1())

    def test_gxx(self):
        with patch(__package__+'.prebuild.get_os', return_value=OS.UBUNTU):
            self.assertIn('g++', subject1())
            self.assertNotIn('gcc-c++', subject1())
        with patch(__package__+'.prebuild.get_os', return_value=OS.CENTOS):
            self.assertIn('gcc-c++', subject1())
            self.assertNotIn('g++', subject1())
        with patch(__package__+'.prebuild.get_os', return_value=OS.WIN32):
            self.assertNotIn('gcc-c++', subject1())
            self.assertNotIn('g++', subject1())

class TestPrebuild(TestCase):

    def test_call_system(self):
        with patch(__package__+'.prebuild.get_packman', return_value='qwegfdbv'), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.CENTOS):
            subject2()
            mock_system.assert_called_once()

    def test_call_with_packman(self):
        packman = 'qwergfdsdewergff'
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.CENTOS):
            subject2()
            mock_system.assert_called_once_with(packman+' install -y ')
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.UBUNTU):
            subject2()
            mock_system.assert_called_once_with(packman+' install -y ')
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.WIN32):
            subject2()
            mock_system.assert_called_once_with(packman+' install ')

    def test_call_with_apps(self):
        packman = 'qwergfdsdewergff'
        apps = ['asdfdsfa', 'ghrgednrgesbfr']
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=apps), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.CENTOS):
            subject2()
            mock_system.assert_called_once_with(packman+' install -y '+' '.join(apps))
