# ########## Project setup ##########
PROJECT(tesserwrap)
CMAKE_MINIMUM_REQUIRED(VERSION 2.4.5)

set(CMAKE_MODULE_PATH
	"${CMAKE_MODULE_PATH}"
	"${tesserwrap_SOURCE_DIR}/CMake/"
	)
find_package(Tesseract REQUIRED)
find_package(Leptonica)
find_package(BoostPython REQUIRED)
find_package(PythonLibs REQUIRED)

# ######### General setup ##########
INCLUDE_DIRECTORIES(
	${CMAKE_SOURCE_DIR}
	${TESSERACT_INCLUDE_DIR}
	${LEPTONICA_INCLUDE_DIR}
	${BOOSTPYTHON_INCLUDE_DIR}
	${PYTHON_INCLUDE_DIRS}
	# stupid compatibility thing for cmake 2.6 :(
	${PYTHON_INCLUDE_PATH}
)

LINK_DIRECTORIES(
	${TESSERACT_LIBRARY_DIRS}
	${LEPTONICA_LIBRARY_DIRS}
	${PYTHON_LIBRARY_DIRS}
)

add_definitions(-DBOOST_PYTHON_DYNAMIC_LIB)

# ########## tesserwrap library ##########
# Sources:
SET(tesserwrap_library_SRCS
    tesserwrap.cpp
    tesseract_wrap.cpp
)

# Headers:
SET(tesserwrap_library_HDRS
    tesseract_wrap.h
)



# actual target:
ADD_LIBRARY(tesserwrap ${tesserwrap_library}_SCRS ${tesserwrap_library_HDRS})
SET_TARGET_PROPERTIES(tesserwrap PROPERTIES VERSION 0.0.0)

# add install target:
INSTALL(TARGETS tesserwrap DESTINATION lib)
