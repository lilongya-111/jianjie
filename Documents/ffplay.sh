#!/bin/bash
while true
do 
    for file in $(cat madplay.m3u)
    do 
        echo $(cat madplay.m3u)
        echo "播放：$file"
        ffplay "$file"  
    done
done