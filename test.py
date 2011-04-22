import Image
import tesserwrap

im = Image.open("test.png")
tw = tesserwrap.Tesserwrap()

# We want a single line
tw.setpagesegmode(tesserwrap.pagesegmode.auto)

# Do it up
print tw.tesseractrect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])


