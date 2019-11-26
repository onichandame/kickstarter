set number
set autoindent
set cindent
set expandtab
set cpoptions+=$
set hlsearch
set wildmenu
set tabstop=1
set shiftwidth=2
set ic
set mouse=c
set splitbelow
set splitright
set foldmethod=indent

" Tab settings for individual filetypes
"function! Tabglobal(numspaces)
"  let &tabstop=a:numspaces
"  let &shiftwidth=a:numspaces
"endfunction

"function! Tablocal(numspaces)
"  let &l:tabstop=a:numspaces
"  let &l:shiftwidth=a:numspaces
"endfunction

" Shortcut to kill highlighted search
"map <F9> /Hello Sam. <CR>

" Set a new leader
let mapleader = ","

" quick save and nav shortcuts
nmap <leader>w :w<CR>
map [ <C-U>
map ] <C-D>
map <BS> i<BS>
imap <C-v> <Esc>l<C-v>
map t y$

" Window & tab Shortcuts
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l
vmap <C-f> :fold<CR>
vmap <Space> I<Space>
map <leader>tn :tabnext<CR>
map <leader>tp :tabprevious<CR>
map <leader>to :tabnew<Space>
map a whi

" Cunning pal to paste consecutive numbers in column
map + yljphx<Esc>h<C-A>
 
" Kill things for laptop
"imap <PageUp> <nop>
"imap <PageDown> <nop>
"imap <Home> <nop>
"imap <End> <nop>


" Pressing ,ss will toggle and untoggle spell checking
" and ,p toggles pastemode
map <leader>ss :setlocal spell!<cr>
map <leader>p :setlocal paste!<CR>:setlocal number!<CR>
map <leader>m :set mouse=a<CR>
map <leader>n :set mouse=<CR>


" make txt different colour 80->85 chars
"highlight rightMargin ctermfg=magenta 
"match rightmargin /\%<85v.\%>80v/

" proper python hilighting
" fsr, this doesn't work in pymaps.vim
"let python_highlight_all = 1
"let python_highlight_numbers = 1
"let python_highlight_builtins = 1
"let python_highlight_exceptions = 1
"let python_highlight_space_errors = 1
" Python-mode settings
let g:pymode_lint = 0



" Stuff to keep JIC.
"set autoindent shiftwidth=4 expandtab tabstop=4 textwidth=80
"
"set nu
"syntax on
"set t_Co=256
"colorscheme solarized
"set background=dark

" Fast editing of the .vimrc
"map <leader>e :w<CR>:e! ~/.vimrc<CR>

" When vimrc is edited, reload it
"autocmd! bufwritepost vimrc source ~/.vimrc

"map <leader>p :set nonumber<CR>:set paste<CR>
"map <leader>o :set number<CR>:set nopaste<CR>

"highlight rightMargin term=bold ctermfg=red ctermbg=blue guifg=blue

"Define function to convert enum to string table
function! Enum2Array()
  exe "normal! :'<,'>g/^\\s*$/d\n"
  exe "normal! :'<,'>s/\\(\\s*\\)\\([[:alnum:]_]*\\).*/\\1[\\2] = \"\\2\",/\n"
  normal `>
  exe "normal a\n};\n"
  normal `<
  exe "normal iconst char *[] =\n{\n"
  exe ":'<,'>normal ==" " try some indentation
  normal `< " set the cursor at the top
endfunction

"enable cursor memory

" Tell vim to remember certain things when we exit
" "  '10  :  marks will be remembered for up to 10 previously edited files
" "  "100 :  will save up to 100 lines for each register
" "  :20  :  up to 20 lines of command-line history will be remembered
" "  %    :  saves and restores the buffer list
" "  n... :  where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo'

function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction
        
augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

"enable plugins!!
filetype plugin on

"enable syntax colouring by default
syntax on

"enable backspace
set nocompatible
set backspace=2

"call pathogen#runtime_append_all_bundles()
"call pathogen#helptags()

call pathogen#infect() 
Helptags

"Define some hotkeys for our super useful plugins!!
nmap <silent> <F2> :NERDTreeToggle<CR>
nmap <silent> <F3> :TagbarToggle<CR>

"Definition for the alternate plugin
"|let g:alternateExtensions_cxx = "hxx"
"|let g:alternateExtensions_hxx = "cxx"

"enable rainbow parentheses all the time
au VimEnter * RainbowParenthesesToggle
au Syntax * RainbowParenthesesLoadRound
au Syntax * RainbowParenthesesLoadSquare
au Syntax * RainbowParenthesesLoadBraces
set enc=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf8,prc
set guifont=Monaco:h11
set guifontwide=NSimsun:h12
set cul!
augroup XML
    autocmd!
    autocmd FileType xml let g:xml_syntax_folding=1
    autocmd FileType xml setlocal foldmethod=syntax
    autocmd FileType xml :syntax on
    autocmd FileType xml :%foldopen!
augroup END

" latex-suite settings
" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
filetype plugin on

" IMPORTANT: win32 users will need to have 'shellslash' set so that latex
" can be called correctly.
set shellslash

" OPTIONAL: This enables automatic indentation as you type.
filetype indent on

" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'

" gVim settings
if has("gui_running")
  set guifont=Dejavu\ Sans\ Mono\ Bold\ 12
endif

" Unfold all folders when reading a file
au BufRead * normal zR
