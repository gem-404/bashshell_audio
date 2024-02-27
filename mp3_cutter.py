"""
Python file for cutting audio files into chunks of 5 minutes each.
"""
import os
import subprocess

# Directory containing mp3 files
input_dir = "/home/gem-404/transcriptions"


# Function to split audio files into chunks
def split_audio(input_file):
    # Calculate total duration in seconds
    ffprobe_cmd = ["ffprobe", "-i", input_file, "-show_entries",
                   "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    total_duration = float(subprocess.check_output(ffprobe_cmd).strip())
    total_minutes = total_duration / 60

    # Calculate the number of chunks needed
    num_chunks = int((total_minutes + 4) / 5)

    # Split the audio into chunks
    for i in range(num_chunks):
        start_time = i * 5 * 60
        duration = 300
        suffix = i + 1

        # Adjust duration for the last chunk
        if i == num_chunks - 1:
            duration = total_duration - start_time

        # Output file name
        output_file = f"{os.path.splitext(input_file)[0]}_part{suffix}.mp3"

        # Extract the chunk using FFmpeg
        ffmpeg_cmd = ["ffmpeg", "-i", input_file, "-ss", str(start_time), "-t",
                      str(duration), "-c", "copy", output_file]
        subprocess.run(ffmpeg_cmd)

        # Write output to a file
        with open("output.txt", "a") as f:
            f.write(f"Split {input_file} into {output_file}\n")


# Iterate over each mp3 file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".mp3"):
        input_file = os.path.join(input_dir, filename)
        split_audio(input_file)
