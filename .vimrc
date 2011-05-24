colorscheme desert
filetype on
syntax enable
set autowrite                 "自动保存

set cindent                   "C/Cxx 自动缩进

set encoding=utf-8            "VI内部编码
set langmenu=zh_CN.UTF-8      "菜单语言编码
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim
" language message zh_CN.UTF-8  "消息语言编码
set termencoding=utf-8        "终端编码
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1
                              "自动检测编码顺序
" set autoindent
" set smartindent             "自动缩进，粘贴时超长的行会被自动折行
" set cindent                 "对C语言进行智能缩进
set expandtab                 "扩展制表符，可以用空格替代tab符
set shiftwidth=4              "自动缩进的宽度
set softtabstop=4             "软制表符宽度
set tabstop=4                 "制表符宽度
" set wrap                    "自动折行，使用nowrap取消自动折行

" set fdm=indent                "启用代码折叠
" set fdc=4                     "代码折叠宽度

set lcs=tab:+-,trail:-        "TAB用 +--- 代替，行尾空格用 - 代替。
set list                      "显示tab和行尾空格

set hlsearch                  "搜索关键词高亮
set incsearch                 "表示在你输入查找内容的同时，vim就开始对你输入的内容进行匹配，并显示匹配的位置

" set mouse=a                   "在Normal,Visual,Command,help file模式中使用鼠标
set nobackup                  "取消自动备份
set nocompatible              "将使vim 以比默认的vi 兼容模式功能更强的方式运行
set number                    "显示行号
set ruler                     "显示标尺
set showcmd                   "显示命令参数
set showmode                  "显示VI编辑器模式
set title

set wildmenu                  "启动具有菜单项提示的命令行自动完成。
set cpo-=<
set wcm=<C-Z>

" Only do this part when compiled with support for autocommands
if has("autocmd")
   " When editing a file, always jump to the last cursor position
   autocmd BufReadPost *
     \ if line("'\"") > 0 && line ("'\"") <= line("$") |
     \   exe "normal! g'\"" |
     \ endif
endif




"pydiction 1.2 python auto complete
filetype plugin on
let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'
"defalut g:pydiction_menu_height == 15
"let g:pydiction_menu_height = 20
