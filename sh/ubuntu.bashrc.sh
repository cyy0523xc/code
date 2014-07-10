#!/bin/bash

# 自定义bashrc

alias ssh179='ssh root@112.124.47.179'
alias ssh195='ssh root@115.29.166.195'
alias ssh35='ssh root@42.120.21.35'

alias yuic="java -jar /home/code/ibbd/cyy-doc/tools/yuicompressor-2.4.7.jar "

# elasticsearch
alias es="/home/alex/programs/elasticsearch-1.2.1/bin/elasticsearch"

# es的get数据接口
# 用法：esget cafe order '{...}'
# 参数说明：
#   $1: index
#   $2: type
#   $3: json字符串
esget() {
    echo ""
    curl -XGET "http://localhost:9200/$1/$2/_search?search_type=count" -d "$3" | python -m json.tool
    echo ""
}


