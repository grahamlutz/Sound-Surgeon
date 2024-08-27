import argparse
from utils.youtube_downloader import download_video
from output.sheet_music_generator import generate_sheet_music
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert YouTube video to piano sheet music or tablature.")
    parser.add_argument("-url", "--url", required=True, help="YouTube video URL (enclose in quotes)")
    parser.add_argument("-o", "--output", default="output", help="Output file name (without extension)")
    parser.add_argument("-f", "--format", choices=["sheet", "tab"], default="sheet", help="Output format: sheet music or tablature")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    print(f"Downloading video: {args.url}")
    video_path = download_video(args.url)
    
    if video_path is None:
        print("Failed to download the video. Exiting.")
        sys.exit(1)
    
    if args.format == "sheet":
        print(f"Generating sheet music: {args.output}.pdf")
        generate_sheet_music(video_path, f"{args.output}.pdf")
    else:
        print("Tablature generation not implemented yet.")
    
    print("Done!")

if __name__ == "__main__":
    main()