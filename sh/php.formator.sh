#!/bin/bash

# PHP代码格式化工具
# @author cyy0523xc@gmail.com

# 处理php文件
# 参数
#   $1: filename
pc_process_file(){
    filename=$1
    echo $filename" is doing..."
}

# list all of php file 
# params:
#   $1: project_path
pc_list_file(){
    project_path=$1
    pushd $project_path 

    for path in $(ls $project_path);
    do
        if [ -d $path ]; then
            pc_list_file $path
        elif [ -f $path -a $(path%.php) != $path ]; then
            pc_process_file "$project_path/$path"
        fi

    done

    popd
}
