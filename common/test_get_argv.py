from unittest import TestCase
from unittest.mock import patch

from .get_argv import get_argv as subject

class TestGetArgv(TestCase):

    def test_require(self):
        with patch('sys.exit') as mock_exit:
            subject()
            mock_exit.assert_called()

    def test_desktop(self):
        mode = 'desktop'
        with patch('common.get_argv.argv', ['', '--{}'.format(mode)]):
            self.assertTrue(subject().desktop)
            self.assertFalse(subject().server)

    def test_server(self):
        mode = 'server'
        with patch('common.get_argv.argv', ['', '--{}'.format(mode)]):
            self.assertTrue(subject().server)
            self.assertFalse(subject().desktop)

    def test_bashrc(self):
        arg = 'bashrc'
        with patch('common.get_argv.argv', ['', '--desktop', '--{}'.format(arg)]):
            self.assertTrue(subject().bashrc)
            self.assertFalse(subject().vimrc)

    def test_vimrc(self):
        arg = 'vimrc'
        with patch('common.get_argv.argv', ['', '--desktop', '--{}'.format(arg)]):
            self.assertTrue(subject().vimrc)
            self.assertFalse(subject().bashrc)
