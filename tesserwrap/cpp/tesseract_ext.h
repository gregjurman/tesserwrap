#include <tesseract/baseapi.h>
#include <tesseract/publictypes.h>
#include <tesseract/resultiterator.h>
#include <stdint.h>
#include <cstring>

class TessBaseAPIExt : public tesseract::TessBaseAPI
{
    private:
    unsigned char *picture;
    typedef tesseract::TessBaseAPI super;

    public:
    TessBaseAPIExt(void);
    ~TessBaseAPIExt(void); // Default destructor
    const char* TesseractRect(const unsigned char *data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height);
    void GetRectangle(uint64_t *, uint64_t *, uint64_t *, uint64_t *);
    void SetImage(const unsigned char *data, uint64_t size, uint64_t width, uint64_t height);
};

typedef TessBaseAPIExt *TessH;
