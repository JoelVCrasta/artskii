import cv2, logging
from utils.source import check_source
from utils.args import get_args
# from video import video
from image import Image

source = 'assets/bocchi.jpeg'

logging.basicConfig(level=logging.INFO)
class Main:
    def __init__(self):
        self.args = get_args()
        self.path = self.args.path
        self.out = self.args.out
        self.speed = self.args.speed

        self.ascii = None

    def run(self):
        try: 
            if check_source(self.path) == 0:
                image = Image(self.path)
                self.ascii = image.process_image()

            elif check_source(self.path) == 1:
                pass

            else:
                raise Exception('Invalid path extension')
            
        except Exception as e:
            print(e)
            exit()

    def output(self):
        if self.out and check_source(self.path) == 0:
            try:
                with open(self.out, 'w') as f:
                    f.write(self.ascii)
            except Exception as e:
                logging.error(e)

if __name__ == '__main__':
    main = Main()
    main.run()
    main.output()