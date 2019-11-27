git submodule update --init --recursive
cd .vim/bundle/YouCompleteMe
git submodule update --init --recursive
./install.py --clang-completer --ts-completer
cd -
rsync -av --delete .bashrc $HOME/.bashrc
rsync -av --delete .vimrc $HOME/.vimrc
rsync -av --delete .vim/ $HOME/.vim
