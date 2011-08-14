#include <tesseract/baseapi.h>
//#include <leptonica/allheaders.h>
#include <string>
#include <boost/python/tuple.hpp>
#include <boost/python.hpp>

using namespace tesseract;
using namespace std;
using namespace boost::python;

enum PILImageFormat
{
L = 0, RGB=3, RGBA=4
};

class TessBaseAPIExt : public TessBaseAPI
{
    public:
    TessBaseAPIExt(void):TessBaseAPI(){}
    int Get_Rect_Left(void){return this->rect_left_;}
    int Get_Rect_Top(void){return this->rect_top_;}
    int Get_Rect_Width(void){return this->rect_width_;}
    int Get_Rect_Height(void){return this->rect_height_;}
};

class Tesserwrap
{
    private:
    TessBaseAPIExt api;
    unsigned char *picture;

    public:
    Tesserwrap(const char* datadir="", const char* lang="eng");
    ~Tesserwrap(void); // Default destructor
    void SetPageSegMode(PageSegMode mode);
    PageSegMode GetPageSegMode();
    const char* TesseractRect(string data,
                          int bytes_per_pixel, int bytes_per_line,
                          int left, int top, int width, int height);
    void SetRectangle(int left, int top, int w, int h);
    tuple GetRectangle(void);
    void SetImage(string data, int w, int h);
    void Clear();
    string GetUTF8Text(void);

};

