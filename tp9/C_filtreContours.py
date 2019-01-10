from scipy import signal as sg
from scipy import ndimage
import numpy as np
import imageio
import  matplotlib.pyplot as plt



img = ndimage.imread("../assets/img/testblur.png")[:,:,1]
# attention, avec imageio c'est :
#  img = imageio.imread("../assets/img/grille.gif")


"""combien de canaux a cette image dans le .gif ?"""
print(img.shape)


def step1():
    """"""
    """calcul des 'gradients' horizontaux et verticaux"""
    Gx = sg.convolve(img, [[1.], [-1]], "valid")
    Gy = sg.convolve(img, [[-1.], [1]], "valid")
    N = np.sqrt(Gx*Gx + Gy*Gy)
    print(N)


    plt.subplot(1, 5, 1)
    plt.imshow(Gx, cmap='gray')
    plt.subplot(1, 5, 2)
    plt.imshow(Gy, cmap='gray')
    plt.subplot(1, 5, 3)
    plt.imshow(N,cmap='gray')
    plt.subplot(1, 5, 4)
    plt.imshow(N,cmap='gray' )
    plt.subplot(1, 5, 5)
    plt.imshow(img,cmap='gray' )
    plt.show()
step1()


"""
Calculez et affichez N=sqrt(Gx^2+Gy^2), la norme du gradient.
Choisissez un seuil S, et affichez les endroits où N>S. On voit bien apparaître les contours. Comparez plusieurs seuils S:


Il est intéressant d'appliquer un lissage gaussien à notre image avant la détection de contours :
     Fort lissage : robustesse au bruit, mais contours épais (mauvaise localisation)
     Faible lissage : sensibilité au bruit, mais bonne localisation
Mettez en image cela.

"""



""" la discrétisation du gradient utilisé dans le step précédent n'est pas très satisfaisante. En voici des meilleurs"""
def step2():
    """"""
    """sobel, so-chouette"""
    Sx=[[-1,0,1],
        [-2,0,2],
        [-1,0,1]]

    Sy=[[ 1, 2, 1],
        [ 0, 0, 0],
        [-1,-2, 0]]

    """ Prewit : idem mais les 2 sont changé en 1. Moins bien"""

    """Robert: gradients 'diagonaux' """
    Rx=[[1,0],
        [0,-1]]

    Ry=[[ 0,1],
        [-1,0]]


    """ Bonus :  Il existe de nombreux autres masques pour approximer le gradient
    ex : les  masques de Kirsch et Robinson. Ce sont en fait des familles de 8 masques. On calcul les 8 convolutions et on garde la plus grande.
    Cf document ci-joint (Coursliban) p17"""


















