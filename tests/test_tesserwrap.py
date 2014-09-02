import os
import unittest
from nose.tools import eq_, ok_, raises
from PIL import Image, ImageDraw, ImageFont

import tesserwrap
from util import tolerant


def create_img(text="Quick brown fox", depth="L"):
    font = "/usr/share/fonts/gnu-free/FreeSansBold.ttf"
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
        tr.get_text()  # run recognizer to get all data set
        ok_(tr.get_mean_confidence() >= 0, "Confidence should be positve integer")

    def test_word_confidences(self):
        tr = tesserwrap.Tesseract()
        img = create_img()
        tr.set_image(img)
        tr.get_text()  # run recognizer to get all data set
        res = tr.get_all_word_confidences()
        eq_(len(res), 3, "Each word should have one item in result")
        eq_(tr.get_mean_confidence(), sum(res)/len(res), "Mean confidence incorrect")
        # Empty image
        img = create_img("")
        tr.set_image(img)
        res2 = tr.get_all_word_confidences()
        eq_([], res2, "Should be empty result and no crash")


    def test_get_words(self):
        tr = tesserwrap.Tesseract()
        img = create_img()
        tr.set_image(img)
        tr.get_text()
        
        res = tr.get_words()
        eq_(len(res), 3, "Each word should have one item in result")
        item = res[0]
        eq_(item.value, 'Quick', "%s is not %s" % (item.value, 'Quick'))
        eq_(len(item.box), 4, 'Box does not contain 4 items')


    def test_get_symbols(self):
        tr = tesserwrap.Tesseract()
        test_text = 'ABCD'
        img = create_img(test_text)
        tr.set_image(img)
        tr.get_text()
        
        res = tr.get_symbols()
        result_text = ''.join([l.value for l in res])
        eq_(result_text, test_text, "%s is not %s" % (result_text, test_text))
