#!/bin/bash
while true
do 
    for file in $(cat madplay.m3u)
    do 
        echo $(cat madplay.m3u)
        echo "播放：$file"
        madplay -o wav:- "$file" | aplay -q
    done
done