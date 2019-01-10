from typing import List
from typing import Dict


"""
  Les principales collections possibles en python sont :
  - listes (longueur variable)
  - dictionnaire (clef-valeur)
  - t-uplet (longueur fixe)
  - tableau numpy (cf. prochain tp).

  Nous utilisons aussi le typage qui évite beaucoup d'erreur (uniquement a partir de python 3.5)"""


""" pour commencer voici la syntaxe des fonctions en python"""
def step1():

    def addition(a:float,b:float)->float:
        return a+b

    def division(a:float,b:float)->float:
        if b==0: raise RuntimeError("second arg must be non zero")
        return a/b
    """depuis python3, en divisant deux entiers on tombe sur un réel : 3/2==1.5 par contre 3//2==1  """

    def duplicateEachLetter(word:str)->str:
        res=""
        for letter in word:
            res+=letter+letter
        return res

    print (addition(1,1)) #output 2
    print (division(2,3)) #output 0.66666666666
    print (duplicateEachLetter("toto"))
    """ci-dessous, une erreur (une exception) que nous avions anticipé"""
    # print (division(5,0))
    """vérifiez que l'IDE vérifie bien que les arguments que l'on rentre sont du bon type"""
    return


def step2():
    """"""
    """ création d'un dico et d'une liste avec des expressions littérales dite 'JSON' (utilisées par de nombreux langages)"""
    dictionnaire={'unEntier':3,'unStr':'aba'}
    maListe=[1,2,3,4,5]

    """un dictionnaire est composé de clef et de valeurs. Les clefs sont des string, des entier (ou  des t-uplet).
    Les valeurs peuvent être n'importe quel objet """
    unEntier=3
    unStr='aba'
    dictionnaireBis={'unEntier':unEntier,'unStr':unStr}
    for key in dictionnaireBis : print ("key:",key,"value:",dictionnaireBis[key])


    """création d'un dico élément par élément """
    dico={}
    dico['unEntier']=3
    dico['unStr']='aba'
    dico['unDico']=dictionnaire
    dico['uneListe']=maListe

    print(dico)
    """ il y a deux façon d'accéder aux valeurs : """
    print(dico['unEntier'])#quand on est sur que la clef est présente
    print(dico.get('toto'))#quand on n'est pas sur. Cela renvoie None quand la clef n'est pas présente


    """ les dictionnaires  sont aussi utilisés pour représenter des ensembles (au sens mathématique).
     Dans un ensemble il n'y a pas de répétition"""
    uneListe=[1,2,1,4,1,4,1,1,1,1]
    unEnsemble={}
    for i in uneListe:
        unEnsemble[i]=True
    """pour savoir si 0 est dans l'ensemble """
    print("0 est dans notre ensemble ?:",unEnsemble.get(0))



    """les dictionnaires sont souvent utilisés pour compter des occurences"""
    unePhrase="bonjour bonjour toi toi toi comment va va"
    lesMots=unePhrase.split(sep=" ")
    print(lesMots)
    dico={}
    for mot in lesMots:
        if dico.get(mot) is None: dico[mot]=1
        else: dico[mot]+=1
    print(dico)
    return


"""quelques variantes"""
def step3():
    liste=[]
    for i in range(4):
        liste.append(i*i)
    print("création 1:",liste)

    """en plus court"""
    liste2=[i*i for i in range(4)]
    print("création 2:",liste2)

    print("parcours 1")
    for i in range(len(liste)):
        print("l'élément:",i," vault",liste[i])

    """ou bien"""
    print("parcours 2")
    i=0
    for val in liste:
        print("l'élément:", i, " vault", val)
        i+=1

    """ou bien"""
    print("parcours 3")
    for i,val in enumerate(liste):
        print("l'élément:", i, " vault", val)






"""=================================================================================================================="""
"""
 Création de liste et des dico via des fonctions.
 vérification de typage (pour ceux qui ont python 3.5)"""
def step4():

    def createList(size)->List[int]:
        res=[]
        for i in range(size):
            res.append(i)
        return res


    li=createList(4)
    li.append(0)
    li.append(-1)
    li.extend([0,0,1,5])
    #extend étend la liste existante.
    #alors que "li+[0,0,1,5]" renverrais une nouvelle liste issue de la concaténation.

    """ci-dessous, erreur de typage"""
    #li.append('aze')
    #li.append(3.5)

    print (li)



    def createDico()->Dict[int,str]:
        res={}
        alphabet='abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            res[i]=alphabet[i]
        return res

    didi=createDico()
    print(didi)
    print("cinquième lettre:",didi[4])

    """ci-dessous, erreur de typage"""
    #didi['toto']

    ''' Remarque: nous aurions pu tout autant faire une liste plutôt qu'un  Dict[int,str].'''
    ''' Mais a quel situation un  Dict[int,str] est mieux adapté qu'une simple liste ?
    Pensez à Mettre la réponse dans votre rapport (ainsi que toutes les interrogations cachées dans les commentaire) '''
    return


"""
 Exercice : créer des fonctions encodeur/décodeur qui transforme une phrase en une série de nombre secret
 (par exemple, aléatoirement choisi) et vis-versa.
  Vous devez utiliser pour cela 2 dictionnaires.
  Cette technique de cryptographie est-elle robuste ? Qu'en est-il si chaque motest codé par un entier ? (cf plus loin).
 """

def tocaesar(text,shift):

    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    dic={}
    for i in range(0,len(alpha)):
        dic[alpha[i]]=alpha[(i+shift)%len(alpha)]

    codedtext=""
    for l in text:
        if l in dic:
            l=dic[l]
        codedtext+=l
    return codedtext


def fromcaesar(codedtext,shift):

    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    dic={}
    for i in range(0,len(alpha)):
        dic[alpha[i]]=alpha[(i)%len(alpha)]

    decodedtext=""
    for l in text:
        if l in dic:
            l=dic[l]
        decodedtext+=l
    return decodedtext



def codageNum(text,shift):

    #nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24"]
    #alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    res = []
    for i in text:
        number = ord(i) - shift
        res.append(number)
    return res


def decodageNum(code,shift):
    letters = [chr(n + shift) for n in code]
    decoded = ''.join(letters)
    return decoded


text="feeling like james bond"
shift = 60
print ("Text to code:", text, ";  with shift: ", shift)
print("*********************************")
print ("Coding with letters via dict: ",tocaesar(text,shift))
print ("Decoding with letters: ", fromcaesar( tocaesar(text,shift), shift ))
print("*********************************")
print ("Coding with numbers via list: ", codageNum(text, shift))
print ("Decoding with numbers: ", decodageNum(codageNum(text,shift), shift))




