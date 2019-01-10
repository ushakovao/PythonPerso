
import imageio
import numpy
import matplotlib.pyplot as plt
import numpy as np

"""une fonction utilitaire pour sauver une image couleur"""
def saveRGB(r:np.ndarray,g:np.ndarray,b:np.ndarray,fileName)->None:
    s = r.shape
    couleur = numpy.zeros((s[0], s[1], 3), dtype=numpy.uint8)
    couleur[:, :, 0] = r
    couleur[:, :, 1] = g
    couleur[:, :, 2] = b
    imageio.imwrite("out/"+fileName, couleur)

def showRGB(r:np.ndarray,g:np.ndarray,b:np.ndarray)->None:
    s = r.shape
    couleur = numpy.zeros((s[0], s[1], 3), dtype=numpy.uint8)
    couleur[:, :, 0] = r
    couleur[:, :, 1] = g
    couleur[:, :, 2] = b
    plt.imshow(couleur)
    plt.show()


"""Un histogramme avec des données entière. Facile."""
def histogramme(image):
    """"""
    """ un entier-non signé sur 32 bit est-il suffisant"""
    h = numpy.zeros(256, dtype=numpy.uint32)
    s = image.shape
    for j in range(s[0]):
        for i in range(s[1]):
            valeur = image[j, i]
            h[valeur] += 1
    return h
