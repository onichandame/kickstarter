from unittest import TestCase
from unittest.mock import patch, mock_open
from os.path import join
from stat import S_IRWXU

from .get_home import get_home

from .install_keys import KeyUrl as subject1, install_keys as subject2

class TestKeyUrl(TestCase):

    def test_get_username(self):
        username = '!@#$%^asdfwqer'
        with patch('builtins.input', return_value=username) as mock_input:
            url = subject1()()
            self.assertIn(username, url)
            mock_input.assert_called()

    def test_get_username_once(self):
        username = 'poikhjgvjbkl'
        with patch('builtins.input', return_value=username) as mock_input:
            url = subject1()
            for _ in range(100):
                url()
            mock_input.assert_called_once()

    def test_get_username_stripped(self):
        username = '  asgeergfgeeasghtewhethew  '
        with patch('builtins.input', return_value=username):
            url = subject1()()
            self.assertNotIn(username, url)
            self.assertIn(username.strip(), url)

class TestInstallKeys(TestCase):

    @patch(__package__+'.install_keys.get')
    def test_prompt(self, mock_get):
        mock_get.return_value.json.return_value = []
        nos = [
            'no',
            'No',
            'nO',
            'NO',
            'n',
            'N'
        ]
        yess = [
            'yes',
            'Yes',
            'yEs',
            'yeS',
            'YEs',
            'YeS',
            'yES',
            'y',
            'Y'
        ]
        for no in nos:
            with patch('builtins.input', return_value=no):
                self.assertFalse(subject2())
        for yes in yess:
            with patch('builtins.input', return_value=yes):
                self.assertTrue(subject2())

    def test_create_keyfile(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.install_keys.open', mock_open(read_data='')) as mock_file, patch('builtins.input', return_value='yes'), patch(__package__+'.install_keys.exists', return_value=False), patch(__package__+'.install_keys.mkdir') as mock_mkdir:
            mock_get.return_value.json.return_value = []
            key_dir = join(get_home(), '.ssh')
            key_file = join(key_dir, 'authorized_keys')
            subject2()
            mock_mkdir.assert_called_once_with(key_dir)
            mock_file.assert_any_call(key_file, 'w')
            mock_file().write.assert_any_call('')

    def test_read_keys(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.install_keys.open', mock_open(read_data='')) as mock_file, patch('builtins.input', return_value='yes'):
            mock_get.return_value.json.return_value = []
            subject2()
            mock_file.assert_called_once()

    def test_get_key(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.install_keys.open', mock_open(read_data='')) as mock_file, patch('builtins.input', return_value='yes'):
            key = 'jjopijopj98uu9yuio9u8uii'
            mock_get.return_value.json.return_value = [
                {
                    'key': key
                }
            ]
            subject2()
            mock_file().write.assert_called_once_with(key+'\n')

    def test_get_keys(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.install_keys.open', mock_open(read_data='')) as mock_file, patch('builtins.input', return_value='yes'):
            key1 = 'jjopijopj98uu9yuio9u8uii'
            key2 = 'hger4w5983y46098utigefu98itreg'
            mock_get.return_value.json.return_value = [
                {
                    'key': key1
                },
                {
                    'key': key2
                }
            ]
            subject2()
            self.assertEqual(mock_file().write.call_count, 2)
            mock_file().write.assert_any_call(key1+'\n')
            mock_file().write.assert_any_call(key2+'\n')

    def test_chmod(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.install_keys.open', mock_open(read_data='')) as mock_file, patch('builtins.input', return_value='yes'), patch(__package__+'.install_keys.exists', return_value=False), patch(__package__+'.install_keys.mkdir') as mock_mkdir, patch(__package__+'.install_keys.chmod') as mock_chmod:
            mock_get.return_value.json.return_value = []
            key_dir = join(get_home(), '.ssh')
            key_file = join(key_dir, 'authorized_keys')
            subject2()
            self.assertEqual(mock_chmod.call_count, 2)
            mock_chmod.assert_any_call(key_file, S_IRWXU)
            mock_chmod.assert_any_call(key_dir, S_IRWXU)
