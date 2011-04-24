import cv
import Image
import numpy
import math
import itertools

im = Image.open("testcols.png")
cv_im = cv.CreateImageHeader(im.size, cv.IPL_DEPTH_8U, 1)
cv_cannyim = cv.CreateImage(im.size, cv.IPL_DEPTH_8U, 1)
cv.SetData(cv_im, im.tostring())

#cv.NamedWindow("original")
#cv.NamedWindow("contours")
#cv.NamedWindow("final")
#cv.ShowImage("original", cv_im)

cv.Canny(cv_im, cv_cannyim, 10, 90, 3)
#cv.ShowImage("contours", cv_cannyim)

sums = numpy.sum(cv.GetMat(cv_cannyim), axis=1)

slices = []
loc = 0
for i in range(0, len(sums)-1):
    val0 = sums[i]
    val1 = sums[i+1]
    if math.log(val1+1) > val0:
        slices.append(i+1)
    elif math.log(val0+1) > val1:
        slices.append(-(i))

splits = []
for i in range(0, len(slices)-1):
    val0 = slices[i]
    val1 = slices[i+1]
    if val0 > 0 and val1 < 0:
        splits.append((val0, abs(val1)))

print splits
print len(splits)*2 == len(slices)
#for val in slices:
#    y = abs(val)
#    cv.Line(cv_im, (0, y), (cv_im.width, y), (0) if val > 0 else (128))

#cv.ShowImage("final", cv_im)

#cv.WaitKey()
