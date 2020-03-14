from unittest import TestCase
from unittest.mock import patch, mock_open

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

    def test_get_keys(self):
        with patch(__package__+'.install_keys.get') as mock_get, patch(__package__+'.open', mock_open(read_data='')) as m, patch('builtins.input', return_value='yes'):
            key = 'jjopijopj98uu9yuio9u8uii'
            mock_get.return_value.json.return_value = [
                {
                    'key': key
                }
            ]
            subject2()
            m().write.assert_called_once_with(key+'\r\n')
