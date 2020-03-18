from unittest import TestCase
from unittest.mock import patch, Mock
from os import devnull
from os.path import join, dirname
from subprocess import DEVNULL

from .apps import Type
from .randomstring import randomstring

from .build import temp_folder_gen as subject1, BuildJob as subject2, build as subject3

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
        subdir = randomstring()
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            new_subdir = subject1()
            self.assertEqual(new_subdir, join(subject1._root_, subdir))

    def test_raise_on_duplicate_subdir(self):
        subdir = randomstring()
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            new_subdir = subject1()
            with self.assertRaises(Exception):
                subject1()

    def test_raise_on_existing_subdir(self):
        subdir = randomstring()
        with patch(__package__+'.build.exists', new=mock_exists_gen(false=[subject1._root_], true=[join(dirname(__file__), subject1._root_, subdir)], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.rstr', return_value=subdir):
            with self.assertRaises(Exception):
                subject1()

class TestBuildJob(TestCase):

    def test_mkdir(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild:
            job = subject2('', '')
            mock_mkdir.assert_called_with(subdir)
            self.assertEqual(job.src_dir, join(subdir, 'src'))

    def test_called_all_steps(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild:
            subject2('', '')
            mock_download.assert_called_once()
            mock_configure.assert_called_once()
            mock_build.assert_called_once()
            mock_postbuild.assert_called_once()

    def test_reset(self):
        desc = randomstring()
        total = 1
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild:
            job = subject2('', '')
            job.reset(desc, total)
            self.assertIn(desc, job.progressbar.desc)
            self.assertEqual(job.progressbar.total, total)

    def test_download(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        name = randomstring()
        config = {
            'repo': randomstring(),
            'tag': randomstring()
        }
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild, patch(__package__+'.build.Repo') as mock_repo:
            job = subject2(name, config)
            self.assertIn('downloading {}'.format(name), job.progressbar.desc)
            mock_repo.clone_from.assert_called_once()

    def test_configure(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        name = randomstring()
        config = {
            'configure': '{} {}'.format(randomstring(), randomstring())
        }
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'build') as mock_build, patch.object(subject2, 'postbuild') as mock_postbuild, patch(__package__+'.build.check_call') as mock_popen:
            mock_popen.return_value.wait.return_value = 0
            job1 = subject2(name, config)
            mock_popen.assert_called_once_with(config['configure'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=job1.src_dir)
            self.assertIn('configuring {}'.format(name), job1.progressbar.desc)
            mock_popen.side_effect = lambda: Exception()
            with self.assertRaises(Exception):
                subject2(name, config)

    def test_build(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        name = randomstring()
        config = {
            'build': '{} {}'.format(randomstring(), randomstring())
        }
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'postbuild') as mock_postbuild, patch(__package__+'.build.check_call') as mock_popen:
            mock_popen.return_value.wait.return_value = 0
            job1 = subject2(name, config)
            mock_popen.assert_called_once_with(config['build'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=job1.src_dir)
            mock_popen.side_effect = lambda: Exception()
            with self.assertRaises(Exception):
                subject2(name, config)

    def test_postbuild(self):
        subdir_name = randomstring()
        subdir = join(dirname(__file__), subject1._root_, subdir_name)
        name = randomstring()
        config = {
            'postbuild': '{} {}'.format(randomstring(), randomstring())
        }
        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.exists', new=mock_exists_gen(true=[subject1._root_], false=[subdir], default=False)), patch(__package__+'.build.mkdir') as mock_mkdir, patch(__package__+'.build.rmtree') as mock_rmtree, patch(__package__+'.build.temp_folder_gen', return_value=subdir), patch.object(subject2, 'download') as mock_download, patch.object(subject2, 'configure') as mock_configure, patch.object(subject2, 'build') as mock_build, patch(__package__+'.build.check_call') as mock_popen:
            mock_popen.return_value.wait.return_value = 0
            job1 = subject2(name, config)
            mock_popen.assert_called_once_with(config['postbuild'].split(), stdout=DEVNULL, stderr=DEVNULL, cwd=job1.src_dir)
            mock_popen.side_effect = lambda: Exception()
            with self.assertRaises(Exception):
                subject2(name, config)

class TestBuild(TestCase):

    def test_reset(self):
        with patch(__package__+'.build.temp_folder_gen.reset') as mock_reset:
            subject3(runner_function=lambda: '')
            mock_reset.assert_called_once()

    def test_runner(self):
        apps = {
            randomstring(): {
                'type': Type.SOURCE
            }
        }

        with open(devnull, 'w') as mock_devnull, patch('sys.stdout', mock_devnull), patch('sys.stderr', mock_devnull), patch(__package__+'.build.ThreadPoolExecutor.submit') as mock_submit, patch(__package__+'.build.apps') as mock_apps, patch(__package__+'.build.as_completed', return_value=[]):

            mock_apps.return_value = {
                randomstring(): {
                    'type': Type.PACKMAN
                }
            }
            subject3(reset_function=lambda: '')
            mock_submit.assert_not_called()

            mock_apps.return_value = apps
            subject3(reset_function=lambda: '')
            mock_submit.assert_called_with(subject2, list(apps.keys())[0], list(apps.values())[0])
