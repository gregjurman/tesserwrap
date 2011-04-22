import Image
import tesserwrap
import time
import subprocess

im = Image.open("test.png")
tw = tesserwrap.Tesserwrap()


time_start = time.time()

# Do it up 1000 times
for i in range(1000):
    tw.tesseractrect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])
time_end = time.time()
print "tesserwrap:"
print "    Total Time: %f" % (time_end - time_start)
print "    Time per iteration: %f" % ((time_end - time_start)/1000)

