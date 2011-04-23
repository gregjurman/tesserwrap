#include <boost/python.hpp>
#include "tesseract_wrap.h"

using namespace boost::python;


BOOST_PYTHON_MODULE(libtesserwrap)
{
    enum_<PageSegMode>("page_seg_mode")
        .value("auto", PSM_AUTO)
        .value("single_column", PSM_SINGLE_COLUMN)
        .value("single_block", PSM_SINGLE_BLOCK)
        .value("single_line", PSM_SINGLE_LINE)
        .value("single_word", PSM_SINGLE_WORD)
        .value("single_char", PSM_SINGLE_CHAR)
        .value("count", PSM_COUNT);

    enum_<PILImageFormat>("imageformat")
        .value("l", L)
        .value("rgb", RGB)
        .value("rgba", RGBA); 

    class_<Tesserwrap>("Tesserwrap")
        .def("set_page_seg_mode", &Tesserwrap::SetPageSegMode)
        .def("get_page_seg_mode", &Tesserwrap::GetPageSegMode)
        .def("set_image", &Tesserwrap::SetImage)
        .def("clear", &Tesserwrap::Clear)
        .def("set_rectangle", &Tesserwrap::SetRectangle)
        .def("get_rectangle", &Tesserwrap::GetRectangle)
        .def("get_utf8_text", &Tesserwrap::GetUTF8Text)
        .def("tesseract_rect", &Tesserwrap::TesseractRect);
}
