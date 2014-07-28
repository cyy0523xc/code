#!/bin/bash

while getopts "s:a" opt;
do
    case $opt in
        s) echo "s is ok"
            ;;
        a) echo "a is ok"
            ;;
        *) echo "****"
            ;;
    esac
done


