#!/bin/bash

sudo apt-get install nginx
sudo apt-get install mysql-server
sudo apt-get install php5 php5-common php5-cli php5-mysql php5-curl php5-gd php5-mcrypt php5-cgi php5-dev


# pear 
sudo apt-get install php-pear

# install pdo 

# pman   过程可能有点慢 
sudo pear install doc.php.net/pman
sudo pear upgrade pear


