import cv2
from util import check_source
from image import image
from video import video

source = 'assets/bocchi.jpeg'

try:
    if check_source(source) == 0:
        image(source)
    elif check_source(source) == 1:
        video(source)
    else:
        print('Unsupported file type')
        exit()
except Exception as e:
    print(e)
    exit()