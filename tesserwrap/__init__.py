from .core import tr
import ctypes

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
