import cv2, sys
import logging
from transform import Transform

logging.basicConfig(level=logging.INFO)

class Image(Transform):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def load_image(self):
        self.media = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)

        if self.media is None:
            raise FileNotFoundError(f"File not found: {self.path}")
        
    def process_image(self) -> str:
        try:
            self.load_image()
            self.alpha()
            self.resize()
            self.grayscale()
            self.display_media()
            return self.ascii
        
        except FileNotFoundError as e:
            logging.error(e)
            sys.exit(1)

        except Exception as e:
            logging.error(e)
            sys.exit(1)



