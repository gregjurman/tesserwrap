# - Try to find BoostPython
# Once done this will define
#
#  BOOSTPYTHON_FOUND - system has BoostPython
#  BOOSTPYTHON_INCLUDE_DIR - the BoostPython include directory
#  BOOSTPYTHON_LIBRARIES - Link these to use BoostPython
#  BOOSTPYTHON_DEFINITIONS - Compiler switches required for using BoostPython
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.
#


if ( BOOSTPYTHON_INCLUDE_DIR AND BOOSTPYTHON_LIBRARIES )
   # in cache already
   SET(BoostPython_FIND_QUIETLY TRUE)
endif ( BOOSTPYTHON_INCLUDE_DIR AND BOOSTPYTHON_LIBRARIES )

FIND_PATH(BOOSTPYTHON_INCLUDE_DIR NAMES boost/python.hpp
)

FIND_LIBRARY(BOOSTPYTHON_LIBRARIES NAMES boost_python
)

include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(BoostPython DEFAULT_MSG BOOSTPYTHON_INCLUDE_DIR BOOSTPYTHON_LIBRARIES )

# show the BOOSTPYTHON_INCLUDE_DIR and BOOSTPYTHON_LIBRARIES variables only in the advanced view
MARK_AS_ADVANCED(BOOSTPYTHON_INCLUDE_DIR BOOSTPYTHON_LIBRARIES )

