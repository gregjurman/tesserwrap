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

void Tesserwrap::SetImage(const unsigned char* data, int h, int w, int dpi)
{
   picture.w = w;
   picture.h = h;
   picture.d = 32;
   picture.xres = dpi;
   picture.yres = dpi;
   picture.data = (l_uint32*)data;

   pixEndianByteSwap(&picture);
} 
