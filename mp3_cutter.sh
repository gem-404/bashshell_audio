#!/usr/bin/env bash

# set -euo pipefail
# IFS=$'\n\t'

input_dir="/home/gem-404/transcriptions"


# Iterate over each mp3 file in the directory
for input_file in "$input_dir"/*.mp3; do

    # Check if the file is actually an mp3 file
    if [ -f "$input_file" ]; then

        total_duration=$(ffprobe -i "$input_file" -show-entries format=duration -v quiet -of csv="p=0")

        # Convert total_duration to minutes
        total_minutes=$(echo "scale=2; $total_duration / 60" | bc)

        # Calculate the number of chunks needed
        num_chunks=$(echo "($total_minutes + 4) / 5" | bc)

        # Split the audio into chunks
        for ((i = 0; i < num_chunks; i++)); do
            start_time=$(echo "$i * 5 * 60" | bc)
            duration=300
            suffix=$((i + 1))

            # Adjust duration for the last chunk
            if [ "$i" -eq "$((num_chunks - 1))" ]; then
                duration=$(echo "$total_duration - $start_time" | bc)
            fi

            # Output file name
            output_file="${input_file%.*}_part${suffix}.mp3"

            # Extract the chunk using FFmpeg
            ffmpeg - i "$input_file" -ss "$start_time" -t "$duration" -c copy "$output_file"
        done

    fi

done

