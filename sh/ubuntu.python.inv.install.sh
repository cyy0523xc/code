#!/bin/bash

# python科学计算环境安装
# @see http://blog.chinaunix.net/uid-7944836-id-3253015.html

# pip是Python的一个安装和管理扩展库的工具
sudo apt-get install python-pip

# 安装Python开发环境，方便今后编译其他扩展库
sudo apt-get install python-dev

# IPython
sudo apt-get install ipython

sudo pip install tornado
sudo pip install pyzmq
sudo pip install pygments
sudo apt-get install libzmq-dev

# NumPy，SciPy和matplotlib
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-matplotlib 



