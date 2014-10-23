#!/bin/bash

# git相关的操作
# Author: Alex Cai <cyy0523xc@gmail.com>

gitsub() {
    case $1 in
        "push")
            check_params $# 3
            if [ 1 -eq $? ]; then
                return
            fi
            git subtree push --prefix=$2 $2 $3
            ;;
        "pull")
            check_params $# 2
            if [ 1 -eq $? ]; then
                return
            fi
            git subtree pull --prefix=$2 $2 --squash
            ;;
        "add")
            check_params $# 3
            if [ 1 -eq $? ]; then
                return
            fi
            git subtree add --prefix=$2 $2 $3 --squash
            ;;
        "remote")
            check_params $# 3
            if [ 1 -eq $? ]; then
                return
            fi
            git remote add -f $2 $3
            ;;
        "sync")
            check_params $# 3
            if [ 1 -eq $? ]; then
                return
            fi
            gitsub pull $2
            gitsub push $2 $3
            git push 
            ;;
        "h"|"help"|*)
            cat <<EOF
params is error!

USAGES:

gitsub remote \$dir \$git_url
gitsub add    \$dir \$branch
gitsub pull   \$dir
gitsub push   \$dir \$branch
gitsub sync   \$dir \$branch     # 把子模块的内容同步到当前项目的远程分支中
gitsub help

EXAMPLES:

1. 把项目独立的文档目录加入到项目中

gitsub remote doc git@git.ibbd.net:project/weixin-printer-doc.git
gitsub add doc master

git push    # 虽然这时git status没什么改变，不过还是需要用git push，不然远程看不到对应的目录

2. 在项目目录下同步文档

gitsub pull doc 
gitsub push doc master 
git push

或者

gitsub sync doc master

EOF
            ;;
    esac

}

__gitsub_complete() {
    COMPREPLY=()
    local cur=${COMP_WORDS[COMP_CWORD]}
    local com=${COMP_WORDS[COMP_CWORD-1]}
    
    case $com in 
        'gitsub')
            COMPREPLY=($(compgen -W 'add pull push remote sync help' -- $cur))
            ;;
        'compile')
            local pro=($(awk '{print $1}' project.list))
            COMPREPLY=($(compgen -W '${pro[@]}' -- $cur))
            ;;
        *)
            ;;
    esac
    return 0
}
    
complete -F __gitsub_complete gitsub 

