# ASCII letters (light to dark)
ASCII_CHARS = ['.', ',', '-', '+', '*', '?', '%', '#', '$', '@']
ASCII_LEN = len(ASCII_CHARS)

def generate_ascii(img):
    image_ascii = ''

    for row in img:
        for pixel in row:
            image_ascii += ASCII_CHARS[int((pixel / 255) * ASCII_LEN)]
        image_ascii += '\n'

    return image_ascii

def generate_ascii_alpha(img, alpha):
    image_ascii = ''

    for row, row_alpha in zip(img, alpha):
        for pixel, pixel_alpha in zip(row, row_alpha):
            if pixel_alpha < 64:
                image_ascii += ' '
            else:
                image_ascii += ASCII_CHARS[int((pixel / 255) * ASCII_LEN)]
        image_ascii += '\n'
    
    return image_ascii