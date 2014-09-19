#!/bin/bash

# 1）Dropbox的安装依赖python-gpgme

sudo apt-get install python-gpgme

# 2）输入以下命令添加Dropbox软件库key

sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 5044912E

# 3）输入以下命令在Ubuntu 12.04中添加Dropbox软件库

sudo add-apt-repository "deb http://linux.dropbox.com/ubuntu $(lsb_release -sc) main"

# 4）更新系统并安装Dropbox

sudo apt-get update && sudo apt-get install nautilus-dropbox

echo "Install dropbox OK!"

