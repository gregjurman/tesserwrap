import os
import unittest
from nose.tools import eq_, ok_, raises
from PIL import Image, ImageDraw, ImageFont

import tesserwrap
from util import tolerant

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def create_img(text="Quick brown fox", depth="L"):
    font = os.path.join(__location__, "FreeSansBold.ttf")
    fnt = ImageFont.truetype(font, 24)
    imgbg = Image.new(depth, (710, 40), "#FFFFFF")
    draw = ImageDraw.Draw(imgbg)
    draw.text((10, 0), text, font=fnt, fill="#000000")
    del draw
    return imgbg


class TestTesseract(unittest.TestCase):
    @tolerant()
    def test_ocr_image(self):
        test_text = "ABABABA"
        img = create_img(test_text)
        tr = tesserwrap.Tesseract()
        out_text = tr.ocr_image(img).strip()
        eq_(out_text, test_text,
            "%s is not %s" % (out_text, test_text))

    @tolerant()
    def test_ocr_image_RGB(self):
        test_text = "ABABABA"
        img = create_img(test_text, "RGB")
        tr = tesserwrap.Tesseract()
        out_text = tr.ocr_image(img).strip()
        eq_(out_text, test_text,
            "%s is not %s" % (out_text, test_text))

    @tolerant()
    def test_ocr_image_Whitelist(self):
        test_text = "ABABABA"
        img = create_img(test_text)
        tr = tesserwrap.Tesseract()
        tr.set_variable("tessedit_char_whitelist", "A")
        out_text = tr.ocr_image(img).strip()
        assert out_text != test_text, "%r == %r" % (out_text, test_text)

    @tolerant()
    def test_set_rectangle(self):
        test_text = "A BBB"
        img = create_img("A BBB  CCC")
        tr = tesserwrap.Tesseract()
        tr.set_image(img)
        tr.set_rectangle(0, 0, 100, 40)
        out_text = tr.get_text().decode().strip()
        eq_(out_text, test_text,
            "%s is not %s" % (out_text, test_text))

    def test_get_rectangle(self):
        test_text = "A BBB"
        img = create_img("A BBB  CCC")
        tr = tesserwrap.Tesseract()
        tr.set_image(img)
        tr.get_text()  # run recognizer to get all data set
        (l, t), (w, h) = tr.get_rectangle()
        eq_(l, 0, "Left attribute incorrect")
        eq_(t, 0, "Top attribute incorrect")
        eq_(w, 710, "Width attribute incorrect")
        eq_(h, 40, "Height attribute incorrect")

    def test_bad_handle(self):
        tr = tesserwrap.Tesseract()
        del tr.handle
        del tr

    def test_clear(self):
        tr = tesserwrap.Tesseract()
        img = create_img("A BBB  CCC")
        tr.set_image(img)
        tr.clear()

    def test_deprecator(self):
        tr = tesserwrap.tesseract()

    def test_mean_confidence(self):
        tr = tesserwrap.Tesseract()
        img = create_img("Hello World")
        tr.set_image(img)
        # Should be high number
        ok_(tr.get_mean_confidence() > 80)



