


""""""
"""
Convolez les images avec l'un des masques suivants. Vous calculerez ainsi le laplacien de l'image.
Comment repère-t-on les contours ? Faite le lien avec le travail effectué dans le fichier contours1d.


Théorisons une image par une fonction de R^2 dans R.  Quand on fait une rotation de cette image, comment
réagit son laplacien ? Cette propriété est-elle vrai avec la norme du gradient ? Nous comprenons ainsi l'intérêt
de la détection du second ordre.
"""
def step0():
    """"""
    """laplacien discret 4"""
    laplace1=[[0, 1,0],
              [1,-4,1],
               0, 1,0]
    """laplacien discret 8"""
    laplace2=[[1, 1,1],
              [1,-8,1],
              [1, 1,1]]

    """laplacien du fameux Robinson (on peut devenir célèbre avec 9 entiers)"""
    laplace3 = [[ 1, -2, 1],
                [-2,  4,-2],
                [ 1, -2, 1]]




"""
Implémentez l'agorithme suivant :
Notons L le laplacien d'une image.
Considérons un pixel 'p'. Notons C le carré 3x3 centré en 'p'.
Notons L_C les 9 valeurs du laplacien sur C.
Ce pixel 'p' sera dans un contour lorsque :
max(L_C)>0, min(L_C)<0 et  max(L_C)-min(L_C) > seuil.

Expliquez cet algorithme avec vos mots, en vous inspirant du programme contour1d précédent.
"""


"""
BONUS 1:
Comme pour les méthodes de gradient : il vaut mieux effectuer un filtrage gaussien avant de détecter les contours.
Notons G le noyau gaussien discrétisé, D le laplacien discret, I l'image et * la convolution. Ainsi il faut faire
         I * G * D = I * (G* D)
Ainsi on peut ainsi directement définir et utiliser le masque G*I (quelle est sa taille ?).
Mais il y a une meilleurs technique : On considère GG la vraie gaussienne définie sur R^2, et DD le vrai opérateur laplacien.
On calcul mathématiquement GG*DD (c.à.d. qu'on applique le Laplacien à la Gaussienne, le calcul n'est pas dur !). Ensuite
on discrétise Cette fonction pour en faire un masque de la taille que l'on veut (inspirez vous de la discrétisation de
la gaussien dans un fichier précédent).
"""



"""
BONUS 2:
Implémenter le filtre de CANY, qui comporte 4 étapes. C'est un filtre 'optimal'
https://en.wikipedia.org/wiki/Canny_edge_detector
"""
