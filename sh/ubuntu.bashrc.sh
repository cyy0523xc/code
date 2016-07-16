#!/bin/bash

# 自定义bashrc
# 在~/.bashrc中被引用
# @author cyy053xc@gmail.com

# 键盘映射
#xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'

# bashrc_plugin_test() {
#     pwd
#     echo "loaded ok"
# }


# source 
#source /home/code/github/phabricator/arcanist/resources/shell/bash-completion 


# javascript和css文件压缩
# yuic input.js [output.js]
yuicompressor() {
    input_file=$1
    if [ 2 -eq $# ]; then 
        output_file=$2
    elif [ 1 -eq $# ]; then 
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

# 输出一个字符串的md5值
cyy_md5() {
    #echo $1 | md5sum
    php -r "echo md5('$1');"
    echo 
}

cyy_find() {
    if [ 1 -ne $# ]; then
        echo "find . | xargs grep -ri \$1"
        return
    fi
    find . | xargs grep -s $1 \
        | awk -F: 'BEGIN {last_file = $1}
    {
        if (keyword) {
            gsub(/'$1'/, "\033[1;31m"keyword"\033[0m", $2)
        }
        if (last_file == $1) {
            print $2;
        } else {
            last_file = $1;
            print "";
            print "\033[40;33m"$1"\033[0m";
            print $2
        }
    }' keyword=$1
}

shuangpin() {
    #xrandr --output HDMI1 --mode 1366x768 --pos 0x0 --rotate left --output VIRTUAL1 --off --output VGA1 --mode 1920x1080 --pos 768x0 --rotate normal
    bash ~/.screenlayout/shuangpin.sh
}

# 直接打开对应后缀的文件
alias -s html=vim
alias -s php=vim 
alias -s py=vim 
alias -s js=vim 
alias -s css=vim 
alias -s md=vim 

# git commit -am 
alias gitc="git commit -am "

export GOPATH=/var/www/go-src
export GOROOT=/home/alex/golang/go-go1.6.2/bin
#export GOROOT_BOOTSTRAP=$GOPATH
export PATH=/home/alex/golang/go-go1.6.2/bin:$PATH
