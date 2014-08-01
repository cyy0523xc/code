#!/bin/bash

# 安装应用
# @param string $1  app name
install-app() {
    if 
        ! which $1
    then
        sudo apt-get install $1
    fi
}

# 配置vim之前，必须先安装nodejs，不然在编辑js文件时会报错
#sudo apt-get install nodejs
install-app nodejs

wget https://raw.github.com/ma6174/vim/master/setup.sh -O ma6174_vim_setup.sh && bash ma6174_vim_setup.sh

install-app curl

install-app gitk

install-app guake

install-app freemind

install-app gnome-do

install-app terminator

install-app tmux



# install pinta
sudo add-apt-repository ppa:pinta-maintainers/pinta-stable
sudo apt-get update
sudo apt-get install pinta


