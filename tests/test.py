import os
import unittest
from PIL import Image, ImageDraw, ImageFont
from itertools import takewhile

import tesserwrap
from util import tolerant

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def create_img(text="Quick brown fox jumps", depth="L"):
    font = os.path.join(__location__, "FreeSansBold.ttf")
    fnt = ImageFont.truetype(font, 24)
    imgbg = Image.new(depth, (710, 40), "#FFFFFF")
    draw = ImageDraw.Draw(imgbg)
    draw.text((10, 0), text, font=fnt, fill="#000000")
    draw.text((20, 0), text, font=fnt, fill="#000000")
    del draw
    return imgbg

tr = tesserwrap.Tesseract()
img = create_img("The quick brown fox jumps over the")
tr.set_image(img)
print tr.get_rectangle()

print tr.get_text()

print tr.get_all_word_confidences()
#print tr.get_symbols()


