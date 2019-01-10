
import imageio
import numpy
import matplotlib.pyplot as plt
import numpy as np
from tp7.util import saveRGB, histogramme

"""
inspiration :
http://www.f-legrand.fr/scidoc/docmml/image/niveaux/images/images.html """


def step0():
    img = imageio.imread("../assets/img/rgb.png")

    """La taille de l'image, repérez la dimension verticale et la dimension horizontale  """
    print(img.shape)
    """  uint8 -> entier non signé, codé en 8bit. Donc une échelle de 0 à 255=2^8-1 """
    print(img.dtype)

    """3 canaux : R,G,B = Red,Green,Blue.
    Ces trois couleurs se mélangent pour donner toutes les couleurs possibles"""
    red = img[:,:,0]
    green = img[:,:,1]
    blue = img[:,:,2]

    """observons un bout de la matrice"""
    print(red[0:20,0:20])

    img[0:100,0:50,:]=0
    plt.subplot(2,2,1)
    plt.imshow(img)
    plt.subplot(2, 2, 2)
    plt.title("red")
    plt.imshow(red)
    plt.subplot(2, 2, 3)
    plt.title("green")
    plt.imshow(green)
    plt.subplot(2, 2, 4)
    plt.title("blue")
    plt.imshow(blue)

    plt.show()



    """question :
     comment les zones blanches/noires ressortent sur les 3-composantes RGB ?

     Quel est le lien entre les indices lignes/colonnes des matrices et les coordonnées x/y des images...
     (Pour s'en souvenir : rappelez-vous comment vous dessiniez les matrices en cours d'algèbre linéraire)

     Dans le code précédent, pourquoi quand on modifie img, cela modifie red/green/blue ?

     """

step0()
"""on met un canal à zéro. Observez l'image produite."""
def step2():
    img = imageio.imread("../assets/img/ernst.jpg")
    g = img[:, :, 1]
    b = img[:, :, 2]

    saveRGB(np.zeros(g.shape),g,b,"ernst_sr.png")

def step2a():
    img = imageio.imread("../assets/img/ernst.jpg")
    r = img[:, :, 0]
    b = img[:, :, 2]

    saveRGB(np.zeros(r.shape),r,b,"ernst_sg.png")

def step2b():
    img = imageio.imread("../assets/img/ernst.jpg")
    r = img[:, :, 0]
    g = img[:, :, 1]

    saveRGB(np.zeros(g.shape),g,r,"ernst_sb.png")



def step3():

    img = imageio.imread("../assets/img/g2.png")
    red = img[:, :, 0]
    green = img[:, :, 1]
    blue = img[:, :, 2]

    h_red = histogramme(red)
    h_green = histogramme(green)
    h_blue = histogramme(blue)
    maxi=max([h_red.max(),h_blue.max(),h_blue.max()])
    plt.figure(figsize=(8, 6))
    plt.plot(h_red,c='red')
    plt.plot(h_green,c='green')
    plt.plot(h_blue,c='blue')
    plt.axis([0, 255, 0, maxi])
    plt.xlabel("valeur")
    plt.ylabel("Nombre")

    plt.show()

"""Que  teste-t-on dans ce step ? """
def step4():
    a=np.random.randint(0,255,(5,5))
    print(a)
    a//=10
    a*=10
    print(a)


"""Observez la manipulation suivante, que l'on appelle la quantization des couleurs. Quel est son intérêt ?
"""
def step5():

    img = imageio.imread("../assets/img/g2.jpg")
    red = (img[:, :, 0]//10 )*10  #type:np.ndarray
    green = (img[:, :, 1]//10)*10 #type:np.ndarray
    blue = (img[:, :, 2]//10)*10  #type:np.ndarray

    h_red = histogramme(red)
    h_green = histogramme(green)
    h_blue = histogramme(blue)
    maxi=max([h_red.max(),h_blue.max(),h_blue.max()])
    plt.figure(figsize=(8, 6))
    plt.plot(h_red,c='red')
    plt.plot(h_green,c='green')
    plt.plot(h_blue,c='blue')
    plt.axis([0, 255, 0, maxi])
    plt.xlabel("valeur")
    plt.ylabel("Nombre")

    saveRGB(red,green,blue,'babouin_quantize.png')

    plt.show()



def step7():
    img = imageio.imread("../assets/img/bb.jpg")

    red = img[:, :, 0]
    green = img[:, :, 1]
    blue = img[:, :, 2]


    nb_rows, nb_cols = red.shape
    row, col = np.ogrid[:nb_rows, :nb_cols]
    cnt_row, cnt_col = nb_rows / 2, nb_cols / 2
    outer_disk_mask = ((row - cnt_row) ** 2 + (col - cnt_col) ** 2 >(nb_rows / 2) ** 2)
    red[outer_disk_mask] = 0
    green[outer_disk_mask] = 0
    blue[outer_disk_mask] = 0



    img[0:100,0:50,:]=0
    plt.subplot(2,2,1)
    plt.imshow(img)
    plt.subplot(2, 2, 2)
    plt.title("red")
    plt.imshow(red)
    plt.subplot(2, 2, 3)
    plt.title("green")
    plt.imshow(green)
    plt.subplot(2, 2, 4)
    plt.title("blue")
    plt.imshow(blue)

    plt.show()



    """Effectuer ce travail d'encerclement sur les 3 composantes RGB puis exporter l'image couleur.
    Petit défit : vous pouvez le faire sans rajouter de ligne de code
    en traitant les 3 composantes en même temps"""

    saveRGB(red, green, blue, 'my.png')


step3()