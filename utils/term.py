import shutil, sys

def term_size(shape):
    height_scale = 2
    terminal_columns, terminal_rows = shutil.get_terminal_size()

    terminal_aspect_ratio = terminal_columns / terminal_rows
    image_aspect_ratio = shape[1] / shape[0]

    # Scale factor 
    if terminal_aspect_ratio > image_aspect_ratio:
        scaling_factor = terminal_rows * height_scale / shape[0]
    else:
        scaling_factor = terminal_columns / shape[1]

    new_width = int(shape[1] * scaling_factor)
    new_height = int(shape[0] * scaling_factor / height_scale) - 2

    return new_width, new_height

def term_clear():
    sys.stdout.write("\033[H")
    sys.stdout.flush()

    
