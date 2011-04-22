# Makefile for Boost.Python component
.PHONY:all install
install: libtesseract_wrap.so tesserwrap.so
	cp libtesseract_wrap.so tesserwrap.so ..
clean:
	rm -f *.so *.o

all: libtesseract_wrap.so tesserwrap.so

boost_cflags = -Wall -ftemplate-depth-100 -DBOOST_PYTHON_DYNAMIC_LIB \
               -isystem /usr/include/python2.7 -I.
boost_libs = -Wl,-rpath-link,. -L/usr/lib/python2.7/config \
               -lboost_python -llept -ltesseract_api
world_libs = -L. -Wl,-R. -ltesseract_wrap

libtesseract_wrap.so:libtesseract_wrap.o
	g++ -Wl,-rpath-link,/usr/local/lib -shared -L/usr/local/lib libtesseract_wrap.o -ltesseract_api -llept -fpic -o libtesseract_wrap.so
libtesseract_wrap.o:tesseract_wrap.cpp tesseract_wrap.h
	g++ -c -Wl,-rpath-link,/usr/local/lib -L/usr/local/lib -ltesseract_api -llept -fpic -o libtesseract_wrap.o tesseract_wrap.cpp

tesserwrap.o:tesserwrap.cpp
	g++ -c $(boost_cflags) -fpic tesserwrap.cpp
tesserwrap.so:tesserwrap.o
	g++ -o tesserwrap.so -module -shared $(boost_libs) $(world_libs) tesserwrap.o

