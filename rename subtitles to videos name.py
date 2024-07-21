import re
import os
import glob

def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return numbers

def rename_subtitles():
    video_files = glob.glob("*.mkv")  # Update with your video file extension
    subtitle_files = glob.glob("*.ass")  # Update with your subtitle file extension

    for video in video_files:
        video_name = os.path.splitext(video)[0]  # Get video filename without extension
        video_num = extract_numbers(video_name)[0]  # Extract number from video filename

        for sub in subtitle_files:
            sub_name = os.path.splitext(sub)[0]  # Get subtitle filename without extension
            sub_num = extract_numbers(sub_name)[0]  # Extract number from subtitle filename

            if sub_num == video_num:
                new_subtitle_name = video_name + os.path.splitext(sub)[1]
                os.rename(sub, new_subtitle_name)
                print(f"Renamed {sub} to {new_subtitle_name}")

rename_subtitles()
