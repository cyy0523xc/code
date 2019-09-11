#!/bin/bash
# 
# 
# Author: alex
# Created Time: 2019年07月22日 星期一 15时55分35秒
curl -XPOST -F "file=@$1" http://192.168.80.245:5000/recognize
