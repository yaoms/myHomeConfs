" UuTxt ebook syntax file
" Language:     UuTxt format text file
" Maintainer:   Yao Mingshun <yms541@gmail.com>
" Last Change:  2011 05 24

" Quit when a (custom) syntax file was already loaded
if exists("b:current_syntax")
    finish
endif

syn match       uutxtKeyword    /^书名\(:\)\@=/
syn match       uutxtKeyword    /^作者\(:\)\@=/
syn match       uutxtKeyword    /^编号\(:\)\@=/
syn match       uutxtKeyword    /\( \)\@<=字数\(:\)\@=/
syn match       uutxtTitle      /^.*\( 字数:\)\@=/
syn match       uutxtTitle      /\(编号:\|书名:\|作者:\|字数:\)\@<=.*/
syn match       uutxtIndent     /^  /
syn match       uutxtComment    /^[^ 书作编][^ 名者号]\(\(字数:\)\@<!.\)\+$/

hi def link uutxtKeyword        Keyword
hi def link uutxtTitle          Title
hi def link uutxtIndent         Conceal
hi def link uutxtComment        Comment

let b:current_syntax = "etxt"
