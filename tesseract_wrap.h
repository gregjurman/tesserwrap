#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>
#include <string>

using namespace tesseract;
using namespace std;

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
    void SetImage(string data, int h, int w, int dpi);
};

