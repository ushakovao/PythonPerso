
import  matplotlib
matplotlib.use('TkAgg')
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt


"""
Explorons ensemble une librairie qui créer des "signatures d'images".

Qu'est-ce que d'après vous une signature d'image ? A quoi cela peu servir ?

La librairie se trouve ici
https://github.com/ascribe/image-match
elle s'installe en 1 coup de pip :
sudo pip install image_match

"""

from image_match.goldberg import ImageSignature
gis = ImageSignature()



""" vous pouvez voir les images étudiée en mettant l'url dans votre navigateur.
Ces exemples  font une bonne publicité pour la librairie (c'est ceux proposés par l'aide)
 """
def step0():

    signatures=[]
    """mona lisa"""
    signatures.append(gis.generate_signature('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg'))
    """ mona lisa, avec résolution et éclairage différent"""
    signatures.append(gis.generate_signature('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg'))
    """ mona lista avec un chat dans les mains ! """
    signatures.append( gis.generate_signature('https://upload.wikimedia.org/wikipedia/commons/e/e0/Caravaggio_-_Cena_in_Emmaus.jpg'))
    """ un tableau de Caravage (rien à voir) """
    signatures.append( gis.generate_signature('https://upload.wikimedia.org/wikipedia/commons/e/e0/Caravaggio_-_Cena_in_Emmaus.jpg'))

    n = len(signatures)
    allDistances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            allDistances[i, j] = gis.normalized_distance(signatures[i], signatures[j])

    print("toutes les distances:\n", allDistances)




""" ces exemples là, font une moins bonne publicité.
  Il est possible qu'il faille une complexité minimale pour que la libraire fonctionne"""
def step1():

    signatures = []

    signatures.append(gis.generate_signature('image/gamma_fin1.gif'))
    # L'exemple ci-dessous fait planter la librairie !!!
    #signatures.append(gis.generate_signature('image/gamma_fin2.gif'))
    signatures.append(gis.generate_signature('image/gamma_grand.gif'))
    signatures.append(gis.generate_signature('image/gamma_petit.gif'))
    signatures.append(gis.generate_signature('image/grand_triangle.gif'))


    n=len(signatures)
    allDistances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            allDistances[i, j] = gis.normalized_distance(signatures[i], signatures[j])

    print("toutes les distances:\n", allDistances)


"""  la libraire est aussi capable de gérer les images à rotation et à déformation près. Mais il faut installer
un package supplémentaire pour gérer des bases de données.
Faites le si cela vous tente -> rapport"""


if __name__=='__main__':
    step0()



