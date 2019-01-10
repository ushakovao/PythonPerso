

""" PASSAGE PAR VALEUR : uniquement les nombres et les strings """
""" Il faut imaginez que les variables contiennent les nombres ou les strings  """
a1="AAAAAA"
""" on crée un nouvelle variable a2 qui reçoit le contenu de a1 """
a2=a1
a2+="BBBBBB"
""" ce print là signifie moi: affiche moi le contenu de a1 et a2 """
print("a1,a2",a1,a2)



"""PASSAGE PAR ADRESSE : tous les autres objets """
""" Il faut imaginez que les variables contiennent des adresses mémoire """
point1={'x':3,'y':5}
""" on crée un nouvelle variable point2 qui reçoit le contenu de point1 (une adresse)"""
point2=point1
point2['x']=4
""" ce print là signifie : affiche moi les objets aux adresses indiquées par le contenu de point1 et point2 """
print("point1,point2",point1,point2)


"""  Voilà pour la première difficulté. En M2 je pense que vous avez déjà tous surmonté cette difficulté."""
""" Mais attention, ne pas  assimiler le contenu de la variable (ici une adresse) et le contenu de la case mémoire (ici l'objet {'x':4,'y':5})"""
""" Par exemple: on vide la variable point2.  """
point2=None
"""pour autant on ne détruit pas l'objet sous-jacent"""
print("point1",point1)
""" par contre si on vide la variable point1 aussi """
point1=None
"""il n'y a plus personne qui pointe vers l'objet sous-jacent, qui sera alors détruit par le ramasse miette"""





"""ATTENTION: tout comme une affectation, l'appel d'une fonction cache la création et la copie d'une variable,
et ceci dans tous les cas (que la variable contiennent une string, un nombre, ou une adresse)"""

def toto(b):
    b={"hoho":7}
    return


"""un passage par valeur"""
b=5
toto(b)
""" la variable b n'a pas changée. Elle contient toujours 5  """
print("b",b)


""" un passage par adresse """
b={'x':3,'y':5}
toto(b)
""" la variable b n'a pas changée, elle contient toujours l'adresse de '{'x':3,'y':5}' """
print("b",b)

""" lorsque l'on lance toto(b), l'ordinateur commence par faire b2 =b  : il crée une variable locale b2 dans lequel il transfert le contenu de la variable d'entrée.
  Pour que ce soit plus clair, vous pouvez renommer à la main la variable  b à l'intérieur de toto()
  """



""" Créons maintenant une fonction qui fait quelque chose  """
def tata(point):
    point['x']=0
    return

point={'x':1,'y':1}
tata(point)
""" en effectuant point['x']=0 on a agit sur l'objet sous-jacent (alors que dans la fonction toto, on n'agissait que sur la variable locale b2 )"""
print("point",point)






















































