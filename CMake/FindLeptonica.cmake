# - Try to find Leptonica
# Once done this will define
#
#  LEPTONICA_FOUND - system has Leptonica
#  LEPTONICA_INCLUDE_DIR - the Leptonica include directory
#  LEPTONICA_LIBRARIES - Link these to use Leptonica
#  LEPTONICA_DEFINITIONS - Compiler switches required for using Leptonica
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.
#


if ( LEPTONICA_INCLUDE_DIR AND LEPTONICA_LIBRARIES )
   # in cache already
   SET(Leptonica_FIND_QUIETLY TRUE)
endif ( LEPTONICA_INCLUDE_DIR AND LEPTONICA_LIBRARIES )

FIND_PATH(LEPTONICA_INCLUDE_DIR NAMES leptonica/allheaders.h
)

FIND_LIBRARY(LEPTONICA_LIBRARIES NAMES lept
)

include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(Leptonica DEFAULT_MSG LEPTONICA_INCLUDE_DIR LEPTONICA_LIBRARIES )

# show the LEPTONICA_INCLUDE_DIR and LEPTONICA_LIBRARIES variables only in the advanced view
MARK_AS_ADVANCED(LEPTONICA_INCLUDE_DIR LEPTONICA_LIBRARIES )

