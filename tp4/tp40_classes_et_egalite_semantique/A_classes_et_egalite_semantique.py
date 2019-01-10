""""""

""" Les objets servent à structurer les programmes.
    Ils peuvent servir de conteneur à données => objet de type "Modèle"
    Ils peuvent servir à rassembler des méthodes (= fonctions) qui ont un but commun => objet de type "Controler"
    Ils peuvent servir à manipuler des entrées/sorties => objet de type "View"
    Quand on organise bien son code, on parle d'architecture MVC (Model, View, Controler)


    Même si on ne crée pas d'objet, on est obligé d'utiliser les objets créer par les bibliothèques tierces.
    Donc autant savoir comme cela marche
    """

class Man:

    """"""
    """le constructeur. Il sera lancé dès que l'on créera un objet de type Man,
    par exemple quand on code  moi=Man("vincent","vigon")
    Dans le constructeur, on définit la plupart des champs (=variables globales d'une classe).
    Certains champs peuvent être initialisé via les paramètres du constructeur (comme firstName et name ci-dessous)"""
    def __init__(self, firstName:str, name:str):
        """
        :param firstName: Le prénom de la personne
        :param name: Le nom de famille de la personne
        """
        self.name=name
        self.firstName=firstName

        """champ privé (car il commence par un underscore). Il ne pourra pas être vu à l'extérieur de la classe"""
        self._age=0


    """une méthode publique qui modifie un champs privé"""
    def becomeOlder(self): self._age+=1
    """une méthode publique qui permet de lire un champs privé"""
    def getAge(self):return self._age

    """ Une bonne habitude: Créer une méthode qui représente votre objet de manière "sémantique" (=ce qui fait sens).
    Nous décidons ici que deux Man sont 'égaux' quand ils ont même nom et prénom.
    Nous ne prenons pas en compte l'âge"""
    def hashString(self):
        return '['+self.firstName+','+self.name+']'


    """une fonction qui duplique un objet de type Man"""
    def duplicate(self):
        return Man(self.firstName, self.name)

    """une fonction automatiquement appelée par la méthode 'print' de python"""
    def __repr__(self):
        return '[un Man de prénom:'+self.firstName+' et de nom:'+self.name+']'

    """ la méthode __dict__ est bien pratique. Elle transforme votre objet en dictionnaire.
     Voici un exemple d'utilisation pour créer une méthode repr qui affiche tous les attributs publics"""
    def repr2(self):
        dico=self.__dict__
        res=""
        for key in dico.keys():
            if not key.startswith('_'):
                res+=key+":"+str(dico[key])+","
        return res






print("deux variables qui pointent vers le même objet")
man0=Man('Vincent','Vigon')
man1=man0
man1.becomeOlder()

print('man0',man0)#équivaut à print('man0',man0.__repr__())
print('man0',man0.repr2())
print('man1',man1)


print("maintenant en copiant")
man0=Man('Vincent','Vigon')
man1=man0.duplicate()
man2=man0.duplicate()
man1.becomeOlder()
man2.firstName="Joachim"
print('man0',man0)
print('man1',man1)
print('man1',man2)



print("les 3 objets référencés dans man0, man1, man2 sont différents (ils n'ont pas la même adresse mémoire)")
print("mais, selon notre convention, man0 et man1 sont sémantiquement égaux")
dico={}
dico[man0.hashString()]=man0
dico[man1.hashString()]=man1
dico[man2.hashString()]=man2

print(dico)





"""
En fait il y a des méthode __eq__ __hash__ qui permettent de créer le sens des égalités sémantiques de manière canonique
Une fois ces méthodes écrites,  l'opérateur == teste l'égalité sémantique, tandis que 'is' teste l'égalité des références.
  Mais c'est de la programmation plus avancé que je vous invite à découvrir vous même, de manière facultative.
"""












