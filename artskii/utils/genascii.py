CHAR_SETS = {
    0: ['.', ':', '-', '+', '*', '?', '#', '%', '$', '@'],
    1: ['@', '$', '%', '#', '?', '*', '+', '-', ':', '.']
}
ascii_chars = []
ascii_len = 0

def use_char_set(idx: int):
    global ascii_chars, ascii_len

    ascii_chars = CHAR_SETS[idx]
    ascii_len = len(ascii_chars)


def generate_ascii(img) -> str:
    image_ascii = ''

    for row in img:
        for pixel in row:
            image_ascii += ascii_chars[int((pixel / 255) * ascii_len)]
        image_ascii += '\n'

    return image_ascii

def generate_ascii_alpha(img, alpha) -> str:
    image_ascii = ''

    for row, row_alpha in zip(img, alpha):
        for pixel, pixel_alpha in zip(row, row_alpha):
            if pixel_alpha < 64:
                image_ascii += ' '
            else:
                image_ascii += ascii_chars[int((pixel / 255) * ascii_len)]
        image_ascii += '\n'
    
    return image_ascii