

"""
Commencez par lire l'autre fichier "Polynome"
Ensuite :


Créer les polynômes de legendre avec la formule récursive suivante :
(n+1)P_{n+1}(x) = (2n+1) x P_{n}(x)- n P_{n-1}(x)
P_0=1
P_1=x



Il y a 2 manières de faire ce tp :

Si vous pensez avoir bien réussi votre classe Polynome, utilisez la technique "semi-formelle".
Sinon utilisez la technique "purement numérique". Indiquez dans votre rapport les avantages
de l'une ou l'autre des techniques.


TECHNIQUE NUMERIQUE :
En vous inspirant du step0 ci-dessous, définissez les polynomes de Legendre. Normalisez-les.
Pour calculer les produits scalaires, il faut calculer des intégrales : utilisez la méthode des rectangles
 comme nous l'avons fait avec les sin-cos.
Vérifiez l'orthonormalité. Faites des approximations de fonctions avec cette base des polynômes.


TECHNIQUE SEMI_FORMELLE :
Définissez les polynomes de Legendre à l'aide de votre classe Polynomes. Vérifiez l'orthonormalité.
Pour calculer des produits scalaires entre polynomes,  utilisez la technique d'intégration formelle (via la primitive).
Faites des approximations de fonctions avec cette base des polynômes : à partir du moment où l'on travaille avec des
fonctions non-polynomiale, on n'a plus le choix : on doit quitter les méthodes formelles et faire de l'intégration numérique.
Utilisez simplement la méthode des rectangles.

Question supplémentaire : considérons la matrice M[i,j]=sca(x^i,x^j). Comme pourriez-vous utiliser cette matrice pour calculer
les coordonnées d'un polynome p dans la base des polynomes de Legendre ?

"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

import matplotlib.pyplot as plt
import numpy as np

left = -1.0
right = 1.0
nbStep = 100
sizeSt=(abs((left-right))/nbStep)

for n in range(5):
    Pn = legendre(n)
    x = np.arange(left,right+sizeSt,sizeSt)
    y = Pn(x)
    plt.plot(x, y)
plt.show()




def step0():
    nbPoints=1000
    x=np.linspace(-1,1,nbPoints)

    poly=5*x**3 - x**2 - x + 3

    plt.plot(x,poly)
    plt.show()






