from unittest import TestCase
from unittest.mock import patch
from os.path import join, dirname
from stat import S_IRWXU, S_IRWXG, S_IRWXO

from .get_home import get_home
from .get_os import OS

from .init_config import init_bashrc as subject1, init_vimrc as subject2, init_config as subject3

class TestInitBashrc(TestCase):

    def test_only_run_on_linux(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.WIN32), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = True
            self.assertFalse(subject1())
            mock_copyfile.assert_not_called()
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = True
            self.assertTrue(subject1())
            mock_copyfile.assert_called_once()

    def test_only_run_when_specified(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = True
            self.assertTrue(subject1())
            mock_copyfile.assert_called_once()

        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = False
            self.assertFalse(subject1())
            mock_copyfile.assert_not_called()

    def test_called_copyfile(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = True
            self.assertTrue(subject1())
            mock_copyfile.assert_called_once_with(join(dirname(__file__), 'bashrc'), join(get_home(), '.bashrc'))

    def test_called_chmod(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.bashrc = True
            self.assertTrue(subject1())
            mock_chmod.assert_called_once_with(join(get_home(), '.bashrc'), S_IRWXU | S_IRWXG | S_IRWXO)

class TestInitVimrc(TestCase):

    def test_only_run_when_specified(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.exists', return_value=True), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            self.assertTrue(subject2())
            mock_copyfile.assert_called_once()

        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.exists', return_value=True), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = False
            self.assertFalse(subject2())
            mock_copyfile.assert_not_called()

    def test_call_mkdir_when_dir_not_found(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.WIN32), patch(__package__+'.init_config.exists', return_value=True), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_mkdir.assert_not_called()
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.WIN32), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_mkdir.assert_called_once_with(join(get_home(), 'AppData', 'Local', 'nvim'))
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_mkdir.assert_called_once_with(join(get_home(), '.config', 'nvim'))

    def test_call_copyfile(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_copyfile.assert_called_once_with(join(dirname(__file__), 'vimrc'), join(get_home(), '.config', 'nvim', 'init.vim'))
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.WIN32), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_copyfile.assert_called_once_with(join(dirname(__file__), 'vimrc'), join(get_home(), 'AppData', 'Local', 'nvim', 'init.vim'))

    def test_call_chmod(self):
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.CENTOS), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_chmod.assert_called_once_with(join(get_home(), '.config', 'nvim', 'init.vim'), S_IRWXU | S_IRWXG | S_IRWXO)
        with patch(__package__+'.init_config.get_argv') as mock_argv, patch(__package__+'.init_config.copyfile') as mock_copyfile, patch(__package__+'.init_config.get_os', return_value=OS.WIN32), patch(__package__+'.init_config.exists', return_value=False), patch(__package__+'.init_config.mkdir') as mock_mkdir, patch(__package__+'.init_config.chmod') as mock_chmod:
            mock_argv.return_value.vimrc = True
            subject2()
            mock_chmod.assert_called_once_with(join(get_home(), 'AppData', 'Local', 'nvim', 'init.vim'), S_IRWXU | S_IRWXG | S_IRWXO)

class TestInitConfig(TestCase):

    def test_run_both_methods(self):
        with patch(__package__+'.init_config.init_bashrc') as mock_bashrc, patch(__package__+'.init_config.init_vimrc') as mock_vimrc:
            subject3()
            mock_bashrc.assert_called_once()
            mock_vimrc.assert_called_once()
