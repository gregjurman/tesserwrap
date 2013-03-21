#include "tesseract_wrap.h"


TESSERWRAP_CAPI TessH Tesserwrap_Init(const char *datadir, const char *lang)
{
  TessH h = new TessBaseAPIExt();
  h->Init(datadir, lang);
  return (TessH) h;
}

TESSERWRAP_CAPI void Tesserwrap_Destroy(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  if (api) delete api;
}

TESSERWRAP_CAPI void Tesserwrap_GetRectangle(TessH tesserwrap,
    uint64_t *left, uint64_t *top,
    uint64_t *width, uint64_t *height)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->GetRectangle(left, top, width, height);
}

TESSERWRAP_CAPI void Tesserwrap_SetRectangle(TessH tesserwrap,
    uint64_t left, uint64_t top,
    uint64_t width, uint64_t height)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->SetRectangle(left, top, width, height);
}

TESSERWRAP_CAPI void Tesserwrap_SetImage(TessH tesserwrap,
    const unsigned char *picture, uint64_t size, uint64_t width, uint64_t height)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->SetImage(picture, size, width, height);
}

TESSERWRAP_CAPI void Tesserwrap_SetPageSegMode(TessH tesserwrap,
    tesseract::PageSegMode pageseg)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->SetPageSegMode(pageseg);
}

TESSERWRAP_CAPI tesseract::PageSegMode Tesserwrap_GetPageSegMode(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  return api->GetPageSegMode();
}

TESSERWRAP_CAPI const char *Tesserwrap_GetUTF8Text(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  return api->GetUTF8Text();
}

TESSERWRAP_CAPI void Tesserwrap_Clear(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->Clear();
}
