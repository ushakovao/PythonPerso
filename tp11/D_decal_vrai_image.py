import  matplotlib
matplotlib.use('TkAgg')
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

from tp11.C_decal2d import convolution_rapide_2d, wrapping_shape, enlargeImage, shiftAndEnlargeImage

np.set_printoptions(precision=1,linewidth=5000)

def get_vrai_images(choix):

    img1=None
    img2=None


    if choix == 1:
        img1 = ndimage.imread("image/lena/lena_256_NB.png")
        img2 = ndimage.imread("image/lena/translation1.png")[:,:,0]



    elif choix == 2:
        img1 = ndimage.imread("image/lena/translation1.png")
        img2 = ndimage.imread("image/lena/translation2.png")[:,:,0]





    return img1.astype(np.float32),img2.astype(np.float32)




""" observer le décalage que propose notre algorithme. Expliquez cette erreur (observer de près la superposition) """
def step0():

    img1, img2 = get_vrai_images(1) #ça va planter avec le choix 4 notamment
    anti=convolution_rapide_2d(img1, img2,False,True)

    wrap=wrapping_shape(img1,img2)

    print(wrap*2,np.prod(wrap*2),np.argmax(anti))

    shift= list(np.unravel_index(np.argmax(anti),wrap*2)) #le list: pour le warning

    somme=enlargeImage(img1,wrap*2)+shiftAndEnlargeImage(img2,shift,wrap*2)
    plt.imshow(somme)
    plt.show()


""" Pour bien caller des vraies images il faut en extraire des 'features', par exemple des contours.
   Installez skimage via la console :

   sudo pip install -U scikit-image

   c'est une bibliothèque très riche de traitement d'image
   (il y a encore plus riche : opencv, mais c'est pénible à installer)

   vous pouvez aussi utilisez un de vos filtre de détection des contours


   """


from skimage import feature


"""observons les filtres de canny avec des sigma différents """
def step1():
    #img1, img2 = get_vrai_images(5)
    img1 = ndimage.imread("image/c1.png")[:, :, 0]
    edge1=feature.canny(img1)
    edge2=feature.canny(img1,sigma=2)
    edge3 = feature.canny(img1, sigma=3)
    edge4 = feature.canny(img1, sigma=4)


    plt.subplot(2,2,1)
    plt.imshow(img1)
    plt.subplot(2, 2, 2)
    plt.imshow(edge2)
    plt.subplot(2, 2, 3)
    plt.imshow(edge3)
    plt.subplot(2, 2, 4)
    plt.imshow(edge4)
    plt.show()


if __name__=='__main__':
    step1()


"""
travail:
recaler le bout de visage de Lena sur son visage entier (choix==1)

recaler deux bouts entre eux

BONUS : rassembler les 4 bouts

"""

