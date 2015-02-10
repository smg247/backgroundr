import sys
from backgroundr import create_background, add_text

def main():
    if len(sys.argv) != 8 or sys.argv[0] == 'help':
        print('There are 7 necessary arguments to use the command line Backgroundr app:'
              ' Width, Height, Red (0, 255), Green (0, 255), Blue (0, 255), output image name, '
              'and the text to be placed on the image (in quotes).')
        return

    size = (int(sys.argv[1]), int(sys.argv[2]))
    color = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    name = sys.argv[6]
    text = sys.argv[7]
    location = '/Users/smg247/Backgroundr_Images/'
    extension = '.jpg'
    font_path = 'fonts/Open_Sans/OpenSans-Regular.ttf'

    image = create_background(size, color)
    add_text(image, text, font_path, 64)

    full_filename = location + name + extension
    image.save(full_filename)


main()