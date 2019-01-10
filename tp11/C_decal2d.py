import matplotlib
import numpy as np
from scipy import ndimage
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import imageio


np.set_printoptions(precision=1,linewidth=5000)



def get_simple_images(choix):

    img1=None
    img2=None
    if choix==0:
        img1=ndimage.imread("image/gamma_fin1.gif")[:,:,0]
        img2 = ndimage.imread("image/gamma_fin1.gif")[:,:,0]
    elif choix == 1:
        img1 = ndimage.imread("image/gamma_grand.gif")[:, :, 0]
        img2 = ndimage.imread("image/gamma_petit.gif")[:, :, 0]
    elif choix==2:
        img1 = ndimage.imread("image/grand_triangle.gif")[:, :, 0]
        img2 = ndimage.imread("image/petit_triangle.gif")[:, :, 0]
    elif choix==3:
        img1 = np.ones((3,3))
        img2= np.ones((2,2))

    elif choix==4:
        img1 = ndimage.imread("image/king.gif")[:, :, 0]
        img2 = ndimage.imread("image/translated.gif")[:, :, 0]
        """que fait-t-on subir à nos images ci-dessous ? """
        img1 = 255 - img1  # type:np.ndarray
        img2 = 255 - img2  # type:np.ndarray

    elif choix == 5: #idem qu'avant, mais en inversant l'ordre des images
        img1 = ndimage.imread("image/translated.gif")[:, :, 0]
        img2 = ndimage.imread("image/king.gif")[:, :, 0]
        """que fait-t-on subir à nos images ci-dessous ? """
        img1 = 255 - img1  # type:np.ndarray
        img2 = 255 - img2  # type:np.ndarray


    elif choix == 6:
        img1 = ndimage.imread("image/lena/lena_256_NB.png")
        img2 = ndimage.imread("image/lena/translation1.png")[:,:,0]

        print( img1.shape)
        print(img2.shape)


    elif choix == 7:
        img1 = ndimage.imread("image/lena/translation1.png")
        img2 = ndimage.imread("image/lena/translation1.png")[:, :, 0]

        print(img1.shape)
        print(img2.shape)



    return img1.astype(np.float32),img2.astype(np.float32)



def step0():
    img1,img2=get_simple_images(3)
    plt.subplot(1,2,1)
    plt.imshow(img1)
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.show()



def wrapping_shape(img1:np.ndarray, img2:np.ndarray):
    if len(img1.shape) != 2 or len(img1.shape) != 2: raise ValueError("args must be matrix")
    shape1 = np.array(img1.shape)
    shape2 = np.array(img2.shape)
    return np.maximum(shape1, shape2)


def enlargeImage(img:np.ndarray,enlargedShape)->np.ndarray:
    if len(img.shape)!=2 : raise ValueError("args must be matrix")
    if img.shape[0]>enlargedShape[0] or img.shape[1]>enlargedShape[1]: raise ValueError("enlargedShape must be larger that the shape of the image to enlarge")
    res=np.zeros(enlargedShape)
    res[:img.shape[0],:img.shape[1]]=img
    return res


def shiftAndEnlargeImage(img:np.ndarray, shift, enlargedShape=None)->np.ndarray:
    if enlargedShape is None : enlargedShape=(img.shape[0]+shift[0],img.shape[1]+shift[1])
    res=np.zeros(enlargedShape)
    res[shift[0]:img.shape[0]+shift[0],shift[1]:img.shape[1]+shift[1]]=img
    return res




def step1():
    img1,img2=get_simple_images(0)
    wrap=wrapping_shape(img1,img2)

    plt.subplot(2,2,1)
    plt.title('Enlarge')
    plt.imshow(enlargeImage(img1, wrap),vmin=100, vmax=150)
    plt.subplot(2,2,2)
    plt.title('Wrap*2')
    im=enlargeImage(img1,wrap * 2)
    plt.imshow(im,vmin=100, vmax=150)
    plt.subplot(2, 2, 3)
    plt.title('ShEn 2020')
    plt.imshow(shiftAndEnlargeImage(img1, (20, 20)),vmin=100, vmax=150)
    plt.subplot(2, 2, 4)
    plt.title('ShEn 3010')
    plt.imshow(shiftAndEnlargeImage(img1, (30, 10), enlargedShape=wrap * 2),vmin=100, vmax=150)
    plt.show()

