import cv2
from utils.source import check_source
from utils.args import get_args
from video import video
from image import Image

source = 'assets/bocchi.jpeg'


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
                Image = Image()
                Image.image()

            elif check_source(self.path) == 1:
                video(self.path, self.speed)
                
            else:
                raise Exception('Invalid path extension')
            
        except Exception as e:
            print(e)
            exit()

    def output(self):
        if self.out and check_source(self.path) == 0:
            with open(self.out, 'w') as f:
                f.write()

if __name__ == '__main__':
    main = Main()
    main.run()
    main.output()