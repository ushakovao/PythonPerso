
from typing import List


""""""
'''  voici 4 bouts de code qui font la même chose: ils suppriment des éléments dans une liste, ces éléments à supprimer
sont désignés par leur indices.

 Le troisième ne fonctionne pas comme on le souhaiterait.
  Cela illustre ce qui est pour moi une des grandes difficulté de l'informatique à savoir : le passage d'argument par adresse '''


def step0():

    """"""
    '''voici une méthode directe pour supprimer plusieurs éléments d'un coup dans un tableau :
    l'idée, c'est qu'on crée un nouveau tableau
    '''
    array=['a','b','c','d']
    indices=[1,3]
    res=[]
    for i in range(len(array)):
        if i not in indices: res.append(array[i])
    array=res
    print('sans appel de fonction',array)



def step1():
    """"""
    '''on fait la même chose dans une fonction'''
    def arrayMinusIndices(array:List,indices:List[int])->List:
        res=[]
        for i in range(len(array)):
            if i not in indices: res.append(array[i])
        return res
    array=['a','b','c','d']
    indices=[1,3]
    array=arrayMinusIndices(array,indices)
    print('arrayMinusIndices',array)

"""remarquez tout de même que cette suppression nécessite une double boucle (mais où se trouve la seconde boucle)?
A la fin de ce tp vous serez comment faire la même chose en une seule boucle. Mais ce n'est vraiment nécessaire que
si la liste d'indice est très longue."""



def step2():
    """"""
    '''Une technique informatique  est dite "InPlace" lorsqu'elle ne créer pas de copie d'objet (pas de res=[]).
       Par exemple, si vous voulez changer 1 élément dans un tableau de taille 1000, il vaut mieux utiliser une technique InPlace.
       Par contre si vous voulez supprimer 50% des éléments d'un tableau, il vaut mieux créer un nouveau tableau comme nous avons fait précédemment.'''

    def deleteIndicesInPlace(array: List, indices: List[int]) -> None:
        for i in indices: del array[i]
        return

    array = ['a', 'b', 'c', 'd']
    indices = [0, 1]
    deleteIndicesInPlace(array, indices)
    print('deleteIndicesInPlace', array)

    """Si vous contiez supprimer 'a' et 'b' c'est raté"""


""" Si vous devez modifiez une listes :
  - Si vous changer des éléments : utiliser une technique inPlace
  - si vous l'étendez : utiliser une technique inPlace
  - sinon créer une copie de la liste

  Si vous avez de très grandes listes et que vous avez besoin d'insérer ou de supprimer des éléments au milieux,
  il faut alors penser à utiliser une autre structure de collection (les listes chaînées). Mais cela ne nous arrivera pas.

  """

