#!/bin/bash

#sudo apt-get install nginx
#sudo apt-get install mysql-server
#sudo apt-get install php5

cd /home/alex/programs/
wget -c http://soft.vpser.net/lnmp/lnmp1.1-full.tar.gz && tar zxf lnmp1.1-full.tar.gz && cd lnmp1.1-full && ./ubuntu.sh
