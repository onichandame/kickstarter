git submodule update .vim/bundle/YouCompleteMe --depth=1
cd .vim/bundle/YouCompleteMe
git submodule update --recursive --depth=1
./install.py --clangd-completer
cd -
cp .bashrc ..
cp .vimrc ..
cp -r .vim/ ..
