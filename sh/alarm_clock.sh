#!/bin/bash
# 
# 晚上休息闹钟
# Author: Alex
# Created Time: 2016年11月06日 星期日 23时02分17秒

# 休息时间配置
time_begin=2300
time_end=800

hm=`date +'%k%M'`
if [ $hm -gt $time_begin -o $hm -lt $time_end ]; then
    echo "Time to sleep"
    firefox
fi
