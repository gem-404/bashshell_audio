#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'


for file in *.dat.unknown; do
    ffmpeg -i "$file" -codec:a libmp3lame -qscale:a 2 "${file%.dat.unknown}.mp3"
done

