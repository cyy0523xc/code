#!/bin/bash 

path=/home/windows/data/spot/
echo $path

for i in "00" "01" "02" "11"; do
    cd $path
    mkdir ac8${i}
    cd ac8${i}
    echo ac8${i}
    for j in {19..25}; do
        mkdir 201308${j}
        scp -P 36000 ymserver@log:/data2/bak/spot2/v2/201308${j}/ac8${i}/part-* ./201308${j}/
    done
done

echo "done"

