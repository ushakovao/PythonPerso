

import numpy as np


"""====================================================== QUELQUES ERREURS CLASSIQUE ============================================================"""

def step1():
    """"""
    """ attention, contrairement au dictionnaire, dans un tableau, il faut avoir créer un élément avant de l'appeler """
    tab=[]
    '''une erreur qui n'en aurait pas été une si tab était un dictionnaire  '''
    #tab[0]='AE'
    ''' l'utilisatino classique des liste est'''
    tab.append('toto')
    tab.append('tata')
    tab.append('tutu')
    for i in range(len(tab)): print(tab[i])

def step2():
    """"""
    '''si on veut créer un tableau vide de taille donnée on peut l'inialiser comme ceci'''
    tabSize4=[None for i in range(4)]
    tabSize4[3]='AES'
    tabSize4[0]='BONBON'
    print('tabSize4',tabSize4)


def step3():
    """"""
    '''créons par exemple un tableau de tableau '''
    tabOfTabSize5= [[] for j in range(5)]
    tabOfTabSize5[3].append(5)
    tabOfTabSize5[3].append(2)
    tabOfTabSize5[1].append(6)

    print("tabOfTabSize5",tabOfTabSize5)



def step4():
    """"""
    '''Mais souvent, si vous avez besoin d'initialiser une liste, et que cette liste doit contenir des nombre,
    il vaut mieux crée un tableau numpy'''
    tabSize4=np.zeros(4)
    tabSize4[2]=4
    '''mais c'est un autre TP'''






