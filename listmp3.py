import os
import argparse

def list_mp3_files(directory, output_file=None):
    # Get the absolute path for each .mp3 file in the given directory
    mp3_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.mp3')]

    if output_file:
        with open(output_file, 'w') as f:
            for mp3 in mp3_files:
                f.write(f"{mp3}\n")
    else:
        for mp3 in mp3_files:
            print(mp3)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List all .mp3 files in a directory.")
    parser.add_argument("directory", type=str, help="Directory to search for .mp3 files.")
    parser.add_argument("-o", "--output", type=str, help="Optional output file for saving the list.")
    args = parser.parse_args()

    list_mp3_files(args.directory, args.output)
