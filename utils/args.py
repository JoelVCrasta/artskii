import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Image/Video to ASCII converter')

    parser.add_argument('-p','--path', type=str, default=None, help='Path to the input image or video')
    parser.add_argument('-o', '--out', type=str, default=None, help='Path to the output text file')
    parser.add_argument('-s', '--speed', type=int, default=5, help='Playback speed of the video (1-10, default=5)')

    return parser.parse_args()