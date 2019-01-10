import imageio
import numpy
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import PIL.ImageOps
from tp7.A_couleur import saveRGB
from tp7.util import histogramme
from tp7.util import showRGB

"""
Une image est en noire-et-blanc (N&B) lorsque les 3 canaux RGB sont égaux.
Ainsi pour transformer une image couleur en N&B il faut effectuer une moyenne pondérée
des composantes RGB de l'image couleur. Les poids doivent prendre en compte le fait que l'oeil humain voit
 certaine couleur plus claire que d'autre.
 """

def step0(naiveWeight:bool):
    img = imageio.imread("../assets/img/rgb1.jpg")

    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    if naiveWeight:
        gray = 0.333 * r + 0.333 * g + 0.333 * b #type: np.ndarray
        """ la formule (r+g+b)/3 ne fonctionne pas, avez-vous une explication ? sinon, vous l'aurez sans doute plus tard """
        saveRGB(gray, gray, gray, "babouin_gris_naif.png")
    else :
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b #type: np.ndarray
        saveRGB(gray, gray, gray, "babouin_gris.png")


    showRGB(gray,gray,gray)

"""Il faut avoir un oeil d'expert pour différencier les poids naifs et les poids officiels."""




"""
Le codage luminance (Y)  chrominance (CbCr) utilise le fait que l'oeil humain est beaucoup
plus sensible à la lumière émise par une image qu'à sa véritable couleur. (ex : si
vous êtes plongé dans un film N&B, vous oubliez très vite qu'il n'y a pas de couleur)

Les composantes Y Cb Cr sont des combinaisons affines de RGB.
La composante Y correspond à l'image en niveau de gris : c'est donc l'image projetée sur le plan
d'équation r=g=b.
 Les deux autre composantes Cb Cr sont des sortes de projection sur des plans orthogonaux à r=g=b.

L'intérêt de ceci est que, pour compresser, on  va  'quantizer' beaucoup plus violemment
 les composantes CbCr que la composante Y.
"""




""" un petit bug c'est cachée dans l'un des programmes ci-dessous.

Voici le commentaire sur stackoverflow de la personne qui a corrigée ce bug.
   <<You have to do your intermediate calculations in floating point.
   The posterization should tip you off; you have a lot of "hot" (saturated) pixels.>>

Ceci illustre l'un des gros défaut (à mon avis) de python. On ne sait jamais trop dans
 avec quel type de données on travaille. A deux petit points prêt, tout change !

Si vous ne trouvez pas : utilisez les programmes d'après.
"""
def rgb2ycbcr_bug(im):
    cbcr = np.empty_like(im)
    r = im[:,:,0]
    g = im[:,:,1]
    b = im[:,:,2]
    # Y
    cbcr[:,:,0] = .299 * r + .587 * g + .114 * b
    # Cb
    cbcr[:,:,1] = 128 - .1687 * r - .3313 * g + .5 * b
    # Cr
    cbcr[:,:,2] = 128 + .5 * r - .4187 * g - .0813 * b

    return np.uint8(cbcr)


def ycbcr2rgb_bug(im):
    rgb = np.empty_like(im)
    y   = im[:,:,0]
    cb  = im[:,:,1] - 128
    cr  = im[:,:,2] - 128
    # R
    rgb[:,:,0] = y + 1.402 * cr
    # G
    rgb[:,:,1] = y - .34414 * cb - .71414 * cr
    # B
    rgb[:,:,2] = y + 1.772 * cb
    return np.uint8(rgb)



""" les même algos en beaucoup plus court et sans le bug.
Essayez de comprendre (avec un calcul sur papier) pourquoi le produit scalaire ci-dessous revient à la multiplication
matricielle ci-dessus //10)*10.
"""
def rgb2ycbcr(im)->np.ndarray:
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128.
    return np.uint8(ycbcr)

def ycbcr2rgb(im)->np.ndarray:
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(np.float)
    rgb[:,:,[1,2]] -= 128.
    return np.uint8(rgb.dot(xform.T))# .T c'est la transposée




def step1_bug():
    img = imageio.imread("../assets/img/babouin_moyen.jpg")
    img_YCbCr= rgb2ycbcr_bug(img)
    img_back=ycbcr2rgb_bug(img_YCbCr)
    plt.subplot(1,2,1)
    plt.imshow(img_back)
    plt.subplot(1,2,2)
    plt.imshow(img)
    plt.show()


""" on fait un aller retour de conversion. Remarquez qu'il y
 a encore des problèmes sur certain pixels. """
def step1():
    img = imageio.imread("../assets/img/test2.png")
    img_YCbCr= rgb2ycbcr(img)

    y  = (img_YCbCr[:, :, 0] )   # type:np.ndarray
    Cb = (img_YCbCr[:, :, 1] // 10)*10 # type:np.ndarray
    Cr = (img_YCbCr[:, :, 2] //10)*10  # type:np.ndarray

    img_back = ycbcr2rgb(img_YCbCr)

    h_red = histogramme(y)
    h_green = histogramme(Cb)
    h_blue = histogramme(Cr)
    maxi = max([h_red.max(), h_blue.max(), h_blue.max()])
    plt.figure(figsize=(8, 6))
    plt.plot(h_red, label='Y')
    plt.plot(h_green, label='Cr')
    plt.plot(h_blue, label='Cb')
    plt.legend()
    plt.axis([0, 255, 0, maxi])
    plt.xlabel("valeur")
    plt.ylabel("Nombre")
    plt.show()


def step3():
    image = Image.open('../assets/img/zebra.jpg')
    inverted_image = PIL.ImageOps.invert(image)
    mirror_im= PIL.ImageOps.mirror(image)
    color_im=PIL.ImageOps.solarize(image,200)
    plt.subplot(1, 4, 1)
    plt.imshow(image)
    plt.subplot(1, 4, 2)
    plt.imshow(inverted_image)
    plt.subplot(1, 4, 3)
    plt.imshow(mirror_im)
    plt.subplot(1, 4, 4)
    plt.imshow(color_im)
    plt.show()

step3()
"""

travail 1: effectuez diverse compression d'images codées en YCbCr
en quantizant les composantes CbCr plus que la Y.
Affichez aussi des histogrammes de couleur.
BONUS: faites une petite GUI (graphic user interface) pour pouvoir régler les quantizations avec des curseurs.
Pour cela, regarder le fichier suivant.

"""

""" travail 2: effectuer des tas de manipulations sur des images,
 notamment des inversions de couleur, des saturations, des superposition ...
Cependant ne faites pas encore des manipulations géométriques (ex : rotation)
 ou des filtrages (ex : floutage, contour)
"""



