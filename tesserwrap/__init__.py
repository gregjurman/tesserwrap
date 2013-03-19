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
