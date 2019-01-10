import numpy as np
import scipy as sci
import pylab as pl

xa=0
xb=2

C=np.linspace(xa,xb,100)
iter=1000
Y = np.ones(len(C))

for x in range(iter):
    Y = Y**2 - C
for x in range(iter):
    Y = Y**2 - C
    pl.plot(C,Y)
pl.show()