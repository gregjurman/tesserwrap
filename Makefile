# Makefile for Boost.Python component
.PHONY:all install
install: libworld.so hello.so
	cp libworld.so hello.so ..
clean:
	rm -f *.so *.o

all: libworld.so hello.so

boost_cflags = -Wall -ftemplate-depth-100 -DBOOST_PYTHON_DYNAMIC_LIB \
               -isystem /usr/include/python2.7 -I.
boost_libs = -Wl,-rpath-link,. -L/usr/lib/python2.4/config -lboost_python
world_libs = -L. -Wl,-R. -lworld

libworld.so:world.o
	g++ -shared world.o -ltesseract_api -fpic -o libworld.so
world.o:world.cpp world.h
	g++ -c -Wall -ltesseract_api -fpic world.cpp

hello.o:hello.cpp
	g++ -c $(boost_cflags) -fpic hello.cpp
hello.so:hello.o
	g++ -o hello.so -module -shared $(boost_libs) $(world_libs) hello.o

