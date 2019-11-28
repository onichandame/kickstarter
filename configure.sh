PACK_MAN=""
if [ -n "$(command -v apt)" ]
then
  PACK_MAN="apt"
elif [ -n "$(command -v yum)" ]
then
  PACK_MAN="yum"
fi
if [ -z "$PACK_MAN" ]
then
  echo "No package manager was found! make sure python3 and cmake are available on the system!"
  read -n 1 -p "(y/Y)" CHOICE
  if [ "$CHOICE" != "y" ] && [ "$CHOICE" != "Y" ]
  then
    exit 0
  fi
fi
sudo $PACK_MAN install python -y

git submodule update --init --recursive
cd .vim/bundle/YouCompleteMe
git submodule update --init --recursive
./install.py --clang-completer --ts-completer
cd -
rsync -qav --delete .bashrc $HOME/.bashrc
rsync -qav --delete .vimrc $HOME/.vimrc
rsync -qav --delete .vim/ $HOME/.vim
