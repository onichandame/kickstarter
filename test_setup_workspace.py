from unittest import TestCase
from unittest.mock import patch

from setup_workspace import setup_workspace as subject

class TestSetupWorkspace(TestCase):

    def test_call_both_methods(self):
        with patch('setup_workspace.init_config') as mock_config, patch('setup_workspace.install_keys') as mock_keys:
            subject()
            mock_config.assert_called_once()
            mock_keys.assert_called_once()
