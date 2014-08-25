from .core import tr
from ctypes import c_ulonglong, byref
from collections import namedtuple
import sys
import warnings


__all__ = ["PageSegMode", "PageIteratorLevel", "Tesseract"]


class PageSegMode(object):
    PSM_OSD_ONLY = 0
    PSM_AUTO_OSD = 1
    PSM_AUTO_ONLY = 2
    PSM_AUTO = 3
    PSM_SINGLE_COLUMN = 4
    PSM_SINGLE_BLOCK_VERT_TEXT = 5
    PSM_SINGLE_BLOCK = 6
    PSM_SINGLE_LINE = 7
    PSM_SINGLE_WORD = 8
    PSM_CIRCLE_WORD = 9
    PSM_SINGLE_CHAR = 10

class PageIteratorLevel(object):
    RIL_BLOCK = 0
    RIL_PARA = 1
    RIL_TEXTLINE = 2
    RIL_WORD = 3
    RIL_SYMBOL = 4


class Tesseract(object):
    """Tesseract OCR object.

    :param datadir:
        Tesseract data-directory with Tesseract training data.

    :param lang:
        The language of the image(s) to be OCRed.

    A simple example::

        >>> from tesserwrap import Tesseract
        >>> from PIL import Image

        >>> img = Image.open("test.png")
        >>> tr = Tesseract()
        >>> tr.ocr_image(img)
        'The quick brown fox jumps ove\\n\\n'
    """

    def __init__(self, datadir="", lang="eng"):
        """Initialize a new Tesseract object

        """
        self.handle = tr.Tesserwrap_Init(
            bytes(datadir, "ascii") if sys.version[:3] >= '3.2' else datadir,
            bytes(lang, "ascii") if sys.version[:3] >= '3.2' else lang
        )

    def __del__(self):
        try:
            if self.handle and core:
                tr.Tesserwrap_Destroy(self.handle)
                self.handle = None
        except AttributeError:
            print("__del__ without handle release")
            pass

    def set_image(self, image):
        '''Takes a PIL Image and loads it into Tesseract for further
        operations.

        Note:: This function will automatically convert the image to
        Grayscale.

        :param image: image
            Image to use in tesseract.
        '''
        if image.mode != "L":
            image = image.convert("L")

        if hasattr(image, "tobytes"):
            img_bytes = image.tobytes()
        else:
            img_bytes = image.tostring()
            
        tr.Tesserwrap_SetImage(
            self.handle,
            img_bytes,                  # Image data
            len(img_bytes),             # size of buffer
            image.size[0],              # Width
            image.size[1])              # Height

    def get_text(self):
        """Get the text of the OCR'd image as a byte-string
        """
        return tr.Tesserwrap_GetUTF8Text(self.handle)

    def get_utf8_text(self):
        """Get the text of the OCR'd image as a string.

        This function is kept for backwards compatability with the 0.0
        version of tesserwrap.
        """
        return self.get_text().decode(encoding="UTF-8")

    def ocr_image(self, image):
        """OCR an image returning the UTF8 text data.

        :param image: image
            Image to be OCR'd by tesseract.
        """
        self.set_image(image)
        self.set_page_seg_mode(PageSegMode.PSM_SINGLE_BLOCK)
        return self.get_utf8_text()

    def get_rectangle(self):
        """Get the bounding rectangle that tesseract is looking at inside
        of the image.
        """
        left, top = c_ulonglong(), c_ulonglong()
        width, height = c_ulonglong(), c_ulonglong()
        tr.Tesserwrap_GetRectangle(
            self.handle,
            byref(left), byref(top),
            byref(width), byref(height))
        return ((left.value, top.value), (width.value, height.value))

    def set_rectangle(self, left, top, width, height):
        """Set the OCR detection bounding-box.

        :param left: integer
            Pixels offset right from left of the image.

        :param top: integer
            Pixels offset down from the top of the image.

        :param width: integer
            Width of the bounding-box.

        :param height: integer
            Height of the bounding-box.
        """
        tr.Tesserwrap_SetRectangle(
            self.handle,
            left, top,
            width, height)

    def get_page_seg_mode(self):
        """Returns the page analysis mode from Tesseract"""
        return tr.Tesserwrap_GetPageSegMode(self.handle)

    def set_page_seg_mode(self, mode=PageSegMode.PSM_SINGLE_BLOCK):
        """Set the page layout analysis mode.

        :param mode: integer
            The page layout analysis mode. See PageSegMode class for options
        """
        tr.Tesserwrap_SetPageSegMode(self.handle, mode)

    def clear(self):
        """Clear the tesseract Image, and clean up any Tesseract run-data."""
        tr.Tesserwrap_Clear(self.handle)

    def set_variable(self, key, value):
        """Set an internal Tesseract variable.

        :param key: str
            Variable name to change.

        :param value: str
            New variable value.

        """
        tr.Tesserwrap_SetVariable(
            self.handle,
            bytes(key, "ascii") if sys.version[:3] >= '3.2' else key,
            bytes(value, "ascii") if sys.version[:3] >= '3.2' else value
        )

    def get_mean_confidence(self):
        """Returns the (average) confidence value between 0 and 100. 
        """
        return tr.Tesserwrap_MeanTextConf(self.handle)

    def get_all_word_confidences(self):
        node = tr.Tesserwrap_AllWordConfidences(self.handle)
        result = []
        
        while bool(node):
            result.append(node.contents.value)
            node = node.contents.next

        return result

    def get_result(self, level):
        node = tr.Tesserwrap_GetResult(self.handle, level)
        result = []
        Item = namedtuple('Item', ['value', 'confidence', 'box'])

        while bool(node):
            item = Item(
                value=node.contents.value,
                confidence=node.contents.confidence,
                box = tuple(node.contents.box)
            )
            result.append(item)
            node = node.contents.next

        return result

    def get_words(self):
        """Get a list containing all the words in the OCR'd image.
        :returns: A list containing objects with the attributes:
            value: the string value of the word
            box: left, upper, right, and lower pixel coordinate
            confidence: confidence value between 0 and 100 
        """        
        return self.get_result(PageIteratorLevel.RIL_WORD)

    def get_symbols(self):
        """Get a list containing all symbols in the OCR'd image.
        :returns: A list containing objects with the attributes:
            value: the string value of the symbol
            box: left, upper, right, and lower pixel coordinate
            confidence: confidence value between 0 and 100 
        """                
        return self.get_result(PageIteratorLevel.RIL_SYMBOL)

    def get_textlines(self):
        """Get a list containing all lines in the OCR'd image.
        :returns: A list containing objects with the attributes:
            value: the string value of the line
            box: left, upper, right, and lower pixel coordinate
            confidence: confidence value between 0 and 100 
        """        
        return self.get_result(PageIteratorLevel.RIL_TEXTLINE)




def tesseract(*args, **kwargs):
    """When the lower-case version of tesseract is called, spit out a
        DeprecationWarning and create the new class object.
    """
    warnings.warn(
        "Soon 'tesseract' will be deprecated, use Tesseract instead",
        DeprecationWarning, stacklevel=2)
    return Tesseract(*args, **kwargs)
