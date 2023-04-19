set nocompatible              " отключить режим совместимости
filetype off                  " отключить определение типа файла

" Настройки плагинов Vundle
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Добавьте плагины здесь, например:
Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle'}
Plugin 'Vimjas/vim-python-pep8-indent'
Plugin 'dense-analysis/ale'
Plugin 'tpope/vim-commentary'
Plugin 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }
call vundle#end()
filetype plugin indent on    " включить поддержку плагинов

" Настройки отображения
set number                     " показать номера строк
set tabstop=4                  " ширина табуляции
set expandtab                  " использовать пробелы вместо табуляции
set softtabstop=4              " количество пробелов на табуляцию
set shiftwidth=4               " количество пробелов на отступ
set smarttab                   " умный таб
set showmatch                  " выделение парных скобок

" Настройки для Python
autocmd FileType python setlocal expandtab tabstop=4 softtabstop=4 shiftwidth=4

" Настройки цветовой схемы
syntax enable
set background=dark
colorscheme desert


set encoding=utf-8
set fileencoding=utf-8
set termencoding=utf-8

noremap <C-l> :bn<CR>
noremap <C-h> :bp<CR>

map <C-n> :NERDTreeToggle<CR>