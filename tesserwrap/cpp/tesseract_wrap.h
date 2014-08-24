#include <stdint.h>
#include "tesseract_ext.h"

#ifdef __cplusplus
#  define TR_C_START           extern "C" {
#  define TR_C_END             }
#else
#  define TR_C_START
#  define TR_C_END
#endif

#define TESSERWRAP_CAPI

TR_C_START

typedef TessBaseAPIExt* TessH;

struct ConfidenceNode;
struct ResultNode;

TESSERWRAP_CAPI TessH Tesserwrap_Init(const char *datadir, const char *lang);
TESSERWRAP_CAPI void Tesserwrap_Destroy(TessH tesserwrap);
TESSERWRAP_CAPI void Tesserwrap_GetRectangle(TessH tesserwrap,
    uint64_t *left, uint64_t *top,
    uint64_t *width, uint64_t *height);
TESSERWRAP_CAPI void Tesserwrap_SetRectangle(TessH tesserwrap,
    uint64_t left, uint64_t top,
    uint64_t width, uint64_t height);
TESSERWRAP_CAPI void Tesserwrap_SetImage(TessH tesserwrap,
    const unsigned char *picture, uint64_t size, uint64_t width, uint64_t height);
TESSERWRAP_CAPI void Tesserwrap_SetPageSegMode(TessH tesserwrap,
    tesseract::PageSegMode pageseg);
TESSERWRAP_CAPI tesseract::PageSegMode Tesserwrap_GetPageSegMode(TessH tesserwrap);
TESSERWRAP_CAPI const char *Tesserwrap_GetUTF8Text(TessH tesserwrap);
TESSERWRAP_CAPI void Tesserwrap_Clear(TessH tesserwrap);
TESSERWRAP_CAPI void Tesserwrap_SetVariable(TessH tesserwrap, const char *key, const char *value);
TESSERWRAP_CAPI int Tesserwrap_MeanTextConf(TessH tesserwrap);
TESSERWRAP_CAPI ConfidenceNode *Tesserwrap_AllWordConfidences(TessH tesserwrap);
TESSERWRAP_CAPI ResultNode *Tesserwrap_GetResult(TessH tesserwrap , int level);

TR_C_END
