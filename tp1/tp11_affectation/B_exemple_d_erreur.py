

from typing import List
from typing import Dict

"""expliquez pourquoi un des Modifier marche et un ne marche pas"""


def step1():

    class Modifier1:
        def __init__(self, liste: List, otherListe: List):
            self.liste = liste
            self.otherListe = otherListe

        def changeArray(self):
            self.liste.extend(self.otherListe)

    liste = [1, 2, 3]
    otherListe = [4, 5, 6]
    modifier = Modifier1(liste, otherListe)
    modifier.changeArray()
    print(liste)


def step2():
    class Modifier2:
        def __init__(self, liste:List, otherListe:List):
            self.liste = liste
            self.otherListe=otherListe

        def changeArray(self):
            self.liste = self.liste+self.otherListe

    liste = [1, 2, 3]
    otherListe=[4,5,6]
    modifier = Modifier2(liste, otherListe)
    modifier.changeArray()
    print(liste)









