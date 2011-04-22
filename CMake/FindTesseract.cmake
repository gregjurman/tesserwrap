# - Try to find tesseract
# Once done this will define
#
#  TESSERACT_FOUND - system has tesseract
#  TESSERACT_INCLUDE_DIR - the tesseract include directory
#  TESSERACT_LIBRARIES - Link these to use tesseract
#  TESSERACT_DEFINITIONS - Compiler switches required for using tesseract
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.
#


if ( TESSERACT_INCLUDE_DIR AND TESSERACT_LIBRARIES )
   # in cache already
   SET(tesseract_FIND_QUIETLY TRUE)
endif ( TESSERACT_INCLUDE_DIR AND TESSERACT_LIBRARIES )

FIND_PATH(TESSERACT_INCLUDE_DIR NAMES tesseract/baseapi.h
  PATHS
  ${TESSERACT_INCLUDE_DIRS}
)

FIND_LIBRARY(TESSERACT_LIBRARIES NAMES tesseract_api
  PATHS
  ${TESSERACT_LIBRARY_DIRS}
)

include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(tesseract DEFAULT_MSG TESSERACT_INCLUDE_DIR TESSERACT_LIBRARIES )

# show the TESSERACT_INCLUDE_DIR and TESSERACT_LIBRARIES variables only in the advanced view
MARK_AS_ADVANCED(TESSERACT_INCLUDE_DIR TESSERACT_LIBRARIES )

