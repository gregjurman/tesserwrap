#include <tesseract/baseapi.h>
#include <string>
#include <stdint.h>

using namespace tesseract;
using namespace std;

#if defined(USE_GCC_VISIBILITY_FLAG)
#    define TESSERWRAP_CAPI __attribute__ ((visibility("default")))
#  else
#    define TESSERWRAP_CAPI
#  endif


enum PILImageFormat
{
L = 0, RGB=3, RGBA=4
};

class TessBaseAPIExt : public TessBaseAPI
{
    private:
    unsigned char *picture;
    typedef TessBaseAPI super;

    public:
    TessBaseAPIExt(void);
    ~TessBaseAPIExt(void); // Default destructor
    const char* TesseractRect(string data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height);
    void GetRectangle(uint64_t **);
    void SetImage(string data, uint64_t w, uint64_t h);
    string GetUTF8Text(void);
};

typedef TessBaseAPIExt *TessH;

