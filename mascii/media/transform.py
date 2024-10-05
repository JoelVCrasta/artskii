import cv2, sys
from utils.term import term_size, term_clear
from utils.genascii import generate_ascii, generate_ascii_alpha, use_char_set

class Transform():
    def __init__(self):
        self.media = None
        self.alpha_channel = None
        self.shape_resized = None
        self.ascii = ''

    def grayscale(self):
        if self.media.shape[2] == 4:
            self.media = cv2.cvtColor(self.media, cv2.COLOR_BGRA2GRAY)
        else:
            self.media = cv2.cvtColor(self.media, cv2.COLOR_BGR2GRAY)

    def alpha(self):
        if self.media.shape[2] == 4:
            self.alpha_channel = self.media[:, :, 3]

    def resize_shape(self):
        self.shape_resized = term_size(self.media.shape)

    def resize_shape_video(self, height, width):
        self.shape_resized = term_size((height, width))

    def resize(self):
        self.media = cv2.resize(
            self.media, 
            (self.shape_resized[0], self.shape_resized[1])
        )

        if self.alpha_channel is not None:
            self.alpha_channel = cv2.resize(
                self.alpha_channel, 
                (self.shape_resized[0], self.shape_resized[1])
            )

    def get_char_set(self, invert):
        if invert:
            use_char_set(1)
        else:
            use_char_set(0)

    def display_media(self, invert):
        term_clear()
        self.get_char_set(invert)

        if self.alpha_channel is None:
            self.ascii = generate_ascii(self.media)
        else:
            self.ascii = generate_ascii_alpha(self.media, self.alpha_channel)

        sys.stdout.write(self.ascii)
        sys.stdout.flush()

            