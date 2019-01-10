""" quelques liens"""


"""
Divers documents/tutoriel intéressant sur JPEG. Mais faites en priorité le TP

Celui qui a inspiré ce TP :
https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html

En français, sympa (aussi dans le dossier biblio) :
https://lehollandaisvolant.net/science/jpg/

Plus détaillé, le cours d'Andrea Dragut dans le dossier biblio

Un document en anglais où la partie "encodage de Huffman est bien détaillée: "
https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/jpegUpToQuant.html
"""

"""
Le dernier algo de compression JPEG est tout récent. Il faut savoir que JPEG est une norme qui définit
un formal de donnée que tous les logiciels/navigateur savent transformer en image RGB (= décompresser).
 Par contre,les algorithmes de compression sont  nombreux.
 L'algo Guetzli ci-dessous a l'avantage de mieux compresser, et le désavantage d'être plus lent.
https://www.developpez.com/actu/124269/Google-presente-son-algorithme-de-compression-JPEG-baptise-Guetzli-qui-promet-des-reductions-de-taille-de-35-pourcent-sans-trop-perdre-en-qualite/
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy


from scipy import ndimage
from scipy import fftpack


np.set_printoptions(precision=2,linewidth=5000)





"""changez le chemin pour changer l'image"""
def readIm():
    return ndimage.imread("../assets/img/cafe.png")


"""on affiche l'image"""
def step0():
    im=readIm()
    plt.imshow(im,cmap='gray')
    plt.show()


""" la dct2 s'obtient en appliquant deux fois la dct1, une fois sur les lignes, puis une fois sur les colonnes """
def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')

"""test"""
def step2():
    a=np.ones((5,5))
    print(dct2(a))


"""on affiche tous les éléments de la base. Expliquez comment on procède"""
def step4():
    for i in range(8):
        for j in range(8):
            a=np.zeros((8,8))
            a[i,j]=1
            plt.subplot(8,8,i*8+j+1)
            plt.axis('off')
            plt.imshow(idct2(a),cmap='gray',interpolation='nearest')
    plt.show()


"""découpage de l'image en carré 8*8, passage au dct de chacune de chacun des carré """
def cutAndTransform(im):
    im_size = im.shape
    dct = np.zeros(im_size)

    """ np.r_  permet de faire des listes d'indice avec une syntaxe qui nous est familière"""
    for i in np.r_[:im_size[0]:8]:
        for j in np.r_[:im_size[1]:8]:
            dct[i:(i + 8), j:(j + 8)] = dct2(im[i:(i + 8), j:(j + 8)])

    return dct


def step5():
    im = readIm()
    dct=cutAndTransform(im)

    plt.imshow(dct, cmap='gray', interpolation='nearest')
    plt.title("8x8 DCTs of the image")
    plt.show()


"""suppression de tous les coefficients inférieur à un seuil"""
def threshold(dct, thresh):
    return dct * (abs(dct) > (thresh * np.max(dct)))



def step7():
    im = readIm()
    dct = cutAndTransform(im)
    dct_thresh=threshold(dct, 0.01)
    print("proportion de non zéro" , np.sum(dct_thresh != 0.0) / (im.shape[0]*im.shape[1]) )


    vmax=np.max(dct) * 0.01
    plt.subplot(1,2,1)
    plt.imshow(dct, cmap='gray', vmax=vmax, vmin=0)
    plt.title("dct")
    plt.subplot(1,2,2)
    plt.imshow(dct_thresh, cmap='gray', vmax=vmax, vmin=0)
    plt.title("dct thresholded")

    plt.show()


"""reconstruction de l'image par idct"""
def recons(dct_thresh):
    im_size=dct_thresh.shape
    res = np.zeros(im_size)

    for i in np.r_[:im_size[0]:8]:
        for j in np.r_[:im_size[1]:8]:
            res[i:(i + 8), j:(j + 8)] = idct2(dct_thresh[i:(i + 8), j:(j + 8)])
    return res


def step9():
    im = readIm()
    dct = cutAndTransform(im)
    dct_thresh1 = threshold(dct, 0.01)
    dct_thresh2 = threshold(dct, 0.5)
    im_comp1=recons(dct_thresh1)
    im_comp2=recons(dct_thresh2)
    plt.figure()
    plt.imshow(np.hstack((im, im_comp1,im_comp2)), cmap='gray')
    plt.title("Comparison between original and DCT compressed images, 0.1 and 0.3")
    plt.show()



step9()




