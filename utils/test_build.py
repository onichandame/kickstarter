from unittest import TestCase
from unittest.mock import patch
from rstr import rstr
from string import digits, ascii_lowercase, ascii_uppercase
from os import devnull
from os.path import join, dirname

from .build import temp_folder_gen as subject1, BuildJob as subject2

def mock_exists_gen(true=[], false=[], default=False):
    def mock_exists(path):
        if path in true:
            return True
        elif path in false:
            return False
        else:
            return default
    return mock_exists

class TestTempFolderGen(TestCase):

    def test_mkdir(self):
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree:
            temp_folder = subject1()
            mock_mkdir.assert_called_once_with(subject1._root_)
        with patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree:
            temp_folder = subject1()
            mock_mkdir.assert_not_called()

    def test_reset(self):
        with patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree:
            temp_folder = subject1.reset()
            mock_rmtree.assert_called_once_with(subject1._root_)
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree:
            temp_folder = subject1.reset()
            mock_rmtree.assert_not_called()

    def test_new_subdir(self):
        subdir = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            new_subdir = subject1()
            self.assertEqual(new_subdir, join(subject1._root_, subdir))

    def test_raise_on_duplicate_subdir(self):
        subdir = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            new_subdir = subject1()
            with self.assertRaises(Exception):
                subject1()

    def test_raise_on_existing_subdir(self):
        subdir = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], true=[join(dirname(__file__), subject1._root_, subdir)], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            with self.assertRaises(Exception):
                subject1()

class TestBuildJob(TestCase):

    def test_mkdir(self):
        subdir_name = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir_name), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild:
            job = subject2('', '')
            mock_mkdir.assert_called_with(subdir)
            self.assertEqual(job.src_dir, join(subdir, 'src'))

    def test_called_all_steps(self):
        subdir_name = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir_name), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild:
            subject2('', '')
            mock_download.assert_called_once()
            mock_configure.assert_called_once()
            mock_build.assert_called_once()
            mock_postbuild.assert_called_once()

    def test_download(self):
        subdir_name = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        name = rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        config = {
            'repo': rstr(digits+ascii_lowercase+ascii_uppercase, 10),
            'tag': rstr(digits+ascii_lowercase+ascii_uppercase, 10)
        }
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir_name), patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild, patch(__package__+'.build.Repo') as mock_repo:
            subject2(name, config)
            mock_repo.clone_from.assert_called_once()
