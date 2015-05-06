" 
" Filename: /home/code/github/code/vim/cyy.vim
" Author:   cyy0523xc@gmail.com
"

let s:cyy_plugins_path = '/home/code/github/code/vim/plugins'
"echo s:cyy_plugins_path
"!ls R/

" 键值映射
au VimEnter * !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'

" 测试 
function! Helloworld() range
    echo "hello,world"
    echo a:firstline
    echo a:lastline
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


" 该函数仅作备份使用
func BakCyyAlignBy(string)
    let __lineno    = line('.')

    " 如果当前行为空行
    if "" == getline(__lineno)
        return
    endif
    
    " 开始行号和结束行号 
    let __begin_ln  = __lineno
    let __end_ln    = __lineno

    " 当前行开头的空格数
    let __space_num = indent(__lineno)
    echo __space_num

    " 向前搜索，直到空行或者前面空格不相等的行
    while "" != getline(__begin_ln-1) && __space_num == indent(__begin_ln-1)
        let __begin_ln -= 1
        if __begin_ln == 1
            break
        endif
    endwhile

    " 向后搜索，直到空行或者前面空格不相等的行
    while "" != getline(__end_ln+1) && __space_num == indent(__end_ln+1)
        let __end_ln += 1
    endwhile

    if __end_ln == __begin_ln
        return 
    endif

    " 生成执行命令，并执行 
    let __exec = printf('%d,%d Tab /%s', __begin_ln, __end_ln, a:string)
    echo __exec 
    exec __exec
endfunction

" 根据每行前缀的空格(指定行)进行对齐
" func CyyAlignPreSpace() range


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
"let g:user_emmet_leader_key='<C-Z>'


" 如果编辑的是blog目录下的，且后缀为md的文件
" 在保存并退出vim时，需要自动git push并发布到网上
"source s:cyy_plugins_path . '/blogdeploy.vim'
source /home/code/github/code/vim/plugins/blogdeploy.vim 

