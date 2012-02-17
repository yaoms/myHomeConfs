" etxt book syntax file
" Language:     etxt format text file
" Maintainer:   Yao Mingshun <yms541@gmail.com>
" Last Change:  2011 05 24
" Last Change:  2012 02 17

" Quit when a (custom) syntax file was already loaded
if exists("b:current_syntax")
    finish
endif

syn match etxtKeyword /^<.*$/
syn match etxtKeyword /^@.*$/
syn match etxtTitle   /^#.*$/
syn match etxtComment /^!.*$/

hi def link etxtKeyword Keyword
hi def link etxtTitle   Title
hi def link etxtComment Comment

let b:current_syntax = "etxt"
