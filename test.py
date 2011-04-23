import Image
import tesserwrap
import time
import subprocess

im = Image.open("test.png")
tw = tesserwrap.Tesseract()


time_start = time.time()
# Do it up 1000 times
for i in range(10):
    tw.ocr_image(im)
    #tw.tesseract_rect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])
time_end = time.time()
print "tesserwrap (load+recog):"
print "    Total Time: %f" % (time_end - time_start)
print "    Time per iteration: %f" % ((time_end - time_start)/1000)


time_start = time.time()

tw.set_image(im)

# Do it up 1000 times
for i in range(10):
    tw.set_rectangle(0, 0, im.size[0], im.size[1])
    tw.get_utf8_text()
time_end = time.time()
print "tesserwrap (preload):"
print "    Total Time: %f" % (time_end - time_start)
print "    Time per iteration: %f" % ((time_end - time_start)/1000)

print tw.get_rectangle()
