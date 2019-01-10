import numpy as np
import matplotlib.pyplot as plt
from scipy import fft2

x = np.ones((4, 4, 2))
y = fft2(x, shape=(8, 8), axes=(-3, -2))
y_r = np.fft.fft2(x, s=(8, 8), axes=(-3, -2))
plt.plot( y, 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')

plt.show()