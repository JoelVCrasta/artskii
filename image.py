import cv2
from term import term_size, term_clear
from genascii import generate_ascii, generate_ascii_alpha


def image(source):
    image = cv2.imread(source, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise FileNotFoundError

    """
    * Check if image has alpha channel
    * Convert image to grayscale
    """
    if image.shape[2] == 4:
        alpha_channel = image[:, :, 3]
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    else:
        alpha_channel = None
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Resize image
    resize_width, resize_height = term_size(image_gray.shape)
    image_gray_resized = cv2.resize(image_gray, (resize_width, resize_height))

    if alpha_channel is not None:
        alpha_channel_resized = cv2.resize(alpha_channel, (resize_width, resize_height))

    # Add alpha channel to resized image
    if alpha_channel is None:
        ascii_img = generate_ascii(image_gray_resized)
    else:
        ascii_img = generate_ascii_alpha(image_gray_resized, alpha_channel_resized)

    term_clear()
    print(ascii_img)