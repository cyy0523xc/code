#!/bin/bash

# git相关的操作
# Author: Alex Cai <cyy0523xc@gmail.com>

gitsub() {
    case $1 in
        "push")
            git subtree push --prefix=$2 $2 $3
            ;;
        "pull")
            git subtree pull --prefix=$2 $2 --squash
            ;;
        "add")
            git subtree add --prefix=$2 $2 $3 --squash
            ;;
        "remote")
            git remote add -f $2 $3
            ;;
        "h"|"help"|*)
            cat <<EOF
params is error!

USAGES:

gitsub remote \$dir \$git_url
gitsub add    \$dir \$branch
gitsub pull   \$dir
gitsub push   \$dir \$branch
gitsub help
EOF
            ;;
    esac

}

gitsub_complete() {
    COMPREPLY=()
    local cur=${COMP_WORDS[COMP_CWORD]}
    local com=${COMP_WORDS[COMP_CWORD-1]}
    
    case $com in 
        'gitsub')
            COMPREPLY=($(compgen -W 'add pull push remote help' -- $cur))
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
    
complete -F gitsub_complete gitsub 
