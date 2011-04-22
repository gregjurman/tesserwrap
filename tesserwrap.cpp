#include <boost/python.hpp>
#include "tesseract_wrap.h"

using namespace boost::python;


BOOST_PYTHON_MODULE(tesserwrap)
{
    enum_<PageSegMode>("pagesegmode")
        .value("auto", PSM_AUTO)
        .value("singlecolumn", PSM_SINGLE_COLUMN)
        .value("singleblock", PSM_SINGLE_BLOCK)
        .value("singleline", PSM_SINGLE_LINE)
        .value("singleword", PSM_SINGLE_WORD)
        .value("singlechar", PSM_SINGLE_CHAR)
        .value("count", PSM_COUNT);
  
    class_<Tesserwrap>("Tesserwrap")
        .def("setpagesegmode", &Tesserwrap::SetPageSegMode)
        .def("getpagesegmode", &Tesserwrap::GetPageSegMode)
        .def("setimage", &Tesserwrap::SetImage)
        .def("tesseractrect", &Tesserwrap::TesseractRect);
}
