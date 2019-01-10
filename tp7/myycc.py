import numpy
import Image as im
image = im.open('test.png')
ycbcr = image.convert('YCbCr')

# output of ycbcr.getbands() put in order
Y = 0
Cb = 1
Cr = 2

YCbCr=list(ycbcr.getdata()) # flat list of tuples
# reshape
imYCbCr = numpy.reshape(YCbCr, (image.size[1], image.size[0], 3))
# Convert 32-bit elements to 8-bit
imYCbCr = imYCbCr.astype(numpy.uint8)

# now, display the 3 channels
im.fromarray(imYCbCr[:,:,Y], "L").show()
im.fromarray(imYCbCr[:,:,Cb], "L").show()
im.fromarray(imYCbCr[:,:,Cr], "L").show()