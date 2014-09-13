#include "tesseract_ext.h"

TessBaseAPIExt::TessBaseAPIExt(void)
:picture(NULL){}

TessBaseAPIExt::~TessBaseAPIExt(void)
{
   if(picture) delete [] picture;
   this->End();
}

const char* TessBaseAPIExt::TesseractRect(const unsigned char *data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height)
{
   return super::TesseractRect(data, bytes_per_pixel, bytes_per_line, 
                            left, top, width, height);

}

void TessBaseAPIExt::SetImage(const unsigned char *data, uint64_t size, 
    uint64_t width, uint64_t height)
{
   if(picture) delete [] picture;
   picture = new unsigned char[size];
   std::memcpy(picture, data, size);
   super::SetImage(picture, width, height, 1, width);
   this->SetRectangle(0, 0, width, height);
}

void TessBaseAPIExt::GetRectangle(uint64_t *left, uint64_t *top, uint64_t *width, uint64_t *height)
{
  (*left) = this->rect_left_;
  (*top) = this->rect_top_;
  (*width) = this->rect_width_;
  (*height) = this->rect_height_;
}