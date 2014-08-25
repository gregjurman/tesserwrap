#include <stdlib.h>
#include <string.h>
#include "tesseract_wrap.h"

struct ConfidenceNode
{
    int value;
    struct ConfidenceNode *next;
};

struct ResultNode
{
    char *value;
    float confidence;
    int box[4];
    struct ResultNode *next;
};


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

TESSERWRAP_CAPI void Tesserwrap_SetVariable(TessH tesserwrap, const char *key, const char *value)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  api->SetVariable(key, value);
}

TESSERWRAP_CAPI int Tesserwrap_MeanTextConf(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  return api->MeanTextConf();
}

TESSERWRAP_CAPI ConfidenceNode *Tesserwrap_AllWordConfidences(TessH tesserwrap)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  
  ConfidenceNode *first = new ConfidenceNode;
  ConfidenceNode *previous = new ConfidenceNode;
  
  int* confs = api->AllWordConfidences();
  int len, *trav;  
  for (len = 0, trav = confs; *trav != -1; trav++, len++){
    ConfidenceNode *temp = new ConfidenceNode;
    temp->value = *trav;
    temp->next = NULL;

    if(len == 0){
      first = temp;
    }
    else{
      previous->next = temp;
    }
    previous = temp;
  }
  free(confs);
  if(len == 0){
    return NULL;
  }
  return first;
}

TESSERWRAP_CAPI ResultNode *Tesserwrap_GetResult(TessH tesserwrap, int level)
{
  TessBaseAPIExt *api = (TessBaseAPIExt*) tesserwrap;
  
  ResultNode *first = new ResultNode;
  ResultNode *previous = new ResultNode;

  tesseract::ResultIterator* ri = api->GetIterator();
  tesseract::PageIteratorLevel lev = static_cast<tesseract::PageIteratorLevel>(level);

  int len = 0;

  if(ri != 0) {
      do {
          char* symbol = ri->GetUTF8Text(lev);
          float conf = ri->Confidence(lev);

          int x1, y1, x2, y2;
          ri->BoundingBox(lev, &x1, &y1, &x2, &y2);

          if(symbol != 0) {
              ResultNode *temp = new ResultNode;
              
              temp->value = strdup(symbol);
              temp->confidence = conf;
              temp->next = NULL;
              temp->box[0] = x1;
              temp->box[1] = y1;
              temp->box[2] = x2;
              temp->box[3] = y2;

              if(len == 0){
                first = temp;
              }
              else{
                previous->next = temp;
              }

              previous = temp;
              len++;
          }
          delete[] symbol;
      } while((ri->Next(lev)));
  }
  
  if(len == 0){
    return NULL;
  }
  return first; 
}



