#!/bin/bash

# elasticsearch自动安装脚本
# 
# elasticsearch的版本：1.2.2 
# kibana的版本：3.1.0 
#
# wget https://raw.githubusercontent.com/cyy0523xc/code/master/sh/ubuntu.elasticsearch.install.sh
#
# 目录，可以指定其他的目录
# NOTICES: 如果目录不同，则注意修改这里
cd /home/alex/programs/

# kibana
filename="kibana-3.1.0.tar.gz"
if ! [ -f $filename ]; then
    wget https://download.elasticsearch.org/kibana/kibana/$filename
    echo "kibana download OK"

    tar -vxf $filename
    echo "kibana tar OK"
fi

# elasticsearch
filename="elasticsearch-1.2.2.tar.gz"
dirname="elasticsearch-1.2.2"
if ! [ -f $filename ]; then
    wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$filename
    echo "elasticsearch download OK"

    tar -vxf $filename
    echo "elasticsearch tar OK"

    cd $dirname

    # marvel
    bin/plugin -i elasticsearch/marvel/latest
    echo "marvel OK"

    # es2unix
    curl -s download.elasticsearch.org/es2unix/es > bin/es 
    chmod +x bin/es
    echo "es2unix OK"

    # jetty
    # @see https://github.com/sonian/elasticsearch-jetty
    bin/plugin -url https://oss-es-plugins.s3.amazonaws.com/elasticsearch-jetty/elasticsearch-jetty-1.2.1.zip -install elasticsearch-jetty-1.2.1
    echo ""
    echo "# jetty config"
    echo "http.type: com.sonian.elasticsearch.http.jetty.JettyHttpServerTransportModule" >> config/elasticsearch.yml
    echo "elasticsearch-jetty OK"

fi

echo "---All is OK."

