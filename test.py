import Image
import tesserwrap
import time
import subprocess

im = Image.open("testcols.png")
tw = tesserwrap.Tesseract()


#These are row slices from the OpenCV test code (not commited)
slices = [(17, 72), (217, 272), (417, 472), (617, 672), (817, 872), (960, 1015), 
          (1103, 1158), (1303, 1358), (1446, 1501), (1646, 1701), (1846, 1901), 
          (2046, 2101), (2246, 2301), (2446, 2501), (2589, 2644), (2789, 2844), 
          (2932, 2987), (3075, 3130), (3218, 3273)]

time_start = time.time()
# Do it up 1000 times
for i in range(1):
    print tw.ocr_image(im)
    #tw.tesseract_rect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])
time_end = time.time()
print "tesserwrap (Entire Image At Once):"
print "    Total Time: %f" % (time_end - time_start)
#print "    Time per iteration: %f" % ((time_end - time_start)/1000)


time_start = time.time()
print

tw.set_image(im)
tw.set_page_seg_mode(tesserwrap.page_seg_mode.single_line)

# Do it up 1000 times
for rt, rb in slices:
    tw.set_rectangle(0, rt, im.size[0], rb-rt)
    print "(%i, %i) - '%s'" % (rt, rb, tw.get_utf8_text().strip())

time_end = time.time()
print "tesserwrap (preload + split rect):"
print "    Total Time: %f" % (time_end - time_start)
#print "    Time per iteration: %f" % ((time_end - time_start)/1000)

#print tw.get_rectangle()
