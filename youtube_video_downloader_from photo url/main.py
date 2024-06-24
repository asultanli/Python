import pytesseract
from PIL import Image
from pytube import YouTube
import re


def extract_youtube_url(text):
    """
    Extracts YouTube URLs from a given text using regular expressions.
    """
    # This regex pattern is designed to match typical YouTube URLs
    pattern = r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s]+)'
    urls = re.findall(pattern, text)
    # Assuming the first YouTube URL found is the one we want
    return urls[0] if urls else None


img = Image.open('img.png')
text = pytesseract.image_to_string(img)

# Extract URL from the OCR text
youtube_url = extract_youtube_url(text)

if youtube_url:
    try:
        yt = YouTube(youtube_url)
        print("Title:", yt.title)
        print("Views: ", yt.views)

        resolution = "720p"
        print('Downloading...')
        yd = yt.streams.filter(res=resolution, file_extension='mp4').first()

        if yd:
            output_dir = r'/Users/sultanliaykhan/Desktop/youtube_video_downloader_from photo url/'
            yd.download(output_dir)
            print('Download Complete!')
        else:
            print(f"No videos found with resolution {resolution}.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No YouTube URL could be extracted from the image.")
