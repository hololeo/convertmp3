# MP3 Converter Utility

This project is a Python-based utility for converting `.mp3` files in a specified directory with custom audio settings using `ffmpeg`. The script allows you to adjust audio properties such as volume, bitrate, and playback speed for each file. This project includes two main scripts: `listmp3.py` to list `.mp3` files and `convert.py` to convert audio files with specific configurations.

## Requirements

- **Python 3.6+**
- **ffmpeg**: The `ffmpeg` tool is required for audio conversions. Install via:
  ```bash
  # MacOS
  brew install ffmpeg

  # Debian/Ubuntu
  sudo apt-get install ffmpeg
  ```

- **Python Packages**: No external Python packages are required beyond the standard library.

## Scripts Overview

### 1. `listmp3.py`

This script lists all `.mp3` files in a specified directory and outputs the full file paths. The paths can be saved to a text file or printed to the console.

**Usage**:
```bash
python listmp3.py <directory_path> [-o output_file.txt]
```

- **`<directory_path>`**: The directory to search for `.mp3` files.
- **`-o output_file.txt`** *(optional)*: Specifies a file to save the list of `.mp3` paths.

Example:
```bash
python listmp3.py /path/to/mp3files -o file.txt
```

This will create `file.txt` with the full paths of all `.mp3` files found in `/path/to/mp3files`.

### 2. `convert.py`

This script converts an audio file with the specified volume, bitrate, and playback speed.

**Usage**:
```bash
python convert.py <input_file> <output_file> [--volume <volume_factor>] [--bitrate <bitrate>] [--speed <speed_factor>]
```

- **`<input_file>`**: Path to the input `.mp3` file.
- **`<output_file>`**: Path to save the converted file.
- **`--volume`**: (Optional) Volume adjustment factor. Default is `2.0`.
- **`--bitrate`**: (Optional) Bitrate for the output file, e.g., `64k`. Default is `64k`.
- **`--speed`**: (Optional) Playback speed factor. Default is `1.0`.

Example:
```bash
python convert.py "/path/to/input.mp3" "/path/to/output.mp3" --volume 2.5 --bitrate 128k --speed 1.2
```

### 3. Batch Conversion with `file.txt`

To convert multiple `.mp3` files listed in a file:

1. Use `listmp3.py` to generate a list of `.mp3` file paths:
   ```bash
   python listmp3.py /path/to/mp3files -o file.txt
   ```

2. Use a batch processing script (e.g., `batch_convert.py`) that reads each line from `file.txt` and applies `convert.py` to each file. This file should output converted files to a separate directory.

## How It Works

1. **Listing Files**: `listmp3.py` generates a list of `.mp3` file paths, which can be saved to a file.
2. **Conversion**: `convert.py` uses `ffmpeg` to convert each file with custom settings for volume, bitrate, and speed.
3. **Batch Processing**: `batch_convert.py` (not shown here) loops through each file in `file.txt`, applies `convert.py` to convert each one, and saves them to an output directory.

## Example Workflow

```bash
# Step 1: List all mp3 files in a directory
python listmp3.py /path/to/mp3files -o file.txt

# Step 2: Convert each file listed in file.txt
# Run batch_convert.py to apply settings to all files
python batch_convert.py --input-file file.txt --output-dir /path/to/converted --volume 2.0 --bitrate 64k --speed 1.0
```

### Notes
- The converted files are saved with the same names as the originals.
- Ensure `ffmpeg` is installed and accessible in your PATH.
