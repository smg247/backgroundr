from __future__ import print_function
import sys

from background_creation import create_background, add_text
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE, LOCATION


def main():
    if len(sys.argv) != 6 or sys.argv[1] == 'help':
        print('There are 5 necessary arguments to use the command line Backgroundr app:'
              'Red (0 - 255), Green (0 - 255), Blue (0 - 255), output image name, '
              'and the text to be placed on the image (in quotes).')
        return

    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    color = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    name = sys.argv[4]
    text = sys.argv[5]
    extension = '.jpg'
    # font_path = font_paths[FONT]

    image = create_background(size, color)
    add_text(image, text, FONT, FONT_SIZE)

    full_filename = LOCATION + name + extension
    image.save(full_filename)


main()
