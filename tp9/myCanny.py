import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import imageio
from PIL import Image
from pylab import *

from skimage import feature

"""
# Generate noisy image of a square
im = np.zeros((128, 128))
im[32:-32, 32:-32] = 1

im = ndi.rotate(im, 15, mode='constant')
im = ndi.gaussian_filter(im, 4)
im += 0.2 * np.random.random(im.shape)
"""
im = array(Image.open('../assets/img/cube.jpg').convert('L'))

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im, sigma=0.05)
edges2 = feature.canny(im, sigma=5)

# display results
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 2),
                                    sharex=True, sharey=True)

ax1.imshow(im)
ax1.axis('off')

ax2.imshow(edges1, )
ax2.axis('off')

"""
ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
"""

fig.tight_layout()

plt.show()