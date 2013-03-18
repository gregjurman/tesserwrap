#include "tesseract_wrap.h"
#include <cstring>
#include <iostream>

TessBaseAPIExt::TessBaseAPIExt(void)
:picture(NULL){}

TessBaseAPIExt::~TessBaseAPIExt(void)
{
   if(picture) delete [] picture;
   this->End();
}

const char* TessBaseAPIExt::TesseractRect(string data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height)
{
   return super::TesseractRect((const unsigned char*)data.c_str(), bytes_per_pixel, bytes_per_line, 
                            left, top, width, height);

}

void TessBaseAPIExt::SetImage(string data, uint64_t w, uint64_t h)
{
   if(picture) delete [] picture;
   picture = new unsigned char[data.length()];
   std::memcpy(picture, (unsigned char*)data.c_str(), data.length());
   super::SetImage(picture, (int)w, (int)h, 1, (int)w);
   this->SetRectangle(0, 0, w, h);
}

string TessBaseAPIExt::GetUTF8Text(void)
{
   return string(super::GetUTF8Text());
}

void TessBaseAPIExt::GetRectangle(uint64_t **rect)
{
  (*rect) = new uint64_t[4];
  (*rect)[0] = this->rect_left_;
  (*rect)[1] = this->rect_top_;
  (*rect)[2] = this->rect_width_;
  (*rect)[3] = this->rect_height_;
}




TESSERWRAP_CAPI TessH Init_Tesserwrap(const char *datadir, const char *lang)
{
  TessH h = new TessBaseAPIExt();
  h->Init(datadir, lang);
  return (TessH) h;
}

TESSERWRAP_CAPI void Destroy_Tesserwrap(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  if (api) delete api;
}
