import os
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def convert_file(input_path, output_path, volume, bitrate, speed):
    """Run the conversion for a single file using convert.py."""
    result = subprocess.run([
        'python', 'convert.py',
        input_path, output_path,
        '--volume', str(volume),
        '--bitrate', bitrate,
        '--speed', str(speed)
    ], check=True)
    print(f"Processed {input_path} to {output_path}")
    return result

def process_mp3s(input_list, output_folder, volume=2.0, bitrate='64k', speed=1.0, max_workers=4):
    """
    Batch process MP3 files listed in a text file using multiple threads.

    Args:
        input_list (str): Path to the file containing list of MP3 filenames.
        output_folder (str): Folder to save the processed MP3s.
        volume (float): Volume adjustment factor.
        bitrate (str): Bitrate for the output file.
        speed (float): Playback speed factor.
        max_workers (int): Number of concurrent threads for parallel processing.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read file names from input_list
    mp3_files = []
    with open(input_list, 'r') as f:
        for line in f:
            mp3_file = line.strip()  # Remove any extra whitespace
            input_path = os.path.join(os.path.dirname(input_list), mp3_file)
            output_path = os.path.join(output_folder, mp3_file)
            mp3_files.append((input_path, output_path))

    # Process files with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(convert_file, input_path, output_path, volume, bitrate, speed)
            for input_path, output_path in mp3_files
        ]

        for future in as_completed(futures):
            try:
                future.result()  # Raise any exception if occurred in the thread
            except Exception as e:
                print(f"Error processing file: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Batch process MP3 files using convert.py with parallel processing.")
    parser.add_argument("input_list", type=str, help="Path to the file containing list of MP3 filenames.")
    parser.add_argument("output_folder", type=str, help="Folder to save the processed MP3s.")
    parser.add_argument("--volume", type=float, default=2.0, help="Volume adjustment factor (default: 2.0).")
    parser.add_argument("--bitrate", type=str, default='64k', help="Bitrate for the output file (default: 64k).")
    parser.add_argument("--speed", type=float, default=1.0, help="Playback speed factor (default: 1.0).")
    parser.add_argument("--max_workers", type=int, default=4, help="Number of concurrent threads (default: 4).")

    args = parser.parse_args()
    process_mp3s(args.input_list, args.output_folder, args.volume, args.bitrate, args.speed, args.max_workers)
