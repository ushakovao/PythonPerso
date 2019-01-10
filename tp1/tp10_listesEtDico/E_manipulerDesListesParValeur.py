from typing import List
from typing import Dict
import time

''' Voici maintenant différentes fonctions qui supprime des éléments d'un tableau par valeur (et non plus par indice).
 Nous faisons également un test de performance qui vous montrera la puissance des dictionnaires (grâce aux tables de hachage qu'il y a derrière) '''

def step3():

    def deleteValuesInPlace0(array: List, valuesToSuppress: List) -> None:
        for elem in valuesToSuppress: array.remove(elem)
        return


    def deleteValuesInPlace1(array:List, valuesToSuppress:List)->None:
        for elem in valuesToSuppress:
            if elem in array: array.remove(elem)
        return

    def deleteValuesInPlace2(array:List, valuesToSuppress:List)->None:
        for elem in valuesToSuppress:
            try:
                array.remove(elem)
            except ValueError:
                pass
        return

    """pourquoi deleteValuesInPlace1 est deux fois plus longue que deleteValuesInPlace2 ?
    pourquoi deleteValuesInPlace0 plante ? """

    def deleteValues3(array:List, valuesToSuppress:List)->List:
        dico={}
        for elem in valuesToSuppress:
            dico[elem]=True
        res=[]
        for elem in array:
            if  dico.get(elem) is None: res.append(elem)
        return res


    import numpy as np

    def createData(size:int):
        data = []
        for a in range(size):
            data.append(str(a))

        perm=np.random.permutation(size)
        perm=perm[0:int(size/2)]
        dataToSuppress=[data[i] for i in perm]
        '''on rajoute une valeur à supprimer qui n'est pas  dans les data'''
        dataToSuppress.append('-1')
        return data,dataToSuppress


    # perm=np.random.permutation(6)
    # print(perm[1:4])
    # print(createData(6))



    size=20000

    data,dataToDelete=createData(size)
    t=time.time()
    deleteValuesInPlace1(data,dataToDelete)
    print('deleteValuesInPlace1:',time.time()-t)


    data,dataToDelete=createData(size)
    t=time.time()
    deleteValuesInPlace2(data,dataToDelete)
    print('deleteValuesInPlace2:',time.time()-t)

    data,dataToDelete=createData(size)
    t=time.time()
    deleteValues3(data,dataToDelete)
    print('deleteValues3:',time.time()-t)


    print("deleteValuesInPlace 1 et 2  : en plus d'être lente, elles ne marchent pas vraiment comme il faudrait ")
    data=['1','1','1','2']
    deleteValuesInPlace1(data,['1'])
    print(data)

    data=['1','1','1','2']
    deleteValuesInPlace2(data,['1'])
    print(data)

    print('deleteValues3 est parfaite en plus d être 1000 fois plus rapide')
    data=['1','1','1','2']
    data=deleteValues3(data,['1'])
    print(data)

    return


def intersection( a, b):
    result = []
    for i in a:
        for j in b:
            if i == j and i not in result:
                result.append(i)
    return result

print (intersection([0,1,2,3], [2,3,4,5 ]))





