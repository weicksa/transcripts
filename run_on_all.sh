#!/bin/bash

mkdir ../transcripts_results
for f in *.mp3;
do
  python whisper_test.py ${f%.mp3} ../transcripts_results;
done
