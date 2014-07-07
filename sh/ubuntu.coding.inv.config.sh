#!/bin/bash

sudo mkdir /home/code
sudo chown -Rh alex:alex /home/code

cd /home/code 

# github
mkdir github
cd github
git clone git@github.com:cyy0523xc/code.git
git clone git@github.com:cyy0523xc/R.git
git clone git@github.com:cyy0523xc/raw.git

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





