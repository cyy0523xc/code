#!/bin/bash

# 在阿里云上配置laravel运行环境
# wget https://raw.githubusercontent.com/cyy0523xc/code/master/sh/ubuntu.aliyun.config.sh -O ubuntu.aliyun.config.sh | bash ubuntu.aliyun.config.sh

# install curl 
apt-get install curl

# install php
apt-get install libapache2-mod-php5 php-apc php-pear php5  php5-cli php5-common php5-curl php5-dev php5-fpm php5-gd php5-imagick php5-mysqlnd php5-mcrypt php5-msgpack php5-mysql
 
php5enmod mcrypt 

# first install php5-mysqlnd, and then install php5-mysql
apt-get install php5-mysqlnd
apt-get install php5-mysql

# install nginx
#sudo apt-get install nginx
wget http://nginx.org/keys/nginx_signing.key
apt-key add nginx_signing.key 

# 不同ubuntu版本需要对应不同的codename
# see http://nginx.org/en/linux_packages.html#distributions
echo "" >> /etc/apt/sources.list
echo "# install nginx" >> /etc/apt/sources.list
echo "deb http://nginx.org/packages/debian/ trusty nginx" >> /etc/apt/sources.list
echo "deb-src http://nginx.org/packages/debian/ trusty nginx" >> /etc/apt/sources.list

# install
apt-get update
apt-get install nginx
 
# install git
apt-get install git

# install composer 
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

# install laravel 
#composer global require "laravel/installer=~1.1"


