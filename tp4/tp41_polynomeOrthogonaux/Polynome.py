
"""
Une classe Polynome à compléter vous-même avec plein de méthode utiles.
Remarques : si vous n'arrivez pas au bout de ce travail, vous pouvez quand même faire le travail associé aux polynomes
orthogonaux (cf autre fichier)
"""

"""
Remarque : cette classe est destinée à être réutilisée dans d'autre fichier.
Quand c'est le cas : C'est une bonne habitude de donner le même nom à la classe et au fichier.
Et surtout : ne pas mettre de code exécutable dans ce fichier en dehors d'un petit programme test, qui
doit être précédé de:
        if __name__=="__main__":
"""


import numpy as np

class Polynome:
    def __init__(self,coef):
        """
        :param coef: an iterable of numbers (int or float, then converted into float)
        """
        try: self.coef = np.array(list(coef),dtype=np.float64)#conversion en float pour éviter les mauvais gag
        except Exception: raise ValueError("coef must be an iterable")
        for i in self.coef:
            if not isinstance(i , float) : raise ValueError("arg must be made of numbers")



    """la première méthode est données, vous devez implémenter les autres"""
    def __add__(self, other):

        if not isinstance(other,Polynome): raise ValueError("arm must be a Polynome")

        nbCoef=max(len(self.coef),len(other.coef))
        resCoef=np.zeros(nbCoef)
        resCoef+=self.coef
        resCoef+=other.coef

        return Polynome(resCoef)


    def __minus__(self, other):

        if not isinstance(other,Polynome): raise ValueError("arm must be a Polynome")

        nbCoef=max(len(self.coef),len(other.coef))
        resCoef=np.zeros(nbCoef)
        resCoef-=self.coef
        resCoef-=other.coef

        return Polynome(resCoef)



    """Cette méthode vous dira comment réagira votre objet à l'opérateur +=
    Suivez la tradition de python, faites un méthode in-place : ne  recréer pas de nouvel objet.
     (même si dans ce cas précis, cela a très peu d'intérêt)"""
    def __iadd__(self, other):
        return None


    """ calcul une primitive du polynôme. Vous avez le choix entre une méthode in-place et ou non.
     Quelle est la plus judicieuse ? """

    """
    def a_primitive(self,constant_coel=0):
        nbCoef = len(self.coef)
        resCoef = np.zeros(nbCoef)
        for i in range(nbCoef):
            resCoef=self.coef/ (i+1)
        resCoef=np.concatenate([[0.],resCoef])
        return Polynome(resCoef)
"""

    def a_primitive(self, constant_coel=0):
        resCoef = [0]
        for i in range(len(self.coef)):
            res = self.coef[i] / (i + 1.)
            if res == int(res): res = int(res)
            resCoef.append(res)
        return Polynome(resCoef)

    def a_derivative(self):
        resCoef = []
        for i in range(0, len(self.coef)): resCoef.append(i * self.coef[i])
        return Polynome(resCoef)



    """ multiplication de 2 polynômes ou bien d'un polynôme avec un number.
    Attention, c'est la partie difficile. Essayer de voir qu'il faut en fait effectuer une convolution.
    Puis utiliser la convolution de numpy (ou bien faites le à la main pour rigoler)"""


    def __mul__(self, other):
        """
        :param other: an other polynome or a number
        :return: the multiplication between self and the polynome other, or the scalar multiplication with other
        """
        if isinstance(other, int):
            nbCoef = len(self.coef)
            resCoef = np.zeros(nbCoef)
            for i in self.coef:
                resCoef=self.coef*other
            return( Polynome(resCoef))
        elif isinstance(other, Polynome):
            resCoef = [0] * (len(other.coef) + len(self.coef) - 1)
            for ind1, coef1 in enumerate(self.coef):
                for ind2, coef2 in enumerate(other.coef):
                    resCoef[ind1 + ind2] += coef1 * coef2
            return Polynome(resCoef)
        else:
            raise ValueError("argument must be a number or an other Polynôme")

    """Remarque : je vous incite ci-dessus à faire un programme souple, qui n'a pas le même comportement si l'argument
    est un nombre ou bien un polynome :  une telle souplesse est-elle toujours souhaitable ?
    """
    """
    def __repr__(self):
        return str(self.coef)
    """

    def __repr__(self):

         joiner = {
             (True, True): '-',
             (True, False): '',
             (False, True): ' - ',
             (False, False): ' + '
         }

         result = []
         for power, coeff in reversed(list(enumerate(self.coef))):
             j = joiner[not result, coeff < 0]
             coeff = abs(coeff)
             if coeff == 1 and power != 0:
                 coeff = ''

             f = {0: '{}{}', 1: '{}{}x'}.get(power, '{}{}x^{}')

             result.append(f.format(j, coeff, power))

         return ''.join(result) or '0'



    """ pour la méthode suivante vous pouvez utiliser la méthode naive, ou bien la méthode de Hörner si vous avez du temps"""


    def evaluation(self, left:float, right:float, nbStep=10)->np.ndarray:
        points = (right - left) / nbStep;
        nbCoef = len(self.coef);
        res = np.zeros(nbCoef)
        for k in range(nbCoef):
            for i in range(nbStep):
                res=res*points+self.coef
        return res

    """pour calculer l'intégrale de ce polynôme vous avez 2 possibilités: une numérique (via toNumpyArray)
    et une formelle (via ???).
    Choisissez la plus précise, ou bien implémentez les deux"""
    def integrale(self,left:float,right:float)->float:
        #TODO
        return None







    """ cette méthode servira à définir l'égalité sémantique des polynômes.
    cela peut-être une version allégée de __repr__  Il serait sympa que deux polynômes 'très proche' soient sémantiquement égaux.
     """
    def hashString(self):
        #TODO
        return None





"""petit programme test"""
if __name__=="__main__":

    """vérifions que les entrées soient bien vérifiées"""
    #Polynome(3)
    #Polynome("aze")
    #Polynome([3,'a'])

    p1=Polynome([1,0,3,4])
    p2=Polynome([2,1,0,2])
    print("P1",p1)
    print("P2", p2)
    print ("P1 + P2", p1+p2)
    print("P1 add P2", p1.__add__(p2))
    print("P1 mul P2", p1.__mul__(p2))
    print("P1 mul const=5", p1.__mul__(5))
    print("P1.primitive", p1.a_primitive())
    print("P1.derivative", p1.a_derivative())
    print("P1.eval(-1,1,10)", p1.evaluation(-1,1,10))



