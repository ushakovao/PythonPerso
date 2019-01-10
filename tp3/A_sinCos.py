import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.fftpack import fft, dct

np.set_printoptions(linewidth=500,precision=3)

'''nombre de fréquences d'approximation. Donc le nombre d'élément dans la base est 2*freqMax+1. //2'''
freqMax=150
'''nombre d'échantillons lorsque l'on discrétise les fonctions.
  Attention: si nbStep est trop petite, l'orthogonalité ne marchera pas (sauf coup de chance)//20'''
nbStep=200
''' intervalle de travaille'''
gauche=-1.
droite=1.
T=droite-gauche
''' pas d'échantillonnage'''
epsilon=T/nbStep
'''la grille d'abscisses (np.array set uniquement à éviter les warning, les déclarations de type en numpy étant mal foutue)'''
x=np.array(np.linspace(gauche,droite,nbStep))
'''la fonction à approximer'''

#y=(np.pi/4)*np.sign(np.sin(x))
y=x**2
#y=x ** 2+ np.expand_dims(x, 1) ** 2


basisAsList=[]
basisAsList.append(np.ones([nbStep]) * 1/math.sqrt(2))
for i in range(1,freqMax+1):
    basisAsList.append(np.sin(i*2*math.pi/T*x))
    basisAsList.append(np.cos(i*2*math.pi/T*x))


"""concaténation. Chaque ligne représente une fonction de la base"""
basis=np.array(basisAsList)

print("basis\n",basis)

matrixProd=np.sum(np.expand_dims(basis,1)*np.expand_dims(basis,0),2)
#matrixProd=np.sum(np.multiply(np.expand_dims(basis,1),np.expand_dims(basis,0)),2)
allScalarProducts=np.round(T/2*epsilon*  matrixProd,decimals=2)


"""avec un produit matriciel :"""
#allScalarProducts=100*2./T*epsilon*np.matmul(basis,basis.transpose())


fourierCoef=2./T*epsilon*np.sum(basis*y,1)
yApprox= np.sum(np.multiply(np.expand_dims(fourierCoef,1),basis),0)
error=np.sum(epsilon*(y-yApprox)*(y-yApprox))


print("allScalarProducts\n",allScalarProducts)
print("fourierCoef\n",fourierCoef)
print("yApprox\n",yApprox)
print("error\n",error)


""" Illustrer graphiquement ce programme, en superposant différentes approximation d'une même fonction """
"""essayer aussi avec une fonction avec discontinuité, par ex y = x (pourquoi est-elle discontinue ?)
 pour faire apparaître le phénomène de Gibbs
 Implémenter la base constituée uniquement de cosinus. Vérifier que le phénomène de Gibbs disparaît avec la fonction y=x

 """


#X, Y = np.meshgrid(x, x)
#Z1 = error
#Z2 = yApprox
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_surface(X, Y, Z1,cmap='OrRd',rstride=1, cstride=1, alpha = 0.5)
#ax.plot_surface(X, Y, Z2,cmap='coolwarm',rstride=1, cstride=1, alpha=0.5)
#
plt.plot(y)
plt.plot(yApprox, "r")
#plt.plot(fourierCoef)
plt.show()





"""maintenant à vous de jouer : vous devez faire le même programme mais en dimension 2.
Vous pouvez vous aider du squelette de programme sinCosDim2 , ou pas... """


