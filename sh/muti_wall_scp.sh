#!/bin/bash 

# 拉取一个星期的数据回本地

cd /home/windows/data/wall

for i in {19..25}; do
    echo 201308${i}
    mkdir 201308${i}
    scp -P 36000 ymserver@log:/data2/bak/wall/v3/201308${i}/ac201/part-*  ./201308${i}
    echo "ok"
done

echo "done"
