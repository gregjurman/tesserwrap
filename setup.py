import os
from setuptools import setup, Extension

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

tesser_cpp = Extension('libtesserwrap',
                    include_dirs = ['/usr/local/include'],
                    libraries = ['boost_python', 'tesseract_api'],
                    library_dirs = ['/usr/local/lib'],
                    sources = ['tesserwrap/cpp/tesseract_wrap.cpp'],
                    depends = ['tesserwrap/cpp/tesseract_wrap.cpp',
                                'tesserwrap/css/tesseract_wrap.h'])

setup(
    name = "tesserwrap",
    version = "0.0.10",
    author = "Greg Jurman",
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
