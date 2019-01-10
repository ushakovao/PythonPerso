
import numpy as np
from scipy import signal as sg
from scipy import ndimage
import  matplotlib.pyplot as plt

from tp9.util import uint8clipRound

np.set_printoptions(precision=2,linewidth=500)

img = ndimage.imread("../assets/img/cat2.png")
red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]
print(red.shape)



""" convolution sans utiliser de bibliothèque"""
def convolution2D(image, masque):

    py = (masque.shape[0] - 1) // 2
    px = (masque.shape[1] - 1) // 2

    """a quoi sert cette copie ? Ne serais-ce pas mieux :
     res=np.empty_like(image)
     ou ce qui est idem
     res=np.empty(shape=image.shape,dtype=image.dtype)
     """
    res = image.copy()

    for i in range(px ,image.shape[1 ] -px):
        for j in range(py ,image.shape[0 ] -py):
            somme = 0.0
            for k in range(-px , px +1):
                for l in range(-py , py +1):
                    somme += image[j + l][i + k] * masque[l + py][k + px]
            res[j][i] = somme
    return res

"""EDGES
    masque =np.array([[-1, 0, 0, 0, 0],
                      [0, -1, 0, 0, 0],
                      [0, 0, 4, 0, 0],
                      [0, 0, 0, -1, 0],
                      [0, 0, 0, 0, -1]])

        masque = np.array([[-1, -1, -1],
                      [-1, -1, -1],
                      [-1, -1, -1]])
"""



"""on fait une convolution avec notre propre fonction. On regarde l'effet que cela produit sur l'image.
 Faites varier la taille du masque"""
def step0():


    image = red*1.0  #type:np.ndarray
    #masque = np.ones((3,3)) #type:np.ndarray
    masque1 =np.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])

    imageConv1 = convolution2D(image,masque1)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.imshow(imageConv1)
    plt.show()


""" idem, mais en utilisant la fonction de convolution de scipy.
Pourquoi la taille d'image rétrécie-t-elle ?
BONUS : quels sont les différents 'mode' possible.
"""


def step1():
    image=[[255, 7, 3],
          [212, 240, 4],
          [218, 216, 230]]

    imageConv= sg.convolve(image, [[1., -1]], mode="valid")
    plt.imshow(imageConv)
    plt._show()
    print(imageConv)


"""Quand on veut effectuer un lissage, on préfère des masques gaussien au masque constant. """
def masqueGaussien2d(shape=(3, 3), sigma=0.5):

    if len(shape)!=2: raise ValueError("len-2 shape required")
    if shape[0]%2!=1 or shape[1]%2!=1: raise ValueError("only odd sizes are OK")

    m,n = (shape[0]-1)/2,(shape[1]-1)/2
    y,x = np.ogrid[-m:m+1,-n:n+1]
    res = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )

    """pour éviter d'avoir des valeur à 1.e-36"""
    res[ res < 1.e-16 ] = 0
    """normalisation"""
    res/=res.sum()
    return res




def masquemed2d(shape=(3, 3)):

    if len(shape)!=2: raise ValueError("len-2 shape required")
    if shape[0]%2!=1 or shape[1]%2!=1: raise ValueError("only odd sizes are OK")

    m,n = (shape[0]-1)/2,(shape[1]-1)/2
    y,x = np.ogrid[-m:m+1,-n:n+1]
    res = np.median ( x, axis=0)

    """pour éviter d'avoir des valeur à 1.e-36"""
    res[ res < 1.e-16 ] = 0
    """normalisation"""
    res/=res.sum()
    return res






def step2():
    print(masqueGaussien2d((11, 11)))


"""convolution avec un masque gaussien pour gommer un bruit gaussien"""
def step3():
    image = red*1.0  # type:np.ndarray

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='Reds')

    image+=np.random.normal(scale=50,size=image.shape)
    masque = masqueGaussien2d(shape=(5,5),sigma=2.)
    imageConv=sg.convolve(image,masque, "valid")

    plt.subplot(1, 3, 2)
    plt.imshow(image,cmap='Reds')
    plt.subplot(1,3,3)
    plt.imshow(imageConv, cmap='Reds')

    plt.show()


def mine1():
    image = red*1.0 #type:np.ndarray
    masque = np.eye((5,5))/25
    imageConv = convolution2D(image,masque)
    plt.imshow(imageConv)
    plt.show()


"""filtre médian pour supprimer un bruit impulsionnel"""
def step4():
    image = img  #type:np.ndarray

    proba=0.05
    intensity=100
    """rajout d'un bruit impulsionnel, aussi appelé 'poivre et sel' """
    imageNoise= uint8clipRound(  image + (np.random.uniform(size=image.shape)<proba) * intensity *(np.random.randint(0,1)*2-1) )

    newim=ndimage.median_filter(image, 7)

    newim2=sg.medfilt(image,11)




    plt.subplot(1, 4, 1)
    plt.imshow(image)
    plt.subplot(1, 4, 2)
    plt.imshow(imageNoise)
    plt.subplot(1, 4, 3)
    plt.imshow(newim)
    plt.subplot(1, 4, 4)
    plt.imshow(np.abs(image - newim))

    """a vous de jouer :  pour chaque sous-images de taille donnée (ex : 5x5), remplacez la valeur centrale par la médiane de la sous-image.
     Vous pouvez vous inspirer du programme de convolution ci-dessus.
     vous pouvez aussi vous inspirer du programme "rolling_window" qu'on a utilisé pour la détection des pics. Cela va accélérer le programme.


     Vous pourriez aussi utiliser une procedure toute faite
     Il y en a plusieurs dans scipy (scipy est une grosse usine) :
     scipy.signal.medfilt
     scipy.ndimage.filters.median_filter (voir par exemple :http://www.scipy-lectures.org/advanced/image_processing/auto_examples/plot_denoising.html)
     Mais je vous demande de le coder à la main. Ce qui vous permettra de faire le bonus suivant :

     BONUS :  Modifiez le filtre médian pour qu'il renvoie la moyenne des n-valeurs les plus médiannes dans la fenêtre (avec n<5x5).

     """


    plt.show()

step0()

""" Justifiez avec vos mots pourquoi   :
   - Les filtres de convolution sont utilisés pour les bruits de moyenne nulle
   - Les  filtres médians sont utilisés  pour les bruits impulsionnels.
   Un filtre est dit linéaire lorsque
      Filtre(image1+image2)=Filtre(image1)+Filtre(image2) et
      Filtre(lambda*image)=lambda*Filtre(image)
    A-t-on fait des filtre linéaire précédemment ?

   """