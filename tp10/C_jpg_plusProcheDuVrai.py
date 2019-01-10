import numpy as np


"""
Etape 1:
Quantification plus intelligente :
Considérons la matrice M issue de la DCT (reprenez les programmes précédents).
Pour la quantifier, faite (M//Q)*Q où Q est l'une des matrice ci-dessous.
Question :
  laquelle de ces matrices permet-elle la plus grand compression ?
  Quel intérêt de prendre de telles matrices plutôt qu'une matrice constante ?
"""



Q50= np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                [12, 12, 14, 19, 26, 58, 60, 55],
                [14, 13, 16, 24, 40, 57, 69, 56],
                [14, 17, 22, 29, 51, 87, 80, 62],
                [18, 22, 37, 56, 68, 109, 103, 77],
                [24, 35, 55, 64, 81, 104, 113, 92],
                [49, 64, 78, 87, 103, 121, 120, 101],
                [72, 92, 95, 98, 112, 100, 103, 99],
                ])

Q10 = np.array([[80, 60, 50, 80, 120, 200, 255, 255],
                [55, 60, 70, 95, 130, 255, 255, 255],
                [70, 65, 80, 120, 200, 255, 255, 255],
                [70, 85, 110, 145, 255, 255, 255, 255],
                [90, 110, 185, 255, 255, 255, 255, 255],
                [120, 175, 255, 255, 255, 255, 255, 255],
                [245, 255, 255, 255, 255, 255, 255, 255],
                [255, 255, 255, 255, 255, 255, 255, 255],
                ])

Q90 = np.array([[3, 2, 2, 3, 5, 8, 10, 12],
                [2, 2, 3, 4, 5, 12, 12, 11],
                [3, 3, 3, 5, 8, 11, 14, 11],
                [3, 3, 4, 6, 10, 17, 16, 12],
                [4, 4, 7, 11, 14, 22, 21, 15],
                [5, 7, 11, 13, 16, 12, 23, 18],
                [10, 13, 16, 17, 21, 24, 24, 21],
                [14, 18, 19, 20, 22, 20, 20, 20],
                ])




"""
Etape 2 : la lecture en zigzag.


Modifiez le programme zigzag ci-dessous pour créer 2 programmes :
matToList(M) qui transforme une matrice 8x8 en une liste de taille 64 correspondant à la lecture de la la matrice en zigzag
listToMat(L) qui effectue l'opération inverse.
AIDE : il y a très peu de chose à modifier.
Vous pouvez le faire, même sans comprendre précisément la mécanique de la fonction zigzag


Vous allez créer votre propre format de compression pour des images N&B :
Le résultat final sera un fichier texte, le plus court possible qui permettra de stocker les coefficients
quantifiées. Bien entendu, il faudra aussi utiliser la lecture en zigzag des matrices. Mais quel est l'intérêt de la
lecture zigzag par rapport à une lecture ligne par ligne, ou colonne par colonne ?

Comparez les tailles des fichiers obtenus en fonction de la quantification, et aussi en fonction des images : essayez
des images très uniformes et d'autres avec plus de détail.
"""


def zigzag(n:int)->np.ndarray:
    """"""
    """
    d'après https://rosettacode.org/wiki/Zig-zag_matrix.
    Si cela vous amuse, il y a une autre manière de faire : en classant les paires d'incides selon un ordre spécial
    """
    def move(i, j):
        if j < (n - 1):
            return max(0, i - 1), j + 1
        else:
            return i + 1, j

    a=np.zeros((n,n))
    x, y = 0, 0
    for v in range(n * n):
        a[y,x] = v
        if (x + y) & 1:
            x, y = move(x, y)
        else:
            y, x = move(y, x)
    return a
#print(zigzag(5))

"""voici quelques manipulation de string qui pourraient vous servir dans votre travail"""
def stringManip():

    """"""
    """spliter une chaîne de caractère"""
    text="123,123,0x6"
    words = text.split(",")
    print(words)
    """transformer une string en int"""
    print(int(words[0]))

    """couper une string tous les n-caractères"""
    n=2
    line = '1234567890'
    a=[line[i:i + n] for i in range(0, len(line), n)]
    print(a)

    """n'hésitez pas à googler toutes les autres manipulation dont vous rêvez. ex: <<python3 save string to file>>  """


"""
Pour faire le vrai JPEG, il manque encore 2 étapes : gérer les couleurs, et gérer l'encodage des chiffre.

L'encodage est un peu techniques : chaque nombre est encodé par une suite de bite selon des règles bien précises
(cf. https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/jpegUpToQuant.html)
 Il faut quand même savoir qu'il s'agit d'un encodage de Huffmann dont le principe est de coder
les nombres les plus fréquent en un minimum de bit, avec la contrainte suivante : aucune suite de bit utilisée ne doit
être la préfixe d'une autre suite de bit utilisée (pourquoi ?).

Par contre, en bonus, vous pouvez coder la compression des images couleur, en réutilisant les codes précédents :
1/ Transformer une image RGB en YCrCb.
2/ Sous échantillonnez les composantes Cr Cb : pour chaque carré 2*2, gardez uniquement sa moyenne.
3/ Appliquez votre algo JPEG sur les 3 matrices.
4/ Implémentez l'algo de décompression correspondant.
5/ Faites tourner cet algo avec différentes quantification, différentes images. Eventuellement, comparez cet algo avec
l'ago naïf qui consiterait à compresser directement les 3 matrices R,G,B sans le sous-échantillonnage.

"""