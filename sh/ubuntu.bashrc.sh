#!/bin/bash

# 自定义bashrc
# 在~/.bashrc中被引用
# @author cyy053xc@gmail.com

# 服务器快速登陆
alias ssh179='ssh root@112.124.47.179'
alias ssh195='ssh root@115.29.166.195'
alias ssh35='ssh root@42.120.21.35'

# javascript和css文件压缩
alias yuic="java -jar /home/code/ibbd/cyy-doc/tools/yuicompressor-2.4.7.jar "

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
        cd $default_dir/$dir/
        git checkout master
        git pull
        echo "----- $dir is ok."
        echo ""
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
    
    if [ "h" = $1 ]; then
        cat <<EOF
This is help for blog.

blog [-hde] [title]

n title    : wrie a new blog 
d          : deploy blog 
e title    : edit blog 
p          : goto the blog path
a title.md : add new exists blog 
h          : help

EOF
    elif [ "p" = $1 ]; then
        cd $blog_post_path"_posts/"
    elif [ "d" = $1 ]; then
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
    elif [ "e" = $1 ]; then
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
    elif [ "a" = $1 ]; then
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
    elif [ "n" = $1 ]; then  
        # write a new blog 
        # 避免同名文件
        pushd $blog_post_path"_posts/"
        if [ -f $2 -o -f $2".md" ]
        then 
            echo "the file is exists!"
            exit 0
        fi 
        popd 

        # begin write 
        echo "Write a new blog begin:"
        pushd $blog_path 
        tmp=$(hexo n $1)
        echo $tmp

        pushd $blog_source_path
        git add _posts/*
        git commit -am "Created ${tmp##*/}"
        git push 
        popd

        popd
        blog e ${tmp##*/}
    else
        blog h
    fi 
}

# github相关操作 
github() {
    cd_github_code
    my_github=git@github.com/cyy053xc/

    case $1 in 
        "h")
            cat <<EOF
github [hpc] [path] 

usage:
h              : help
c  project     : git clone {$my_github}project.git
l  project     : git pull 
s  project     : git push 
EOF
            ;;
        "c")
            git clone $my_github$2".git"
            ;;
        "l")
            pushd $my_github$2
            git pull
            popd
            ;;
        "s")
            pushd $my_github$2
            git pull 
            git commit -am 'script commit'
            git push 
            popd
            ;;
        *)
            github h
            ;;
    esac
}
