#!/bin/bash

error_log()
{
    echo $1
    exit
}

if [ $# -ne 1 ] 
then 
    error_log "the number of params is error!"
fi 

# 目录不能已经存在的
path=$1
if [ -d $path ]
then 
    error_log "$path is existed!"
fi 

# create laravel project
# php -r "copy('.env.example', '.env');"
# php artisan clear-compiled
# php artisan optimize
# php artisan key:generate
laravel new $path 

