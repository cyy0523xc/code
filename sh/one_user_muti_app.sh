#!/bin/bash

for i in {0..9}; do
    grep "&at=6" /data1/bak/wall/v3/ac201/2013070${i}/2013*|cut -d '&' -f '5,10'|sort|uniq > /tmp/test_aid_cid_0${i}
done

for i in {0..9}; do
    grep "&at=6" /data1/bak/wall/v3/ac201/2013071${i}/2013*|cut -d '&' -f '5,10'|sort|uniq > /tmp/test_aid_cid_1${i}
done

for i in {0..5}; do
    grep "&at=6" /data1/bak/wall/v3/ac201/2013072${i}/2013*|cut -d '&' -f '5,10'|sort|uniq > /tmp/test_aid_cid_2${i}
done

rm -f /tmp/test_aid_cid_all
cat /tmp/test_aid_cid_[012]* |sort|uniq > /tmp/test_aid_cid_all

cat /tmp/test_aid_cid_all |cut -d '&' -f 2|sort|uniq -c|sort -k 1 -n

