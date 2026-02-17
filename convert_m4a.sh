#!/bin/bash

mkdir ../data_mp3
for f in *.m4a; 
  do 
  ffmpeg -i "$f" -acodec libmp3lame -ab 256k ../data_mp3/"${f%.m4a}.mp3"; 
done
