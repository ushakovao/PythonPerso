
import math
import numpy as np
from scipy import ndimage
np.set_printoptions(precision=2,linewidth=5000)


"""Définissons une matrice 'basis' de taille N*N.
 Chacune des lignes étant un vecteur de la base des cosinus discrets.
 """

N=8
basis=np.zeros((N,N))
x=np.arange(N)
for n in range(N):
    basis[n,:]=np.cos( (2.* x +1)*math.pi*n/(2.*N))
    if n==0 :basis[n, :]*=math.sqrt(1 / N)
    else :basis[n, :]*=math.sqrt(2 / N)

"""bien sur, on pourrait supprimer la boucle, mais le gain en vitesse de calcul, serait trop peu
important par rapport à la perte en lisibilité du code.
"""


"""
A l'aide d'un produit matriciel, vérifiez que cette base est orthonormale,
 pour le produit scalaire usuel sca(u,v) = sum_x u[x] v[x]."""




"""Définissez la base de matrice issue de la tensorisation de la base précédente. Il faudra donc définir
 un tenseur d'ordre 4 :
                            basis2[i,j,x,y] = basis[i,x] basis[j,y] ;
On respectera cet ordre d'indice : pour avoir quelque chose ressemblant à base2_ij(x,y)

Vérifiez l'orthonormalité sur quelques matrices.
   BONUS : vérifiez l'orthonormalité pour tous les éléments de la base de matrices.
   """


""" Considérons une fonction de R^2 dans R échantillonnée sur une grille N*N. Par exemple
            (x,y)-> x^2+y^2
ou, cette fonction peut-être les niveaux de gris d'une image :
            ndimage.imread("../assets/img/lena_256_NB.png")
Vous obtiendrez  une matrice N*N qu'on appellera fonc2

Calculez ces coordonnées dans la base précédente. Pour mémoire :
           coef2[i,j] =   sum_x,y  basis2[i,j,x,y] fonc2[x,y]

Reconstituez la fonction avec la formule de reconstruction :
            fonc2[x,y] =  sum_i,j basis2[i,j,x,y]  coef2[i,j]
Vérifiez que l'on retombe bien sur la même fonction (faites des sorties graphiques, et des sorties numériques).

Maintenant 'compressez' la matrice coef2, par exemple en la quantifiant ou bien en mettant des coefficient à zéro.
Observez l'image obtenue par la formule de reconstitution.
Indiquez l'erreur quadratique :
             err = sum_x,y  ( fonc2[x,y]-fonc2Approx[x,y] )^2
Y a-t-il une autre façon de calculer cette erreur (égalité de Parceval ?)


BONUS : sur papier, vérifiez que la base de cosinus discret est orthonormale :
astuce : partez du fait que la bases des exponentielles discret est orthonormale pour le produit
scalaire : sca(u,v) =  1/N * sum_x u[x] v[x]
Attention, dans les exponentielles discret, il faut mettre un facteur spéciale devant le vecteur d'indice 0.

BONUS 2 :  comment passer de la Transformée de Fourier Discrète (TFD aussi appelée FFT par abus de langage)
à la transformée en cosinus discret ?
Dans le document 'fromFFT_toDCT' il est expliqué comment, à partir de Fourier discret, on crée la base des
cosinus discret.   Vous pouvez lire, c'est intéressant (mais un peu technique).
Vous pouvez aussi faire la paralèlle  avec les équivalents en temps continu :
C'est beaucoup plus facile en continu : la transformée en cosinus étant simplement les séries de Fourier
 appliquées aux fonction paires.

Mais le travail le plus facile est de faire le chemin inverse : observez la formule de la DCT. utilisez
la formule de Moivre (cos (x) =   [ e^(ix) + e^(-ix) ] /2 pour faire apparaître des exponentielles partout,
et exprimez cela en terme de TFD. En bonus, vous saurez comment faire une transformée en cosinus Rapide
(via la FFT)

 """


