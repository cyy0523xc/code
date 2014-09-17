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
    if [ "d" -eq $1 ]; then
        # deploy blog 
        pushd "/home/code/github/cyy0523xc.github.io/source/"
        git pull 

        pushd "/home/code/github/cyy0523xc.github.io/"
        hexo g
        hexo d

        popd
        popd 
    elif [ "e" -eq $1 ]; then
        # edit blog 
        if [ -f $2 ]; then 
            vim $2

            git commit -am "Edited $2"
            git push

            blog d 
        else
            echo "file: \"$2\" is not exists!"
        fi 
    else 
        # write a new blog 
        cd /home/code/github/blog/ 
        tmp=$(hexo n $1)
        echo $tmp

        filename=${tmp##*/}
        vim $filename

        git commit -am "Created $filename"
        git push 
        echo "push ok"
        
        blog d
    fi 
}


