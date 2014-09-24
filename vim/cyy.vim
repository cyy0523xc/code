" 
" Filename: /home/code/github/code/vim/cyy.vim
" Author:   cyy0523xc@gmail.com
"

let s:cyy_plugins_path = '/home/code/github/code/vim/plugins'
"echo s:cyy_plugins_path
"!ls R/

" 测试 
function! Helloworld()
    echo "hello,world"
endfunction
command! -nargs=0 Helloworld call Helloworld()

" php_beautifier
map <C-b> :% ! php_beautifier --filters "Pear() ArrayNested()"<CR>

" powerline插件
set t_Co=256
let g:Powerline_symbols = 'unicode'
set encoding=utf8


"au BufWritePost * :echo "this is vim file."

" 如果编辑的是blog目录下的，且后缀为md的文件
" 在保存并退出vim时，需要自动git push并发布到网上
"source s:cyy_plugins_path . '/blogdeploy.vim'
source /home/code/github/code/vim/plugins/blogdeploy.vim 

