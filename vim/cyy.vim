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

" align
" markdown table align by "|"
nmap tab\|   :call CyyAlignBy("\|")<CR>
nmap tab,    :call CyyAlignBy(",")<CR>
nmap tab=    :call CyyAlignBy("=")<CR>
nmap tab=>   :call CyyAlignBy("=>")<CR>

" 根据某字符串对齐
" 根据区块前后的空行来确定开始和结束的行号
func CyyAlignBy(string)
    let __lineno    = line('.')
    let __begin_ln  = __lineno
    let __end_ln    = __lineno

    " 向前搜索，直到空行
    while "" != getline(__begin_ln)
        let __begin_ln -= 1
        if __begin_ln < 1
            break
        endif
    endwhile

    " 向后搜索，直到空行 
    while "" != getline(__end_ln)
        let __end_ln += 1
    endwhile 

    " 生成执行命令，并执行 
    let __exec = printf('%d,%d Tab /%s', __begin_ln, __end_ln, a:string)
    echo __exec 
    exec __exec
endfunction


" au BufWritePost * :echo "this is vim file."

" 新建php文件 
autocmd BufNewFile *.php exec ":call SetCyyTitle()" 

" 定义SetCyyTitle函数
func SetCyyTitle()
    let __lineno = 0
    if &filetype == 'php'
        call setline(1, "<?php")
        call append(line("."),   "\/** ")
        call append(line(".")+1, " * @author Alex <cyy0523xc@gmail.com>")
        call append(line(".")+2, " * @copyright ")
        call append(line(".")+3, " * @see ")
        call append(line(".")+4, " * @todo ")
        call append(line(".")+5, " * @version ")
        call append(line(".")+6, " */")
        call append(line(".")+7, "")
    endif
endfunc 
autocmd BufNewFile * normal G 



" 如果编辑的是blog目录下的，且后缀为md的文件
" 在保存并退出vim时，需要自动git push并发布到网上
"source s:cyy_plugins_path . '/blogdeploy.vim'
source /home/code/github/code/vim/plugins/blogdeploy.vim 

