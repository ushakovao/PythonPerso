import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = np.linspace(0, 10, num=11, endpoint=True)
#y=np.cos(x)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
f1= interp1d(x, y, kind='quadratic')
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=41, endpoint=True)

plt.plot(x, y, 'o',  xnew, f(xnew), ':', xnew, f1(xnew), '-.',xnew, f2(xnew), '--')
plt.legend(['points d`interpolation', 'linear','quadratic', 'cubic'], loc='best')
plt.show()