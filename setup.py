import os
from setuptools import setup, Extension

# Library locator function
# Looks to see which library is available to link against
def check_lib_by_name(lib_name, search_path=None):
    s_path = ""
    if search_path:
        for path in search_path:
            s_path = s_path + "-L%s" % path
    return os.system('ld %s -l%s'% (s_path, lib_name)) == 0

def find_closest_libname(lib_names, search_path=None):
    for lib_name in lib_names:
        if check_lib_by_name(lib_name, search_path):
            return lib_name
    raise Exception("Cannot find Tesseract library via ld search. Confirm it is installed.")

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

extra_lib_paths = ['/usr/local/lib']

tesseract_possible_names = ['tesseract_api', 'tesseract']
tesseract_lib_name = find_closest_libname(tesseract_possible_names, extra_lib_paths)

tesser_cpp = Extension('libtesserwrap',
                    include_dirs = ['/usr/local/include'],
                    libraries = ['boost_python', tesseract_lib_name],
                    library_dirs = extra_lib_paths,
                    sources = ['tesserwrap/cpp/tesseract_wrap.cpp'],
                    depends = ['tesserwrap/cpp/tesseract_wrap.cpp',
                                'tesserwrap/css/tesseract_wrap.h'])

setup(
    name = "tesserwrap",
    version = "0.0.13",
    author = "Greg Jurman, and others",
    author_email = "gdj2214@rit.edu",
    description = ("Basic python bindings to the Tesseract C++ API"),
    license = "Apache License 2.0",
    keywords = "tesseract ocr cpp",
    url = "https://github.com/gregjurman/tesserwrap",
    packages = ['tesserwrap'],
    ext_modules = [tesser_cpp],
    long_description=read('README'),
    classifiers=[
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
    ],
)
