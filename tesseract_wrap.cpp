#include <tesseract/baseapi.h>
// TODO: Add the leptonica h file for the Pix class

using namespace tesseract;

class Tesserwrap
{
    private:
    TessBaseAPI api;
   
    public:
    Tesserwrap(void);
    Tesserwrap(const char* datadir="", const char*="eng");
}

// Tesserwrap - constructor
// Initializes the Tesseract Engine with a defined directory
// and defined language.
Tesserwrap::Tesserwrap(const char* datadir, const char* lang)
{
   api.Init(datadir, lang);
}

