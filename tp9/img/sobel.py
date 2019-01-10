import numpy
import scipy
from scipy import ndimage
from scipy import ndimage
import  matplotlib.pyplot as plt

im = scipy.misc.imread("hearts.jpg")
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
scipy.misc.imsave('hxS.jpg', dx)
dy = ndimage.sobel(im, 1)  # vertical derivative
scipy.misc.imsave('hdyS.jpg',dy)
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('hS.jpg', mag)
