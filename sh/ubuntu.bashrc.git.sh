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
        *)
            cat <<EOF
params is error!

USAGES:

gitsub add \$dir \$branch 
gitsub pull \$dir 
gitsub push \$dir \$branch
EOF
            ;;
    esac

}