"""
Quelle critique peut-on faire des sorties précédentes ?
Améliorez-les en précisant l'échelle des couleurs :
            plt.imshow(img,vmin=..., vmax=...)
"""



"""the convolution of the two images, with shape: max(img1.shape[0],img2.shape[0]), max(img1.shape[1],img2.shape[1])"""
def convolution_rapide_2d(img1:np.ndarray, img2:np.ndarray,isCircular:bool,isAnti:bool)->np.ndarray:

    wrap_shape=wrapping_shape(img1,img2)
    if not isCircular: wrap_shape*=2

    img1=enlargeImage(img1, wrap_shape)
    img2=enlargeImage(img2, wrap_shape)

    if isAnti:img1=img1[::-1,::-1]

    fft1=np.fft.fft2(img1)
    fft2=np.fft.fft2(img2)
    preRes=np.real(np.fft.ifft2(fft1*fft2))

    if isAnti :return preRes[::-1,::-1]
    else : return preRes




""" Pour tester, attention, elle ne calcule que les décalages positifs"""
def anti_convolution_lente2D(img1, img2):

    res=np.zeros(img1.shape)
    for x in range(0,img1.shape[0]):
        for y in range(0, img1.shape[1]):
            shift2=shiftAndEnlargeImage(img2, (x, y))
            wrap=wrapping_shape(img1,shift2)
            res[x,y]=np.sum(enlargeImage(img1,wrap)*enlargeImage(shift2,wrap))

    return res



def step3():
    img1, img2 = get_simple_images(1)
    print("lente\n",np.round(anti_convolution_lente2D(img1, img2),1))
    print("rapide\n",np.round( convolution_rapide_2d(img1, img2,False,True),1))



""" comparons les différents type de convolutions.
Essayez d'interprétez les résultats. Les convolutions de "gamma" sont les plus faciles à interpréter à mon avis """
def step4():
    """"""
    """avec 0, c'est les gamma fin"""
    img1, img2 = get_simple_images(7)
    plt.subplot(3, 2, 1)
    plt.imshow(img1)
    plt.title("img1")
    plt.subplot(3, 2, 2)
    plt.imshow(img2)
    plt.title("img2")
    plt.subplot(3, 2, 3)
    plt.imshow(convolution_rapide_2d(img1, img2,False,False))
    plt.title("convolution")
    plt.subplot(3, 2, 4)
    plt.imshow(convolution_rapide_2d(img1, img2,True,False))
    plt.title("convolution circulaire")
    plt.subplot(3, 2, 5)
    plt.imshow(convolution_rapide_2d(img1, img2,False,True))
    plt.title("anti-convolution")
    plt.subplot(3, 2, 6)
    plt.imshow(convolution_rapide_2d(img1, img2,True,True ))
    plt.title("anti-convolution circulaire")
    plt.legend()
    plt.show()




def step5():

    img1, img2 = get_simple_images(2) #ça va planter avec le choix 4 notamment
    anti=convolution_rapide_2d(img1, img2,False,True)


    wrap=wrapping_shape(img1,img2)

    print(wrap*2,np.prod(wrap*2),np.argmax(anti))

    shift= list(np.unravel_index(np.argmax(anti),wrap*2)) #le list: pour le warning

    somme=enlargeImage(img1,wrap*2)+shiftAndEnlargeImage(img2,shift,wrap*2)
    plt.subplot(131)
    plt.imshow(img1)
    plt.subplot(132)
    plt.imshow(img2)
    plt.subplot(133)
    plt.imshow(somme)
    plt.show()


"""
travail :

Modifiez le dernier step pour qu'il puisse caller 2 images quelque soit leur position relative.
notamment
        img1, img2 = getImages(4)
devrait fonctionner.
Attention, il y a 4 sortes de décalages possibles (2 décalages possibles pour les abscisses, 2 décalages possibles pour les ordonnées).
Vous trouverez peut-être un moyen astucieux pour traiter les 4 cas d'un seul coup. Sinon traitez les 4 cas.

"""


if __name__=="__main__":
    step1()
