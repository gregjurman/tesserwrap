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

PageSegMode Tesserwrap::GetPageSegMode(void)
{
   return api.GetPageSegMode();
}

void Tesserwrap::SetPageSegMode(PageSegMode mode)
{
   api.SetPageSegMode(mode);
}

void Tesserwrap::SetImage(string data, PILImageFormat iformat, int h, int w)
{
   switch(iformat)
   {
      case PILImageFormat.L:
         api.SetImage((const unsigned char*)data.c_str(), w, h, 1, w);
         break;
      case PILImageFormat.RGB:
         api.SetImage((const unsigned char*)data.c_str(), w, h, 3, w*3);
      case default:
         break;
   }
} 

void Tesserwrap::SetRectangle(int left, int top, int w, int h)
{
   api.SetRectangle(left, top, w, h)
} 
