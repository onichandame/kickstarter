from unittest import TestCase
from unittest.mock import patch
from rstr import rstr
from string import ascii_lowercase, digits, ascii_uppercase

from .get_user import get_user as subject

def randomstring():
    return rstr(digits+ascii_lowercase+ascii_uppercase, 10)

class TestGetUser(TestCase):

    def test_get_user(self):
        environ = {
            'SUDO_USER': randomstring(),
            'USER': randomstring()
        }
        with patch(__package__+'.get_user.environ', environ):
            self.assertEqual(subject(), environ['SUDO_USER'])

        del environ['SUDO_USER']
        with patch(__package__+'.get_user.environ', environ):
            self.assertEqual(subject(), environ['USER'])
