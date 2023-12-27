#!/bin/bash
while true
do 
    for file in $(cat madplay.m3u)
    do 
        echo $(cat play.m3u)
        echo "播放：$file"
        madplay -o wav:- "$file" | aplay 
    done
done