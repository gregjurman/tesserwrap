import Image
import libtesserwrap
import time
import subprocess

im = Image.open("test.png")
tw = libtesserwrap.Tesserwrap()


time_start = time.time()
# Do it up 1000 times
for i in range(1000):
    tw.tesseractrect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])
time_end = time.time()
print "tesserwrap (load+recog):"
print "    Total Time: %f" % (time_end - time_start)
print "    Time per iteration: %f" % ((time_end - time_start)/1000)


time_start = time.time()

tw.setimage(im.tostring(), im.size[0], im.size[1])

# Do it up 1000 times
for i in range(1000):
    tw.setrectangle(0, 0, im.size[0], im.size[1])
    tw.getutf8text()
time_end = time.time()
print "tesserwrap (preload):"
print "    Total Time: %f" % (time_end - time_start)
print "    Time per iteration: %f" % ((time_end - time_start)/1000)


