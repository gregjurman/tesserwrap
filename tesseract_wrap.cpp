#include "tesseract_wrap.h"

// Tesserwrap - constructor
// Initializes the Tesseract Engine with a defined directory
// and defined language.
Tesserwrap::Tesserwrap(const char* datadir, const char* lang)
{
   api.Init(datadir, lang);
}

Tesserwrap::~Tesserwrap(void)
{
   api.End();
}

const char* Tesserwrap::TesseractRect(string data, 
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height)
{
   return api.TesseractRect((const unsigned char*)data.c_str(), bytes_per_pixel, bytes_per_line, 
                            left, top, width, height);

}

void Tesserwrap::SetImage(string data, int h, int w, int dpi)
{
   picture.w = w;
   picture.h = h;
   picture.d = 32;
   picture.xres = dpi;
   picture.yres = dpi;
   picture.data = (l_uint32*)data.c_str();

   pixEndianByteSwap(&picture);
   api.SetImage(&picture);
} 
