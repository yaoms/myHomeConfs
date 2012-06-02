#!/bin/bash
ffmpeg -i "$1" -s qvga -acodec libfaac -ar 22050 -ab 128k -vcodec libx264 -threads 0 -f ipod "$2"
