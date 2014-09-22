#!/bin/bash


# ******************   GIT   ************************

sudo mkdir /home/code
sudo chown -Rh alex:alex /home/code

# config
git config --global user.email 'cyy0523xc@gmail.com'
git config --global user.name  "alex cai"
git config --global push.default simple

cd /home/code 

# github
mkdir github
cd github
git clone git@github.com:cyy0523xc/code.git
git clone git@github.com:cyy0523xc/R.git
git clone git@github.com:cyy0523xc/raw.git
git clone git@github.com:cyy0523xc/blog.git
git clone git@github.com:cyy0523xc/cyy0523xc.github.io.git

# ibbd
cd /home/code/
mkdir ibbd
cd ibbd
git clone git@git.ibbd.net:ibbd/ibbdcrm.git
git clone git@git.ibbd.net:caiyingyao/cyy-doc.git
git clone git@git.ibbd.net:caiyingyao/raw.git
git clone git@git.ibbd.net:ibbd/juketong-intl.git
git clone git@git.ibbd.net:ibbd/juketong-cafe-deco.git
git clone git@git.ibbd.net:ibbd/ibbdcrm-tasks.git


# ****************** 其他配置 ***********************

self_config_path=/home/alex/github/code

# 自定义bashrc
echo "" >> ~/.bashrc 
echo "# 自定义bashrc" >> ~/.bashrc
echo "." $self_config_path/sh/ubuntu.bashrc.sh  >> ~/.bashrc

# 自定义vim
echo "" >> ~/.vimrc 
echo "# 自定义vimrc" >> ~/.vimrc 
echo "source $self_config_path/vim/cyy.vim" >> ~/.vimrc 

