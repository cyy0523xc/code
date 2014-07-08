#!/bin/bash

# elasticsearch自动安装脚本
# 
# elasticsearch的版本：1.2.1 
# kibana的版本：3.1.0 

# 目录，可以指定其他的目录
cd /home/alex/programs/

# elasticsearch
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.1.tar.gz
echo "elasticsearch download OK"

tar -vxf elasticsearch*.tar.gz
echo "elasticsearch tar OK"

# kibana
wget https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz
echo "kibana download OK"

tar -vxf kibana*tar.gz
echo "kibana tar OK"


echo "---All is OK."
