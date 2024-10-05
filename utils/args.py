import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Image/Video to ASCII converter')

    parser.add_argument('-p','--path', type=str, default=None, help='Path to the input image or video')
    parser.add_argument('-o', '--out', type=str, default=None, help='Output file name (without extension) ')
    parser.add_argument('-s', '--speed', type=int, default=5, choices=range(1, 11), help='Playback speed of the video (1-10, default=5 (smaller terminal font may cause video lag)')
    parser.add_argument('-i', '--invert', action='store_true', help='Invert the ASCII character set')

    return parser.parse_args()