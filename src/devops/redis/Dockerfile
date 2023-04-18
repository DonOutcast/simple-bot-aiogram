FROM redis:7.2-rc1-bullseye

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install git -y \
    && git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim \
    && apt-get install dos2unix \
    && apt-get install -y python3.10 \
#    && apt-get install -y build-essential cmake python3-dev \
#    && cd ~/.vim/bundle/YouCompleteMe \
#    && python3 install.py --clangd-completer \
    && rm -rf /var/lib/apt/lists/* \



COPY .vimrc /root/.vimrc

RUN --mount=type=cache,target=/root/.vim \
    dos2unix /root/.vimrc \
    && vim +PluginInstall +qall
