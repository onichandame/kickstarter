git submodule update --init --recursive
cd .vim/bundle/YouCompleteMe
./install.py --clangd-completer
cd -
cp .bashrc $HOME
cp .vimrc $HOME
cp -r .vim/ $HOME
