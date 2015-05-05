#!/bin/bash

index=0

ifs=$IFS
IFS=
cat ./test.sh  | while read myline
do
    let index++
    echo "$index: $myline"
done

IFS=$ifs

