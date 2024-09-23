import cv2, time, sys
import logging
from term import term_size, term_clear, term_clear_full
from genascii import generate_ascii

logging.basicConfig(level=logging.INFO)

class Video:
    def __init__(self, source):
        self.source = source
        self.capture = None
        self.frame_count = None
        self.frame_width = None
        self.frame_height = None
        self.target_ms = None

    def load_video(self):
        self.capture = cv2.VideoCapture(self.source)

        if not self.capture.isOpened():
            raise FileNotFoundError(f"File not found: {self.source}")
        
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.capture.get(cv2.CAP_PROP_FPS))
        self.target_ms = 1 / fps

    def frame_timing(self, elapsed_time):
        remaining_time = self.target_ms - elapsed_time

        if remaining_time > 0:
            time.sleep(remaining_time)    

    def display_video(self):
        frame_idx = 0

        # Resize frame to fit terminal size
        shape = [self.frame_height, self.frame_width]
        resize_width, resize_height = term_size(shape)

        while self.capture.isOpened():
            start_time = time.time()

            ret, frame = self.capture.read()

            if not ret:
                break

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_gray_resized = cv2.resize(frame_gray, (resize_width, resize_height))

            ascii_img = generate_ascii(frame_gray_resized)
            term_clear()
            sys.stdout.write(ascii_img)
            sys.stdout.flush()

            frame_idx += 1
            if frame_idx == self.frame_count:
                break

            # Calculate frame timing
            elapsed_time = time.time() - start_time
            self.frame_timing(elapsed_time)

        self.capture.release()

    def process_video(self):
        try:
            self.load_video()
            term_clear_full()
            self.display_video()

        except FileNotFoundError as e:
            logging.error(e)
            exit()

        except Exception as e:
            logging.error(f"An error occurred while processing the video: {e}")
            exit()