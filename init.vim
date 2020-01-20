" Plugins
if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin(stdpath('config').'/plugged')

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'altercation/vim-colors-solarized'
Plug 'alvan/vim-closetag'

call plug#end()

" close tag for tsx, jsx and html
let g:closetag_filenames = "*.html,*.xhtml,*.phtml,*.erb,*.jsx,*.tsx"
let g:closetag_xhtml_filenames = '*.xhtml,*.jsx,*.erb,*.tsx'
let g:closetag_emptyTags_caseSensitive = 1
let g:closetag_regions = {
    \ 'typescript.tsx': 'jsxRegion,tsxRegion',
    \ 'javascript.jsx': 'jsxRegion',
    \ }

" coc nvim

" if hidden is not set, TextEdit might fail.
set hidden

" Some servers have issues with backup files, see #649
set nobackup
set nowritebackup

" Better display for messages
set cmdheight=2

" You will have bad experience for diagnostic messages when it's default 4000.
set updatetime=300

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
"set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <leader>rn <Plug>(coc-rename)

" Remap for format selected region
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Create mappings for function text object, requires document symbols feature of languageserver.
xmap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap if <Plug>(coc-funcobj-i)
omap af <Plug>(coc-funcobj-a)

" Use <TAB> for select selections ranges, needs server support, like: coc-tsserver, coc-python
nmap <silent> <TAB> <Plug>(coc-range-select)
xmap <silent> <TAB> <Plug>(coc-range-select)

" Use `:Format` to format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` to fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" use `:OR` for organize import of current buffer
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add status line support, for integration with other plugin, checkout `:h coc-status`
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Using CocList
" Show all diagnostics
nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions
nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols
nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
nnoremap <silent> <space>p  :<C-u>CocListResume<CR>
" legacy from vim
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
set cul cuc
hi CursorLine   cterm=NONE ctermbg=darkgrey ctermfg=white guibg=darkred guifg=white
hi CursorColumn cterm=NONE ctermbg=darkgrey ctermfg=white guibg=darkred guifg=white
augroup CursorLine
    au!
    au VimEnter,WinEnter,BufWinEnter * setlocal cul cuc
    au WinLeave * setlocal nocursorline nocursorcolumn
augroup END

if has('win32') || has ('win64')
  let $VIMHOME = $VIM."/vimfiles"
else
  let $VIMHOME = $HOME."/.vim"
endif

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

" toggle cursorline & cursorcolumn
nmap <Leader>c :set cursorline! cursorcolumn!<CR>

" quick save and nav shortcuts
nmap <leader>w :w<CR>
nmap <leader>q :q<CR>
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
let g:pymode_options = 0

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

set nocompatible

filetype plugin indent on

set foldenable

set foldmethod=syntax

au FileType sh let g:sh_fold_enabled=5

au FileType sh let g:is_bash=1

au FileType sh set foldmethod=syntax

syntax enable

"augroup javascript_folding
"  au!
"  au FileType javascript setlocal foldmethod=syntax
"augroup END

"Define some hotkeys for our super useful plugins!!
nmap <silent> <F2> :CocCommand explorer<CR>
nmap <silent> <F3> :TagbarToggle<CR>

"Definition for the alternate plugin
"|let g:alternateExtensions_cxx = "hxx"
"|let g:alternateExtensions_hxx = "cxx"

"enable rainbow parentheses all the time
let g:rainbow_active = 1
set enc=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf8,prc
set guifont=Monaco:h11
set guifontwide=NSimsun:h12
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

" markdown configuration
let g:markdown_enable_spell_checking=0

syntax enable
set background=dark
colorscheme solarized
