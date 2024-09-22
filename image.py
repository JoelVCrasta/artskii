import cv2, sys
import logging
from term import term_size, term_clear_full
from genascii import generate_ascii, generate_ascii_alpha

logging.basicConfig(level=logging.INFO)

class Image:
    def __init__(self, path):
        self.path = path
        self.image = None
        self.image_gray = None
        self.alpha_channel = None
        self.image_gray_resized = None
        self.alpha_channel_resized = None
        self.ascii = None

    def load_image(self):
        self.image = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)

        if self.image is None:
            raise FileNotFoundError(f"File not found: {self.path}")

    def check_alpha_channel(self):
        if self.image.shape[2] == 4:
            self.alpha_channel = self.image[:, :, 3]
            self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGRA2GRAY)
        else:
            self.alpha_channel = None
            self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def resize_image(self):
        resize_width, resize_height = term_size(self.image_gray.shape)
        self.image_gray_resized = cv2.resize(self.image_gray, (resize_width, resize_height))

        if self.alpha_channel is not None:
            self.alpha_channel_resized = cv2.resize(self.alpha_channel, (resize_width, resize_height))

    def display_image(self):
        term_clear_full()
        if self.alpha_channel is not None:
            ascii_image = generate_ascii_alpha(self.image_gray_resized, self.alpha_channel_resized)
        else:
            ascii_image = generate_ascii(self.image_gray_resized)

        sys.stdout.write(ascii_image)
        sys.stdout.flush()

        self.ascii = ascii_image

    def process_image(self) -> str:
        try:
            self.load_image()
            self.check_alpha_channel()
            self.resize_image()
            self.display_image()

            return self.ascii

        except FileNotFoundError as e:
            logging.error(e)
            exit()

        except Exception as e:
            logging.error(f"Something went wrong:\n{e}")
            exit()
