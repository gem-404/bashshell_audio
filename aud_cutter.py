import os
import subprocess
import sys

# Directory containing mp3 files
input_dir = "/home/gem-404/transcriptions"


# Function to cut audio files
def cut_audio(input_file, start_minute, end_minute):
    # Calculate start time and duration in seconds
    start_time = start_minute * 60
    end_time = end_minute * 60
    duration = end_time - start_time
    aud_name_first = os.path.splitext(input_file)[0]

    # Output file name
    output_file = f"{aud_name_first}_{start_minute}-{end_minute}.mp3"

    # Cut the audio using FFmpeg
    ffmpeg_cmd = ["ffmpeg", "-i", input_file, "-ss", str(start_time),
                  "-t", str(duration), "-c", "copy", output_file]
    subprocess.run(ffmpeg_cmd)


# Check if arguments are provided
if len(sys.argv) != 3:
    print("Usage: python aud_cutter.py <start_minute> <end_minute>")
    sys.exit(1)

# Get start and end minutes from command-line arguments
start_minute = int(sys.argv[1])
end_minute = int(sys.argv[2])

# Iterate over each mp3 file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith(".mp3"):
        input_file = os.path.join(input_dir, filename)
        cut_audio(input_file, start_minute, end_minute)
