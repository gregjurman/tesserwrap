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

# use pkg-config to get the directories and then use these values
# in the FIND_PATH() and FIND_LIBRARY() calls
if( NOT WIN32 )
  find_package(PkgConfig)

  pkg_check_modules(BOOSTPYTHON boost-python)

  set(BOOSTPYTHON_DEFINITIONS ${BOOSTPYTHON_CFLAGS})
endif( NOT WIN32 )

FIND_PATH(BOOSTPYTHON_INCLUDE_DIR NAMES boost/python.hpp
  PATHS
  ${BOOSTPYTHON_INCLUDE_DIRS}
)

include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(BoostPython DEFAULT_MSG BOOSTPYTHON_INCLUDE_DIR BOOSTPYTHON_LIBRARIES )

# show the BOOSTPYTHON_INCLUDE_DIR and BOOSTPYTHON_LIBRARIES variables only in the advanced view
MARK_AS_ADVANCED(BOOSTPYTHON_INCLUDE_DIR BOOSTPYTHON_LIBRARIES )

