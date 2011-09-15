augroup filetypedetect
au BufNewFile,BufRead *.etxt        setf etxt
au BufNewFile,BufRead UuTxt*        setf etxt
au BufRead,BufNewFile */nginx/conf/* set ft=nginx
augroup END
