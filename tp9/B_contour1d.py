import numpy as np
import matplotlib.pyplot as plt


"""un signal lisse"""
def buildSignal()->np.ndarray:
    a=50
    dec=30
    x=np.linspace(-a,a,1000)
    y1=np.arctan(x+dec)
    y2=np.arctan(-x+dec)
    return y1+y2


"""calculons la dérivée discréte de notre signal"""
def step0():
    y=buildSignal()
    yPlus1=np.empty_like(y)
    yPlus1[0]=0
    yPlus1[1:]=y[:len(y)-1]

    yDiff =  y - yPlus1
    plt.plot(yDiff)
    plt.show()


"""Supposons que ce signal soit une image 1d en niveau de gris.
Les valeurs hautes correspondant au blanc, les basses au noir.
Détecter les 'contours' dans l'image, revient à détecter les variations brusques.

Comment, avec la dérivée première, peut-on repérer les contours ?
Appliquez cela au signal précédent (si vous n'avez pas d'idée, vous pouvez passer au fichier suivant, les idées s'y trouvent).
AIDE :  vous Tracerez la fonction qui à chaque indice (=pixel) associe la valeur 1 si il correspond à
un contour, et la valeur 0 sinon.


Essayez de faire le même travail, mais en utilisant la dérivée seconde discrète (différence finie).
Si vous ne savez pas faire, c'est une honte (demandez moi quand même).

"""



