


def step0():

    paire='P','F'
    triplet=(1,2,3) #les parenthèses sont facultative
    print('paire, triplet',paire, triplet)

    """les t-uplet sont immutable : on ne peux pas les modifier"""
    """Ainsi l'opération ci-dessous n'est pas possible (l'IDE vous le dira)"""
    #triplet[0]=2

    print('triplet[0]',triplet[0])

    """bien pratique en python : l'affectation multiple"""
    a,b,c=triplet
    print('a,b,c', a, b, c)


    """l'affectation multiple surtout utilise dans les fonctions"""
    def twoResults(a,b):
        return a+b,a-b
    c,d=twoResults(1,2)
    print('c,d',c,d)


def step1():

    paire=({'a':3},[1,2,3])

    paire[0]['a']=0
    paire[1][0]=0

    print('paire',paire)

    """ un tuplet est immutable, mais jusqu'à un certain niveau ... Expliquez   """


def step2():

    """"""
    """dans les fonctions on peut mettre des arguments avec des valeurs par défaut, dans ce cas ils sont facultatifs"""

    def additionne(a:float,b:float,precision:int=1)->float:
        res=a+b
        return round(res,precision)

    """variante"""
    def additionne2(a:float,b:float,precision:int=None)->float:
        res=a+b
        if precision is None: return res
        else : return round(res,precision)


    print(additionne(2.1234,3,precision=2))
    print(additionne(2.1234, 3))

    """les valeurs par défaut doivent être immutable ! donc on peut mettre un t-uplet mais pas une liste"""














