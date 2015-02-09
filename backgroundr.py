from PIL import Image, ImageFont, ImageDraw


def create_background(size, color):
    image = Image.new('RGB', size, color)
    return image


def add_text(image, font_path, size=32, x_cord=0, y_cord=0):
    font = ImageFont.truetype(font_path, size)
    draw = ImageDraw.Draw(image)
    draw.text((x_cord, y_cord), "Hello World", font=font)


def main():
    size = (1920, 1080)
    color = (100, 120, 200)
    location = '/Users/smg247/Backgroundr_Images/'
    name = 'out'
    extension = '.jpg'
    font_path = 'fonts/Open_Sans/OpenSans-Regular.ttf'

    image = create_background(size, color)
    add_text(image, font_path, 32, 100, 300)

    full_filename = location + name + extension
    image.save(full_filename)


main()