import cv2, time, sys
import logging
from utils.term import term_clear
from .transform import Transform

logging.basicConfig(level=logging.INFO)

class Video(Transform):
    def __init__(self, path, speed, invert):
        super().__init__()
        self.path = path
        self.speed = speed
        self.invert = invert
        self.video = None
        self.height = None
        self.width = None
        self.frame_count = 0
        self.timing = 0

    def load_video(self):
        self.video = cv2.VideoCapture(self.path)

        if not self.video.isOpened():
            raise FileNotFoundError(f"File not found: {self.path}")
        
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.frame_count = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = self.video.get(cv2.CAP_PROP_FPS)
        self.timing = (1 / fps) * (5 / self.speed)

    def timing_fps(self, elapsed_time):
        remaining_time = self.timing - elapsed_time

        if remaining_time > 0:
            time.sleep(remaining_time)  

    def process_video(self):
        try:
            self.load_video()
            self.resize_shape_video(self.height, self.width)

            frame_idx = 0
            while self.video.isOpened():
                start_time = time.time()

                ret, frame = self.video.read()
                if not ret:
                    break

                self.media = frame
                self.resize()
                self.grayscale()
                self.display_media(self.invert)

                if frame_idx == self.frame_count - 1:
                    term_clear()
                    break
                frame_idx += 1

                elapsed_time = time.time() - start_time
                self.timing_fps(elapsed_time)
            
            self.video.release()

        except FileNotFoundError as e:
            logging.error(e)
            sys.exit(1)

        except Exception as e:
            logging.error(e)
            sys.exit(1)



    