#!/bin/sh
NAME="$1"
iconv -f GB18030 "$NAME" -o "${NAME}.utf8" && mv "${NAME}.utf8" "$NAME"
