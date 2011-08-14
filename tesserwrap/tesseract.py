from libtesserwrap import Tesserwrap
import Image

class tesseract(Tesserwrap):
    def __init__(self):
        Tesserwrap.__init__(self)

    def set_image(self, image):
        '''
        Takes a PIL Image and loads it into Tesseract for further operations.
   
        Note: This function will automatically convert the image to Grayscale.
        '''
        if image is None:
             self.clear()
        else:
             if image.mode != "L":
                 image.convert("L")

             Tesserwrap.set_image(self, image.tostring(), # Image data
                 image.size[0], # Width
                 image.size[1]) # Height


    def ocr_image(self, image):
        '''
        Takes a PIL Image, sends it to Tesseract for processing and returns 
        a string based on the image's contents.
   
        Note: This function will automatically convert the image to Grayscale.
        '''
        if image.mode != "L":
            image.convert("L")

        return self.tesseract_rect(image.tostring(), # Image data
            1, # Byte per Pixel (greyscale)
            image.size[0], # Bytes per line
            0, # Left
            0, # Top
            image.size[0], # Width
            image.size[1]) # Height
