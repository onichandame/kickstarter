from unittest import TestCase
from unittest.mock import patch

from install_apps import install_apps as subject

class TestInstallApps(TestCase):

    def test_call_both_methods(self):
        with patch('install_apps.prebuild') as mock_prebuild, patch('install_apps.build') as mock_build:
            subject()
            mock_prebuild.assert_called_once()
            mock_build.assert_called_once()
