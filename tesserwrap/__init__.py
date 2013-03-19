from .core import tr, PageSegMode
from ctypes import c_ulonglong, byref
import warnings

__all__ = ["Tesseract"]


class Tesseract(object):
    def __init__(self, datadir="", lang="eng"):
        self.handle = tr.Tesserwrap_Init(
            bytes(datadir, "ascii"),
            bytes(lang, "ascii"))

    def __del__(self):
        try:
            if self.handle and core:
                try:
                    tr
                except AttributeError:
                    # dll isn't active for some reason..
                    return
                tr.Tesserwrap_Destroy(self.handle)
                self.handle = None
        except AttributeError:
            print("__del__ without handle release")
            pass

    def set_image(self, image):
        '''
        Takes a PIL Image and loads it into Tesseract for further operations.
        Note: This function will automatically convert the image to Grayscale.
        '''
        if image.mode != "L":
            image = image.convert("L")

        img_bytes = image.tostring()
        tr.Tesserwrap_SetImage(
            self.handle,
            img_bytes,                  # Image data
            len(img_bytes),             # size of buffer
            image.size[0],              # Width
            image.size[1])              # Height

    def get_text(self):
        return tr.Tesserwrap_GetUTF8Text(self.handle)

    def get_utf8_text(self):
        return self.get_text().decode()

    def ocr_image(self, image):
        self.set_image(image)
        return self.get_utf8_text()

    def get_rectangle(self):
        left, top = c_ulonglong(), c_ulonglong()
        width, height = c_ulonglong(), c_ulonglong()
        tr.Tesserwrap_GetRectangle(
            self.handle,
            byref(left), byref(top),
            byref(width), byref(height))
        return (left.value, top.value, width.value, height.value)

    def set_rectangle(self, left, top, width, height):
        tr.Tesserwrap_SetRectangle(
            self.handle,
            left, top,
            width, height)

    def get_page_seg_mode(self):
        return tr.Tesserwrap_GetPageSegMode(self.handle)

    def set_page_seg_mode(self, mode=PageSegMode.PSM_SINGLE_BLOCK):
        tr.Tesserwrap_SetPageSegMode(self.handle, mode)

    def clear(self):
        tr.Tesserwrap_Clear(self.handle)


def deprecate_warning(cls):
    def _deprecate(*args, **kwargs):
        warnings.warn(
            "Soon 'tesseract' will be deprecated, use Tesseract instead",
            DeprecationWarning, stacklevel=2)
        return cls(*args, **kwargs)
    return _deprecate


tesseract = deprecate_warning(Tesseract)
