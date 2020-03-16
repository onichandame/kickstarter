from unittest import TestCase
from unittest.mock import patch

from .randomstring import randomstring as subject

class TestRandomstring(TestCase):

    def test_return_type(self):
        self.assertEqual(type(subject()), str)

    def test_random(self):
        rstr1 = subject()
        rstr2 = subject()
        self.assertNotEqual(rstr1, rstr2)
