import subprocess
import argparse
import shlex

def convert_audio(input_file, output_file, volume=2, bitrate='32k', speed=1.0):
    """
    Convert audio file using ffmpeg.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Desired output file name.
        volume (float): Volume adjustment factor (default is 2.0).
        bitrate (str): Bitrate for the output file (default is '64k').
        speed (float): Playback speed factor (default is 1.0).
    """
    command = [
        'ffmpeg',
        '-i', input_file,
        '-b:a', bitrate,
        '-filter:a', f"volume={volume},atempo={speed}",
        '-y',  # Overwrite output file without asking
        output_file
    ]

    # Execute the command
    subprocess.run(command, check=True)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert audio files using ffmpeg.')
    parser.add_argument('input_file', type=str, help='Path to the input audio file.')
    parser.add_argument('output_file', type=str, help='Desired output file name.')
    parser.add_argument('--volume', type=float, default=2.0, help='Volume adjustment factor (default: 2.0).')
    parser.add_argument('--bitrate', type=str, default='64k', help='Bitrate for the output file (default: 64k).')
    parser.add_argument('--speed', type=float, default=1.0, help='Playback speed factor (default: 1.0).')

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function
    convert_audio(args.input_file, args.output_file, args.volume, args.bitrate, args.speed)

if __name__ == '__main__':
    main()
