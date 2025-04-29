#!/bin/bash

input_file="/mnt/kiso-qnap3/hurigana-speech-corpus-aozora/train/1y4eRgkEey/3VA5QzZL1f/D50JsbGwQA/9Y1hiCvbzIPfqYooLoME.mp3"
output_file="/mnt/kiso-qnap3/yuabe/m1/useWhisper/data/train/audio/short_clip.mp3"

ffmpeg -y -i "$input_file" -t 30 "$output_file"
