import cv2
import os

def check_source(source):
    image_ext = ['.jpeg', '.jpg', '.png', '.bmp', '.webp', '.tiff']
    video_ext = ['.mp4', '.avi', '.mov', '.mkv', '.webm']

    _, ext = os.path.splitext(source)
    ext = ext.lower()

    if ext in image_ext:
        return 0
    elif ext in video_ext:
        return 1
    else:
        return -1