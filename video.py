import cv2
import time
from image import image
from term import term_size, term_clear, term_clear_full
from genascii import generate_ascii

def video(source):
    try:
        capture = cv2.VideoCapture(source)

        if not capture.isOpened():
            raise FileNotFoundError(f"File not found: {source}")
        
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(capture.get(cv2.CAP_PROP_FPS))
        delay = int(1000 / fps)

        term_clear_full()

        frame_idx = 0
        while capture.isOpened():
            ret, frame = capture.read()

            if not ret:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            shape = [frame_height, frame_width]
            resize_width, resize_height = term_size(shape)

            frame_gray_resized = cv2.resize(frame_gray, (resize_width, resize_height))

            ascii_img = generate_ascii(frame_gray_resized)

            term_clear()
            print(ascii_img)

            frame_idx += 1

            if frame_idx == frame_count:
                print("End of video")
                break

            # time.sleep(delay / 3000)


        capture.release()


    except FileNotFoundError as e:
        print(e)
        exit()

    except Exception as e:
        print(f"An error occurred while processing the video: {e}")
        exit()
        