#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>
#include <string>

using namespace tesseract;
using namespace std;

enum PILImageFormat
{
L = 0, RGB=3, RGBA=4
};

class Tesserwrap
{
    private:
    TessBaseAPI api;
    PIX picture;

    public:
    Tesserwrap(const char* datadir="", const char* lang="eng");
    ~Tesserwrap(void); // Default destructor
    void SetPageSegMode(PageSegMode mode);
    PageSegMode GetPageSegMode();
    const char* TesseractRect(string data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height);
    void SetRectangle(int left, int top, int w, int h);
    void SetImage(string data, PILImageFormat iformat, int h, int w);
};

