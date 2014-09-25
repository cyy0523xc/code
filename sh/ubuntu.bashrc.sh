#!/bin/bash

# 自定义bashrc
# 在~/.bashrc中被引用
# @author cyy053xc@gmail.com

# 服务器快速登陆
alias ssh179='ssh root@112.124.47.179'
alias ssh195='ssh root@115.29.166.195'
alias ssh35='ssh root@42.120.21.35'

# javascript和css文件压缩
# yuic input.js [output.js]
yuicompressor() {
    input_file=$1
    if [ 2 -eq $# ]; then 
        output_file=$2
    elif [ 1 -eq $# ]
        # 如果只有一个参数，则文件名使用: input.min.js （假设原来是input.js）
        file_type=${input_file##*.}
        len=${#file_type}
        output_file=${input_file:0:-$len}"min."$file_type
    else 
        echo "The number of params is error."
        return;
    fi 

    java -jar /home/code/ibbd/cyy-doc/tools/yuicompressor-2.4.7.jar $input_file -o $output_file --charset utf-8
    echo "yuicompressor OK."
}

# elasticsearch
alias es="/home/alex/programs/elasticsearch-1.2.2/bin/elasticsearch"

# es的get数据接口
# 用法：esget cafe order '{...}'
# 参数说明：
#   $1: index
#   $2: type
#   $3: json字符串
esget() {
    echo ""
    curl -XGET "http://localhost:9200/$1/$2/_search?search_type=count" -d "$3" | python -m json.tool
    echo ""
}

esput() {
    echo ""
    curl -XPUT "http://localhost:9200/$1/$2/" -d "$3" | python -m json.tool

}

# cd github目录
cd_github_code() {
    cd /home/code/github/
}

# cd开发目录
cd_ibbd_code() {
    cd /home/code/ibbd/ 
}

# cd博客目录
cd_blog() {
    cd /home/code/github/blog/_posts/ 
}

# gitlab: new project
# 参数说明：
#   $1: project name
#   $2: group name, the default value is "ibbd"
ibbd_git_init() {
    if [ 2 -eq $# ]; then
        groupname=$2
    else
        groupname="ibbd"
    fi

    cd_ibbd_code
    mkdir $1
    cd $1
    git init
    touch README.md
    echo "# 项目：$1" >> README.md
    echo "  Created at " $(date) >> README.md
    echo "  Gitlab: git@git.ibbd.net:${groupname}/$1\.git"
    git add README.md
    git commit -m 'first commit'
    git remote add origin git@git.ibbd.net:${groupname}/$1\.git
    git push -u origin master

    echo ""
    echo "project $1 is OK!"
}

# 输出一个字符串的md5值
cyy_md5() {
    echo $1 | md5sum
}

# git pull all
# 一次性git pull所有代码
# 参数说明
#   $1: 目录，默认为：/home/code/ibbd
git_pull_all() {
    if [ 1 -eq $# ]; then 
        default_dir=$1
    else
        default_dir=/home/code/ibbd
    fi

    # git pull 
    for dir in $(ls $default_dir);
    do 
        echo $default_dir/$dir/
        pushd $default_dir/$dir/
        git checkout master
        git pull
        echo "----- $dir is ok."
        echo ""
        popd 
    done 

    echo "-------------------------------"
    echo "All is ok!"
}


# blog相关操作
# 
# blog "filename"     : new blog
# blog e "filename"   : Edit blog
# blog d              : deploy blog 
#
blog() {
    blog_path=/home/code/github/cyy0523xc.github.io/
    blog_post_path=/home/code/github/blog/
    blog_source_path="/home/code/github/cyy0523xc.github.io/source/"
   
    case $1 in 
        "p"|"path")
            cd $blog_post_path"_posts/"
            ;;

        "d"|"deploy")
            # deploy blog 
            echo "Deploy blog begin:"
            pushd $blog_source_path
            git pull 

            pushd $blog_path
            hexo g
            hexo d

            popd
            popd 

            echo "Deploy blog end."
            ;;

        "e"|"edit")
            # edit blog 
            cd $blog_post_path 
            git pull 

            filename=$2
            filename=${filename##*/}
            if [ -f _posts/$filename ]; then 
                echo "Edit blog begin: "
                vim _posts/$filename

                git commit -am "Edited $filename"
                git push

                blog d 
                echo "Edit blog end."

                cd _posts/
            else
                echo "file: \"$filename\" is not exists!"
            fi 
            ;;

        "a"|"add")
            # add an md file to blog 
            if [ -f $2 ]; then 
                cp $2 $blog_post_path"_posts/"
                pushd $blog_post_path 
                git add _posts/$2
                git commit -am "Add new blog $2"
                git push 
                popd

                pushd $blog_source_path
                git pull 
                hexo g
                hexo d
                popd 
            fi 
            ;;

        "n"|"new")
            # write a new blog 
            filename=$2
            filename=${filename##*/}

            # 避免同名文件
            pushd $blog_post_path"_posts/"
            if [ -f $filename -o -f $filename".md" ]
            then 
                echo "the file is exists!"
            fi 
            popd 

            # begin write 
            echo "Write a new blog begin:"
            pushd $blog_path 
            tmp=$(hexo n $filename)
            echo $tmp

            pushd $blog_source_path
            git add _posts/*
            git commit -am "Created ${tmp##*/}"
            git push 
            popd

            popd
            blog e ${tmp##*/}
            ;;

        "b"|"bak"|"backup")
            cp_all /home/code/github/cyy0523xc.github.io /home/code/github/bak.all.blog 
            
            pushd /home/code/github/bak.all.blog/ 
            git add ./*
            git commit -am 'bak'
            git push 
            popd 

            echo "Backup is ok!"
            ;;

        "h"|"help"|*)
            cat <<EOF
This is help for blog.

blog [-hdenpa] [title]

n|new    title     : wrie a new blog 
d|deploy           : deploy blog 
e|edit   title     : edit blog 
p|path             : goto the blog path
a|add    title.md  : add new exists blog 
b|bak|backup       : backup all files 
h|help             : help

EOF
        ;;

    esac 
}

# github相关操作 
github() {
    cd_github_code
    my_github=git@github.com/cyy053xc/

    case $1 in 
        "c"|"clone")
            git clone $my_github$2".git"
            ;;
        "l"|"pull")
            pushd $my_github$2
            git pull
            popd
            ;;
        "s"|"push")
            pushd $my_github$2
            git pull 
            git commit -am 'script commit'
            git push 
            popd
            ;;
        "h"|"help"|*)
            cat <<EOF
github [hcls] [path] 

usage:
h|help               : help
c|clone  project     : git clone {$my_github}project.git
l|pull   project     : git pull 
s|push   project     : git push 
EOF
            ;;
    esac
}

function _github() {
    COMPREPLY=()
    local cur=${COMP_WORDS[COMP_CWORD]};
    local com=${COMP_WORDS[COMP_CWORD-1]};
    case $com in
        'github')
            COMPREPLY=($(compgen -W 'c clone l pull s push h help' -- $cur))
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

complete -F _github github 

# 把文件从一个目录copy到另一个目录
# Usage : cp_all  path1 path2
cp_all() {
    if [ 2 -ne $# ]; then
        # 如果不是两个参数，则输出帮助信息
        echo 'The number of params is not equal 2!'
        echo <<HELP 
cp_all: Copy all files from source dir to target dir.

usage:
cp_all source_dir target_dir
HELP
        return
    fi

    if [ -f $1 ]; then 
        # if it is file, then copy 
        cp $1 $2
    elif [ -d $1 ]; then 
        # if it is dir, then ls
        echo $1

        if [ ! -d $2 ]; then 
            # 如果源路径是一个目录，则目标路径的目录必须存在
            mkdir $2 
        fi 

        for i in $(ls $1)
        do
            src_path=$1/$i
            target_path=$2/$i
            cp_all $src_path $target_path
        done
    else
        echo "$1 : is not a file or a dir!"
    fi 

}
