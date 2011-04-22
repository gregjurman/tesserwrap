AC_INIT ([tesserwrap], [1.0])
AC_PREREQ([2.59])
AM_INIT_AUTOMAKE([1.10 no-define])
AC_CONFIG_HEADERS([config.h])
AC_PROG_CXX
AC_CONFIG_FILES([Makefile])
AC_CONFIG_SRCDIR([tesseract_wrap.cpp])
AC_CHECK_HEADER(leptonica/allheaders.h,
	[AC_DEFINE(HAVE_LEPT_H, 1, 
		[Define to 1 if you have <leptonica/allheaders.h>])],
	[AC_MSG_WARN([Leptonica headers missing, using alternate functions.])])

AC_CHECK_HEADER(tesseract/baseapi.h,
	[AC_DEFINE(HAVE_TESSERACT_H, 1,
		[Define to 1 if you have <tesseract/baseapi.h])],
	[AC_MSG_ERROR([Missing the Tesseract API header!])])
AC_OUTPUT
