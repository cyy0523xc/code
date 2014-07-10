#!/bin/bash

# 判断函数参数的个数是否符合
#    如果函数参数不对，则直接退出程序
# param $1  函数的参数
# param $2  函数应该有的参数
params_num_check() {
    if [$# != 2 -a $1 != $2]; then
        echo "the number of params is not equal $2"
        exit 0
    fi
}


