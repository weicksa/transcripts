#!/bin/bash

mkdir ../mp3_data
for f in *.m4a; 
  do 
  ffmpeg -i "$f" -acodec libmp3lame -ab 256k ../mp3_data/"${f%.m4a}.mp3"; 
done
