"""
Measurements from images
==========================

This examples shows how to measure quantities from various images.

"""

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import imageio

#im = array(Image.open('bac.jpg').convert('L'))

np.random.seed(1)
n = 10
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = im > im.mean()

label_im, nb_labels = ndimage.label(mask)

sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))
mask_size1 = sizes < 500
remove_pixel = mask_size1[label_im]
label_im[remove_pixel] = 0

labels = np.unique(label_im)
label_clean = np.searchsorted(labels, label_im)




plt.imshow(label_im, cmap="gray")


plt.show()


