PACK_MAN=""
PACKAGES="vim python3 cmake gcc make nodejs"
if [ -n "$(command -v apt)" ]
then
  PACK_MAN="apt"
  PACKAGES=$PACKAGES:" python3-dev g++"
elif [ -n "$(command -v yum)" ]
then
  curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
  PACKAGES=$PACKAGES" python3-devel gcc-c++"
  PACK_MAN="yum"
fi
echo $PACKAGES
if [ -z "$PACK_MAN" ]
then
  echo "No package manager was found! make sure python3 and cmake are available on the system!"
  read -n 1 -p "(y/Y)" CHOICE
  if [ "$CHOICE" != "y" ] && [ "$CHOICE" != "Y" ]
  then
    exit 0
  fi
fi
sudo $PACK_MAN install $PACKAGES -y
VI="$(which vi)"
VIM="$(which vim)"
if [ -n $VI ]
then
  sudo rm $VI
else
  VI="/usr/bin/vi"
fi
if [ -z $VIM ]
then
  VIM="/usr/bin/vim"
fi
sudo ln -s $VIM $VI

git submodule update --init --recursive
cd .vim/bundle/YouCompleteMe
git submodule update --init --recursive
python3 install.py --clang-completer --ts-completer
cd -
rsync -qav --delete .bashrc $HOME/.bashrc
rsync -qav --delete .vimrc $HOME/.vimrc
rsync -qav --delete .vim/ $HOME/.vim
