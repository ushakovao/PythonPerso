
import numpy as np
import imageio
from PIL import Image
from pylab import *
import  matplotlib.pyplot as plt


"""
Un algorithme de détection de composante connexe dans une image.
Comprenez-le. Faites le tourner pas à pas, sur un papier, avec un dessin.
"""


def add_neighbours_in_stack(image:np.ndarray, threshold:int, stack:list, i:int, j:int, inComponent:np.ndarray)->None:
   inComponent[i, j] = True
   neighbours = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
   for pixel in neighbours:
        (k,l) = pixel
        if 0<=k<image.shape[0] and 0<=l<image.shape[1]:
            """ que ferait l'algo sans la seconde condition ?"""
            if image[k,l]>threshold and not inComponent[k, l]:
                inComponent[k, l] = True
                stack.append(pixel)


def connected_component(image:np.ndarray, seuil:int, i0:int, j0:int, inComponent:np.ndarray)->None:
    stack = [(i0,j0)]
    while len(stack)>0:
        """ pop() est une méthode qui renvoie le dernier élément d'une liste, tout en le supprimant de la liste"""
        (i,j) = stack.pop()
        add_neighbours_in_stack(image, seuil, stack, i, j, inComponent)



def step0():
    img = imageio.imread("../assets/img/1-2.jpg")
    im = array(Image.open('s.jpg').convert('L'))
    image = img[:,:,0]
    print(image.shape)

    inComponent = np.empty(image.shape, dtype=np.bool)
    inComponent[:, :] = False
    connected_component(image, 10, image.shape[0] // 2, image.shape[1] // 2,inComponent)



    plt.imshow(inComponent,cmap='gray',vmin=0,vmax=1)
    plt.show()

    """
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.subplot(1,2,2)
    contour(im, levels=[245], colors='black', origin='image')
    plt.show()"""


if __name__=='__main__':
    step0()



"""
BONUS :
Cette algorithme de détection de zone s'écrirait naturellement de manière récursive
 Ré-écrivez-le en récursif.

L'emploie d'une pile (stack) permet d'éviter la récursivité.
Plus précisément, on crée nous même une pile
que l'ordinateur ferait naturellement dans une procédure récursive. L'avantage de faire nous même notre
pile, c'est qu'on maîtrise mieux les choses ; par exemple on pourrait controler  la hauteur de la pile,
et utiliser le disque dure pour stocker des données quand la pile devient trop haute.

Maintenant, vous devrez comprendre le sens de : "stack-overflow"
"""
