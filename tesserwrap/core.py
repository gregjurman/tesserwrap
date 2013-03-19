import os
import sys
from ctypes import *
from ctypes.util import find_library

import distutils


def get_shared_lib_extension(is_python_ext=False):
    """Return the correct file extension for shared libraries.

    Parameters
    ----------
    is_python_ext : bool, optional
        Whether the shared library is a Python extension.  Default is False.

    Returns
    -------
    so_ext : str
        The shared library extension.

    Notes
    -----
    For Python shared libs, `so_ext` will typically be '.so' on Linux and OS X,
    and '.pyd' on Windows.  For Python >= 3.2 `so_ext` has a tag prepended on
    POSIX systems according to PEP 3149.  For Python 3.2 this is implemented on
    Linux, but not on OS X.

    """
    so_ext = distutils.sysconfig.get_config_var('SO') or ''
    # fix long extension for Python >=3.2, see PEP 3149.
    if not is_python_ext and 'SOABI' in distutils.sysconfig.get_config_vars():
        # Does nothing unless SOABI config var exists
        so_ext = so_ext.replace(
            '.' + distutils.sysconfig.get_config_var('SOABI'), '', 1)

    return so_ext


def load_library(libname, loader_path):
    """Load a DLL via ctypes load function. Return None on failure.

    Try loading the DLL from the current package directory first,
    then from the Windows DLL search path.

    """
    so_ext = get_shared_lib_extension()
    libname_ext = [libname + so_ext]
    if sys.version[:3] >= '3.2':
        # For Python >= 3.2 a tag may be added to lib extension
        # (platform dependent).  If we find such a tag, try both with
        # and without it.
        so_ext2 = get_shared_lib_extension(is_python_ext=True)
        if not so_ext2 == so_ext:
            libname_ext.insert(0, libname + so_ext2)

        loader_path = os.path.abspath(loader_path)
        if not os.path.isdir(loader_path):
            libdir = os.path.dirname(loader_path)
        else:
            libdir = loader_path

        # HACK
        libdir = os.path.abspath(libdir + "/..")

        # Need to save exception when using Python 3k, see PEP 3110.
        exc = None
        for ln in libname_ext:
            try:
                libpath = os.path.join(libdir, ln)
                return cdll[libpath]
            except OSError as e:
                exc = e
        raise exc


tr = load_library('libtesserwrap', os.path.dirname(__file__))


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


tr.Tesserwrap_Init.restype = c_void_p
tr.Tesserwrap_Init.argtypes = [c_char_p, c_char_p]

tr.Tesserwrap_Destroy.argtypes = [c_void_p]
tr.Tesserwrap_Destroy.restype = None

tr.Tesserwrap_GetRectangle.restype = None
tr.Tesserwrap_GetRectangle.argtypes = [
    c_void_p,
    POINTER(c_ulonglong), POINTER(c_ulonglong),
    POINTER(c_ulonglong), POINTER(c_ulonglong)
]

tr.Tesserwrap_SetRectangle.restype = None
tr.Tesserwrap_SetRectangle.argtypes = [
    c_void_p,
    c_ulonglong, c_ulonglong,
    c_ulonglong, c_ulonglong
]

tr.Tesserwrap_SetImage.restype = None
tr.Tesserwrap_SetImage.argtypes = [
    c_void_p,
    c_char_p,
    c_ulonglong, c_longlong, c_longlong
]

tr.Tesserwrap_GetUTF8Text.restype = c_char_p
tr.Tesserwrap_GetUTF8Text.argtypes = [c_void_p]

tr.Tesserwrap_GetPageSegMode.restype = c_int
tr.Tesserwrap_GetPageSegMode.argtypes = [c_void_p]

tr.Tesserwrap_SetPageSegMode.restype = None
tr.Tesserwrap_SetPageSegMode.argtypes = [c_void_p, c_int]

tr.Tesserwrap_Clear.restype = None
tr.Tesserwrap_Clear.argtypes = [c_void_p]
