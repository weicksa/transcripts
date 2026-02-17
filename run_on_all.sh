#!/bin/bash

mkdir ../transcripts_results
for f in *.mp3;
do
  python ../whisper_test.py ../min_data/${f%.mp3} ../transcripts_results;
done
