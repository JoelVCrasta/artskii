import logging, sys
from utils.source import check_source
from utils.args import get_args
from media.video import Video
from media.image import Image

logging.basicConfig(level=logging.INFO)
class Main:
    def __init__(self):
        self.args = get_args()
        self.path = self.args.path
        self.speed = self.args.speed
        self.invert = self.args.invert
        self.out = self.args.out
        self.ascii = ''

    def run(self):
        if self.args.out:
            print(f"Outputting to {self.out}.txt")
            return

        try: 
            if check_source(self.path) == 0:
                img = Image(self.path, self.invert)
                self.ascii = img.process_image()

            elif check_source(self.path) == 1:
                vid = Video(self.path, self.speed, self.invert)
                vid.process_video()
                
            else:
                raise Exception('Invalid path extension')
            
        except Exception as e:
            logging.error(e)
            sys.exit(1)

    def output(self):
        if self.args.out:
            try:
                if check_source(self.path) == 0:
                    with open(self.out+".txt", 'w') as f:
                        f.write(self.ascii)

                if check_source(self.path) == 1:
                    logging.info("Video output is not supported yet")
            
            except Exception as e:
                logging.error(e)
                sys.exit(1)

def main():
    main = Main()
    main.run()
    main.output()

if __name__ == '__main__':
    main()