from PIL import Image, ImageDraw, ImageFont
import numpy as np
'''
https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
https://pythoncircle.com/post/674/python-script-13-generating-ascii-code-from-image/

'''
class Ascii:
    def __init__(self, path, strings, font_width, font_height, background_color, font_size, foreground,type):
        self.path = path
        self.strings = strings
        self.font_width = font_width
        self.font_height = font_height
        self.background_color = background_color
        self.font_size = font_size
        self.foreground = foreground
        self.type=type

    def grayscale(self):
        img = Image.open(self.path)
        if self.type == 'R':
            img = img.split()[0]
            img.save('grayscale.jpg')
        elif self.type == "G":
            img = img.split()[1]
            img.save('grayscale.jpg')
        else:
            img = img.split()[2]
            img.save('grayscale.jpg')

        img = img.convert('L')
        img.save('grayscale.jpg')
        return img


    def create_fontimage(self):
        for i in self.strings:
            img = Image.new('L', (self.font_width, self.font_height), color=self.background_color)
            font = ImageFont.truetype('arial.ttf', self.font_size)
            draw = ImageDraw.Draw(img)
            draw.text((self.font_width//2, self.font_height//2), i, fill=self.foreground, font=font)
            img.save(str(self.strings.index(i)) + ".jpg")

    def create_ascii_simple(self):
        ascii_file = open('ascii.txt', 'w')

        # Load the grayscale image
        grayscale_img = Image.open('grayscale.jpg')
        width, height = grayscale_img.size

        # Get the width and height of each ASCII character
        char_width = self.font_width
        char_height = self.font_height

        # Convert each pixel of the grayscale image to ASCII characters
        ascii_repr = []
        for y in range(0, height, char_height):
            row = []
            for x in range(0, width, char_width):
                pixel_intensity = grayscale_img.getpixel((x, y))
                min_distance = float('inf')
                min_char = ''
                for char in self.strings:
                    char_intensity = self.strings.index(char) * (255 / (len(self.strings) - 1))
                    distance = abs(char_intensity - pixel_intensity)
                    if distance < min_distance:
                        min_distance = distance
                        min_char = char
                row.append(min_char)
            ascii_repr.append(row)

        # Print or further process the ASCII representation
        for row in ascii_repr:
            ascii_file.write(''.join(row) + '\n')
        ascii_file.close()

    def create_ascii_euclidean(self):
        img_euclidean = Image.open('grayscale.jpg')
        ascii_file_euclidean = open('ascii_euclidean.txt', 'w')
        width, height = img_euclidean.size
        font_width = 1  # Define font_width based on desired character width
        font_height = 1  # Define font_height based on desired character height
        ascii_euclidean = []
        for y in range(0, height, font_height):
            row = []
            for x in range(0, width, font_width):
                pixel_intensity = img_euclidean.getpixel((x, y))
                min_distance = float('inf')
                min_char = ''
                for char in self.strings:
                    char_intensity = self.strings.index(char) * (255 / (len(self.strings) - 1))
                    # euclidean distance
                    distance = np.linalg.norm(pixel_intensity - char_intensity)
                    if distance < min_distance:
                        min_distance = distance
                        min_char = char
                row.append(min_char)
            ascii_euclidean.append(row)

        for row in ascii_euclidean:
            ascii_file_euclidean.write(''.join(row) + '\n')
        ascii_file_euclidean.close()

'''

test = Ascii('test.jpg', strings)
test.grayscale()
test.create_ascii_euclidean()

test = Ascii('test.jpg',strings)
test.grayscale()
test.create_fontimage()
test.create_ascii_simple()
'''