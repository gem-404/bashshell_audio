# Audio File Conversion and Chunk Cutting Scripts

This repo contains two Bash scripts for audio file manipulation:

1. **./dat_to_mp3_converter.sh**: This sript converts .dat audio files to .mp3 format using FFmpeg.

2. **./mp3_cutter.sh**: This script splits .mp3 audio files into chunks of 5 minutes each (with the last chunk potentially shorter.)
-- Currently needs a fix...
-- Before it is fixed... enjoy its python equiv...

3. **./mp3_cutter.py**: Does what mp3_cutter.sh was intended to do. (Also produces logs stored in output.txt)

## Instructions

### 1. Convert .dat files to .mp3

**Usage:**
```bash

./dat_to_mp3_converter.sh /path/to/input/dir

```
