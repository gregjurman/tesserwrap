#include "tesseract_wrap.h"
#include <cstring>
#include <iostream>

// Tesserwrap - constructor
// Initializes the Tesseract Engine with a defined directory
// and defined language.
Tesserwrap::Tesserwrap(const char* datadir, const char* lang)
:picture(NULL)
{
   api.Init(datadir, lang);
}

Tesserwrap::~Tesserwrap(void)
{
   if(picture) delete [] picture;
   api.End();
}

const char* Tesserwrap::TesseractRect(string data, 
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height)
{
   return api.TesseractRect((const unsigned char*)data.c_str(), bytes_per_pixel, bytes_per_line, 
                            left, top, width, height);

}

PageSegMode Tesserwrap::GetPageSegMode(void)
{
   return api.GetPageSegMode();
}

void Tesserwrap::SetPageSegMode(PageSegMode mode)
{
   api.SetPageSegMode(mode);
}

void Tesserwrap::SetImage(string data, int w, int h)
{
   if(picture) delete [] picture;
   picture = new unsigned char[data.length()];
      
   std::memcpy(picture, (unsigned char*)data.c_str(), data.length());
   api.SetImage(picture, w, h, 1, w);
   api.SetRectangle(0,0, w, h);
} 

void Tesserwrap::Clear(void)
{
   api.Clear();
}
void Tesserwrap::SetRectangle(int left, int top, int w, int h)
{
   api.SetRectangle(left, top, w, h);
}

string Tesserwrap::GetUTF8Text(void)
{
   return string(api.GetUTF8Text());
}

tuple Tesserwrap::GetRectangle(void)
{
   return make_tuple(make_tuple(api.Get_Rect_Left(), api.Get_Rect_Top()), 
                     make_tuple(api.Get_Rect_Width(), api.Get_Rect_Height()));
}


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

