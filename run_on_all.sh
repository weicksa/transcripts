#!/bin/bash

mkdir ../transcripts_results
for f in *.mp3;
do
  python ../run_whisper.py ${f%.mp3}.mp3 ../transcripts_results;
done
