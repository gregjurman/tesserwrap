import Image
import tesserwrap

im = Image.open("test.png")
tw = tesserwrap.Tesserwrap()

print tw.tesseractrect(im.tostring(), 1, im.size[0], 0,0, im.size[0], im.size[1])


