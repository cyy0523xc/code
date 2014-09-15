#!/bin/bash

# 把自动启动项目cp到系统目录 

autostart_path=~/.config/autostart/
if [ ! -d $autostart_path ]; then
    mkdir $autostart_path
    echo "mkdir is OK"
fi

cp ./*.desktop $autostart_path 

echo "cp is OK!"

