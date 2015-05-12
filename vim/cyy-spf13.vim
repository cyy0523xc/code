"
" Filename: /home/code/github/code/vim/cyy.vim
" Author:   cyy0523xc@gmail.com
"

" 测试
function! Helloworld() range
    echo "hello,world"
    echo a:firstline
    echo a:lastline
endfunction
command! -nargs=0 Helloworld call Helloworld()

nmap tt :%s/\t/    /g<CR>

" align
" markdown table align by "|"
nmap tab\|   :call CyyAlignBy("\|")<CR>
nmap tab,    :call CyyAlignBy(",")<CR>
nmap tab=    :call CyyAlignBy("=")<CR>
nmap tab=>   :call CyyAlignBy("=>")<CR>

" 根据某字符串对齐，依赖于 tabular 插件
" 根据区块前后的空行来确定开始和结束的行号
func CyyAlignBy(string)
    let lineno    = line('.')

    " 如果当前行为空行
    if "" == getline(lineno)
        return
    endif

    " 计算首行和尾行
    let indent_pat = '^' . matchstr(getline(lineno), '^\s*') . '\S'
    let firstline  = search('^\%('. indent_pat . '\)\@!','bnW') + 1
    let lastline   = search('^\%('. indent_pat . '\)\@!', 'nW') - 1
    if lastline < 0
        let lastline = line('$')
    endif

    if firstline == lastline
        return 
    endif

    " 生成执行命令，并执行 
    let __exec = printf('%d,%d Tab /%s', firstline, lastline, a:string)
    echo __exec 
    exec __exec
endfunc


" 新建php文件 
autocmd BufNewFile *.php exec ":call SetCyyTitle()" 

" 定义SetCyyTitle函数
func SetCyyTitle()
    let __lineno = 0
    if &filetype == 'php'
        call setline(1, "<?php")
        call append(line("."),   "\/** ")
        call append(line(".")+1, " * @author Alex <cyy0523xc@gmail.com>")
        call append(line(".")+2, " * @copyright IBBD.net")
        call append(line(".")+3, " * @see ")
        call append(line(".")+4, " * @todo ")
        call append(line(".")+5, " * @version " . strftime("%Y-%m-%d"))
        call append(line(".")+6, " */")
        call append(line(".")+7, "")
    endif
endfunc 
autocmd BufNewFile * normal G 


" 暂时屏蔽光标键 
"normal <Up>    <Nop>
"normal <Down>  <Nop>
"normal <Left>  <Nop>
"normal <Right> <Nop>


" 插件
Plugin 'mattn/emmet-vim'
let g:user_emmet_mode='n'
let g:user_emmet_install_global = 0
autocmd FileType html,css,js,php EmmetInstall

Bundle "airblade/vim-gitgutter"
Bundle "gregsexton/gitv"
Bundle "Raimondi/delimitMate"


" 键值映射
"au VimEnter * !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'
