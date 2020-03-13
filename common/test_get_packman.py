from unittest import TestCase
from unittest.mock import patch

from .get_packman import get_packman as subject

def mock_packman(packman):
    def mock_selector(cand):
        if cand == packman:
            return True
        else:
            return False
    return mock_selector


class TestGetPackman(TestCase):

    def test_run(self):
        self.assertEqual(type(subject()), str)

    def test_snap(self):
        target = 'snap'
        with patch('common.get_packman.which', new=mock_packman(target)):
            self.assertIn(target, subject())

    def test_dnf(self):
        target = 'dnf'
        with patch('common.get_packman.which', new=mock_packman(target)):
            self.assertIn(target, subject())

    def test_apt(self):
        target = 'apt'
        with patch('common.get_packman.which', new=mock_packman(target)):
            self.assertIn(target, subject())

    def test_yum(self):
        target = 'yum'
        with patch('common.get_packman.which', new=mock_packman(target)):
            self.assertIn(target, subject())
