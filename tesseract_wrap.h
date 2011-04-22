#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

using namespace tesseract;

class Tesserwrap
{
    private:
    TessBaseAPI api;
    PIX picture;

    public:
    Tesserwrap(const char* datadir="", const char* lang="eng");
    ~Tesserwrap(void); // Default destructor

    void SetImage(const unsigned char* data, int h, int w, int dpi);
};

