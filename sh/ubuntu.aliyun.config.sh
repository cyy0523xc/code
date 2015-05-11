#!/bin/bash

# 在阿里云上配置laravel运行环境
# wget https://raw.githubusercontent.com/cyy0523xc/code/master/sh/ubuntu.aliyun.config.sh -O ubuntu.aliyun.config.sh | bash ubuntu.aliyun.config.sh

# install curl 
apt-get install curl

# install php
apt-get install libapache2-mod-php5 php-apc php-pear php5  php5-cli php5-common php5-curl php5-dev php5-fpm php5-gd php5-imagick php5-mysqlnd php5-mcrypt php5-msgpack php5-mysql
 
php5enmod mcrypt 

apt-get install php5-mysqlnd php5-mysql

sudo apt-get install nginx
 
# install git
apt-get install git

# install composer 
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

# install laravel 
#composer global require "laravel/installer=~1.1"


