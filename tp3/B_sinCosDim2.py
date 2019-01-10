import math
import numpy as np


'''nombre de fréquences d'approximation. Donc le nombre d'élément dans la base est 2*freqMax+1. '''
freqMax=5
'''nombre d'échantillons lorsque l'on discrètise les fonctions.
on commence par un nbStep très petit pour créer le programme
'''
nbStep=10
''' intervalle de travaille'''
gauche=-1.
droite=1.
T=droite-gauche
''' pas d'échantillonnage'''
epsilon=T/nbStep
'''la grille d'abscisses'''
x=np.array(np.linspace(gauche,droite,nbStep))
'''la fonction à approximer. Quelle est cette fonction ? Quelle symétrie admet-elle ? '''
fonc2= x ** 2+ np.expand_dims(x, 1) ** 2


"""crée la base 'basis' sin/cos  en dimension 1"""

basisAsList=[]
basisAsList.append(np.ones([nbStep]) * 1/math.sqrt(2))
for i in range(1,freqMax+1):
    basisAsList.append(np.sin(i*2*math.pi/T*x))
    basisAsList.append(np.cos(i*2*math.pi/T*x))


"""
Créer 'basis2' en tensorisant 'basis'
basis2[i,j,x,y] = basis[i,x] basis[j,y] ; pour avoir  un ordre d'indice ressemblant à base2_ij(x,y)"""

"""vérifions : """
#print(basis2.shape)




"""vérifion : calculez
- un produit scalaire sur la diagonale
- un produit scalaire en dehors de la diagonale
 Si cela ne fait pas 1 et 0, c'est soit qu'il y a une erreur, soit que nbStep est trop petit
 """


"""calculez les coef de fourier :
fourierCoef2[i,j] =   cst * sum_x,y  basis2[i,j,x,y] fonc2[x,y]
   """

"""
calculez la fonction approximée
fonc2Approx[x,y]= sum_i,j basis2[i,j,x,y]  fourierCoef2[i,j]  """

""" le calcul de l'erreur devrait être ceci :"""
#a=  np.sqrt( (fonc2 - fonc2Approx)**2) *epsilon * epsilon
#error2=np.sum(a)
""" l'erreur devrait décroître quand nbStep augmente"""



"""voici la partie affichage"""


"""Attention : même si les 2 premiers import semblent inutiles, ils servent quelque part
(matplotlib est mal conçue)"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


# X, Y = np.meshgrid(x, x)
# Z = fonc2Approx
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(X, Y, Z,cmap='coolwarm',rstride=1, cstride=1)
#
# plt.show()








