#!/bin/bash

input_file="/mnt/kiso-qnap3/hurigana-speech-corpus-aozora/test/4SBmtE4oT0/Boqfggcfos/yOr4eeSK8I/QXPS9XBZnsZYReQqe1uV.mp3"
output_file="/mnt/kiso-qnap3/yuabe/m1/useWhisper/data/audio/short_clip.mp3"

ffmpeg -y -i "$input_file" -t 30 "$output_file"
