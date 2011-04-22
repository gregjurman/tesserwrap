#include <boost/python.hpp>
#include "tesseract_wrap.h"

using namespace boost::python;


BOOST_PYTHON_MODULE(tesserwrap)
{
    class_<Tesserwrap>("Tesserwrap")
    .def("setimage", &Tesserwrap::SetImage)
    .def("tesseractrect", &Tesserwrap::TesseractRect)
    ;
}
