# Audio File Conversion and Chunk Cutting Scripts

This repo contains two Bash scripts for audio file manipulation:

1. **./dat_to_mp3_converter.sh**: This script converts .dat audio files to .mp3 format using FFmpeg.

2. **./mp3_cutter.sh**: This script splits .mp3 audio files into chunks of 5 minutes each (with the last chunk potentially shorter.)
-- Currently needs a fix...
-- Before it is fixed... enjoy its python equiv...

3. **./mp3_cutter.py**: This Python script serves as a replacement for mp3_cutter.sh. It cuts .mp3 audio files into chunks of 5 minutes each (with the last chunk potentially shorter). Additionally, it produces logs stored in output.txt.

4. **./aud_cutter.py**: This Python script is designed to cut portions of .mp3 audio files based on specified start and end times. It allows users to specify the start and end times in minutes and segments the audio accordingly.


## Instructions

### 1. Convert .dat files to .mp3

**Usage:**
```bash
./dat_to_mp3_converter.sh /path/to/input/dir

```


## Instructions

Replace start_min and end_min with the desired start and end times in minutes, respectively. The script will then cut the audio from the specified start time to the specified end time and save the resulting segment.

### 1. Cut a chunk from an audio file...

```bash
python aud_cutter.py /path/to/input/audio.mp3 start_min end_min

```
