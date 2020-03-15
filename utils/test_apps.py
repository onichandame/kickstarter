from unittest import TestCase
from unittest.mock import patch

from .apps import apps as subject, Type

class TestApps(TestCase):

    def test_return_type(self):
        with patch(__package__+'.apps.get_argv') as mock_argv:
            mock_argv.return_value.desktop = True
            apps = subject()
            self.assertEqual(type(apps), dict)
            for app in apps.values():
                self.assertIn('type', app)
                self.assertIn(app['type'], Type)
                if 'dependency' in app:
                    for dep in app['dependency']:
                        self.assertIn('name', dep)
                if app['type'] == Type.SOURCE:
                    self.assertIn('build', app)
        with patch(__package__+'.apps.get_argv') as mock_argv:
            mock_argv.return_value.desktop = False
            apps = subject()
            self.assertEqual(type(apps), dict)
            for app in apps.values():
                self.assertIn('type', app)
                self.assertIn(app['type'], Type)
                if 'dependency' in app:
                    for dep in app['dependency']:
                        self.assertIn('name', dep)
                if app['type'] == Type.SOURCE:
                    self.assertIn('build', app)
