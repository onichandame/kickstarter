from unittest import TestCase
from unittest.mock import patch

from .get_os import OS
from .apps import Type

from .prebuild import get_apps as subject1, prebuild as subject2

class TestGetApps(TestCase):

    def test_return_type(self):
        with patch(__package__+'.apps.get_argv') as mock_argv:
            mock_argv.return_value.desktop = True
            apps = subject1()
            self.assertTrue(type(apps) == list)
            for app in apps:
                self.assertEqual(type(app), str)

    def test_get_packman(self):
        with patch(__package__+'.prebuild.apps') as mock_apps:
            mock_apps.return_value = {
                'app1': {
                    'type': Type.PACKMAN
                },
                'app2': {
                    'type': Type.PACKMAN
                },
                'app3': {
                    'type': Type.SOURCE
                }
            }
            apps = subject1()
            self.assertEqual(len(apps), 2)
            self.assertIn('app1', apps)
            self.assertIn('app2', apps)
            self.assertNotIn('app3', apps)

    def test_get_deps(self):
        with patch(__package__+'.prebuild.apps') as mock_apps:
            mock_apps.return_value = {
                'app1': {
                    'type': Type.SOURCE,
                    'dependency': {
                        'app3': {},
                        'app4': {}
                    }
                },
                'app2': {
                    'type': Type.SOURCE,
                    'dependency': {
                        'app1': {},
                        'app2': {}
                    }
                }
            }
            apps = subject1()
            self.assertEqual(len(apps), 4)
            self.assertIn('app1', apps)
            self.assertIn('app2', apps)
            self.assertIn('app3', apps)
            self.assertIn('app4', apps)

    def test_remove_duplicate(self):
        with patch(__package__+'.prebuild.apps') as mock_apps:
            mock_apps.return_value = {
                'app1': {
                    'type': Type.PACKMAN
                },
                'app2': {
                    'type': Type.SOURCE,
                    'dependency': {
                        'app1': {}
                    }
                }
            }
            apps = subject1()
            self.assertEqual(len(apps), 1)
            self.assertIn('app1', apps)

class TestPrebuild(TestCase):

    def test_call_system(self):
        with patch(__package__+'.prebuild.get_packman', return_value='qwegfdbv'), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.LINUX):
            subject2()
            mock_system.assert_called_once()

    def test_call_with_packman(self):
        packman = 'qwergfdsdewergff'
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.LINUX):
            subject2()
            mock_system.assert_called_once_with(packman+' install -y ')
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=[]), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.WIN32):
            subject2()
            mock_system.assert_called_once_with(packman+' install ')

    def test_call_with_apps(self):
        packman = 'qwergfdsdewergff'
        apps = ['asdfdsfa', 'ghrgednrgesbfr']
        with patch(__package__+'.prebuild.get_packman', return_value=packman), patch(__package__+'.prebuild.get_apps', return_value=apps), patch(__package__+'.prebuild.system') as mock_system, patch(__package__+'.prebuild.get_os', return_value=OS.LINUX):
            subject2()
            mock_system.assert_called_once_with(packman+' install -y '+' '.join(apps))
