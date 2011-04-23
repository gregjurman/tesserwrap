from libtesserwrap import *
import Image

class Tesseract(Tesserwrap):
    def __init__(self):
        Tesserwrap.__init__(self)

    def set_image(self, image):
        if image is None:
             self.clear()
        else:
             if image.mode != "L":
                 image.convert("L")

             Tesserwrap.set_image(self, image.tostring(), # Image data passed as string
                 image.size[0], # Width
                 image.size[1]) # Height


    def ocr_image(self, image):
        if image.mode != "L":
            image.convert("L")

        self.tesseract_rect(image.tostring(), # Image data passed as string
            1, # Byte per Pixel (greyscale)
            image.size[0], # Bytes per line
            0, # Left
            0, # Top
            image.size[0], # Width
            image.size[1]) # Height
