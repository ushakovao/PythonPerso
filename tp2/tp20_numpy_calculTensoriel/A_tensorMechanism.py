import numpy as np
import matplotlib.pyplot as plt


np.set_printoptions(linewidth=500)

'''créer un tenseur. Accéder à ses éléments. Connaître sa forme (shape)'''
def step1():
    tensor1=np.array([[1,2,1],[3,4,3]])
    grosTenseur=np.array([[[1,2,0],[3,4,0]],[[5,6,0],[7,8,0]]])

    print("tensor1\n",tensor1)
    print("shape(tensor1)\n",tensor1.shape)
    print("tensor1[0,1]\n",tensor1[0,1])
    print("tensor1[0,:]\n",tensor1[0,:])
    print("grosTenseur\n",grosTenseur)
    print("grosTenseur\n",grosTenseur.shape)

    '''apprenez très vite à repérer les indices 0,1,2 dans les sorties consoles.
    Exemple1: l'indice 0 balaye les lignes, l'indice 1 balaye les colonnes
    tensor1
    [[1 2 1]
    [3 4 3]]

    Exemple2:
    grosTenseur
    [[[1 2 0]
     [3 4 0]]

    [[5 6 0]
      [7 8 0]]]

    voici comment sont les indices
    [i=0: [ j=0:[ k=0 k=1 k=2]
            j=1:[ k=0 k=1 k=2]]

    [i=1: [ j=0:[ k=0 k=1 k=2]
            j=1:[ k=0 k=1 k=2]]

    '''

    return

def exo1():
    """"""

    print( "**Partie 1**")

    a =np.array(range(4))
    b=np.array(range(3))
    print ("a\n",a)
    print ("b\n", b)

    c=np.array([[i*j for i in a] for j in b ])
    print("c\n", c)

    d = np.array([[i*j-i-j for i in a] for j in b ])
    print ("d\n", d)

    e = np.array([[i*j-i*j+i+j for i in a ] for j in b ])
    print("e\n", e)

    e_sum_col = np.sum(e, axis =0)
    print("e_sum by columns\n", e_sum_col)

    e_sum_raw = np.sum(e, axis =1)
    print("e_sum by rows\n", e_sum_raw)

    e_sum_total = np.sum(e)
    print("e_sum total\n", e_sum_total)

    print("**Partie 2**")

    x = np.array([[0, 1], [3, 4]])
    y = np.array([[5, 6], [7, 8], [9,0]])

    """matmul + transpose"""

    print("x.shape: ", x.shape, "  and y.shape:  ", y.shape)
    y_t=np.transpose(y)
    print("matmul(x,y) \n", np.matmul(x, y_t))
    #print("matmul(l,m)", np.matmul(m, l)) - ERROR

    """**expand_dims**"""

    new_x = np.expand_dims(x,1)
    new_y = np.expand_dims(y,0)


    print("Add dims: shape of new x", new_x.shape)
    print("Add dims: shape of new y", new_y.shape)

    new_m = new_x*new_y
    print("Result \n", new_m )
    print("and its shape", new_m.shape) #ASK!!!

    return



"""  a1 = [[1, 0], [0, 1]]
    b1 = [1, 2]
    m  =[3, 4]
    l = [[5,6],[1,2]]
    print(np.matmul(m,l))

    X = np.random.rand(5, 10)
    Y = X - X.mean(axis=1, keepdims=True)
    print (X)
    print(Y)

    A2 = np.random.rand(2, 2)
    B2 = np.random.rand(2, 2)
    print(A2)
    print(B2)
    print ("np.diag(np.dot(A2, B2))",np.diag(np.dot(A2, B2)))
    print("np.sum(A2 * B2.T, axis=1)", np.sum(A2 * B2.T, axis=1));"""


exo1()






''' numpy fait une différence entre les entiers (ex: 5) et les float (ex: 5. ou 5.5 ou 5/3)'''
def step2():
    x=np.array([5,5])
    '''Dès qu'il y a un float dans un tenseur, tout le tenseur est mis en float'''
    y=np.array([5.,5])
    print('x',x,'\ny',y)

    ''' quand on additionne, c'est le type float qui gagne  '''
    z=x+y
    print('z',z)

    '''Attention, seul les entiers peuvent servir d'indice'''
    a=np.array([0,2,4,6,8,10])
    '''vous pouvez supprimer la ligne ci-dessous, si
    dans la ligne ci-dessus vous changer le 0 en 0.0 '''
    a=a.astype(np.int32)
    x=np.linspace(0,100,50)
    print('x\n',x)
    """on extrait un sous tenseur"""
    print('x[a]\n',x[a])

    return


"""opération élémentaire sur un tenseur"""
def step3():
    tensor1= np.ones(shape=[3, 2])
    tensor2= np.transpose(tensor1)
    tensor3= np.sum(tensor1,1)
    tensor4= tensor1*3
    tensor5=tensor1+tensor1

    print("tensor1\n",tensor1)
    print("tensor2\n",tensor2 )
    print("tensor3\n",tensor3 )
    print("tensor4\n",tensor4 )
    print("tensor5\n",tensor5 )
    print("tensor1\n",tensor1 )

    """vérifiez que toutes ces opération n'ont pas affecté le tensor1"""
    return


"""comment utiliser des dimensions supplémentaires pour éviter des boucles (et ainsi rendre possible l'optimisation)
Attention: l'extension de dimension est difficile au début. Conseil : toujours écrire les indices comme ci-dessous.
CE STEP EST TRèS IMPORTANT
"""
def step4():
    size=3
    data=[i for i in range(size)]

    """deux vecteurs 'lignes' """
    tensor1 =np.array(data)
    tensor2=np.array(data)
    """tensor1Exp_ij=tensor1_j """
    tensor1Exp=np.expand_dims(tensor1,0)
    """tensor2Exp_ij=tensor2_i """
    tensor2Exp=np.expand_dims(tensor2,1)
    """
    tensor3_ij= tensor1Exp_ij + tensor2Exp_ij
              = tensor1_j + tensor2_i
    la fonction tf.add adapte les tailles, pour permettre une addition: C'est tous à fait naturel: nous le faisons aussi
    """
    tensor3=tensor1Exp+tensor2Exp

    """on peut additionner,multiplier, soustraire,  des tenseurs de dimensions différentes.
    Par défaut numpy fait des expand_dims(,0). Cette adaptation des tailles s'appelle le 'broadcast' """
    tensor4=np.array([[1.,2,3],[4,5,6]])
    tensor5=np.array([10.,10,10])
    tensor6=np.array([100.])
    tensor7=tensor4+tensor5
    tensor8=tensor6+tensor7
    '''Cette convention est naturelle. On l'utilise par exemple lorsqu'en math on écrit  Sum_i (a_i - b )^2   '''



    print("tensor1\n",tensor1 )
    print("tensor2\n",tensor2 )
    print("tensor1Exp\n",tensor1Exp )
    print("tensor2Exp\n",tensor2Exp )
    print("shape(tensor1)\n",np.shape(tensor1) )
    print("shape(tensor1Exp)\n",np.shape(tensor1Exp) )
    print("tensor3\n",tensor3 )
    print("tensor7\n",tensor7)
    print("tensor8\n",tensor8)

    return




"""extractions de sous-tenseurs et concaténation"""
def step7():

    """"""
    """ concaténations de tenseurs """
    tensor0=np.array([[1,2,3],[4,5,6]])
    tensor1 =np.array([[7,8,9],[10,11,12]])
    tensor2 =np.concatenate([tensor0,tensor1],axis=0)
    tensor3 =np.concatenate([tensor0,tensor1],axis=1)
    """quel est le role du premier paramètre dans concat ? """

    """ extractions de sous matrices : on précise les indices que l'on veut extraire.
    Quand on ne met rien : on va jusqu'à l'indice max """
    gros=np.array([[0,1,2,3,4],[10,11,12,13,14],[20,21,22,23,24]])
    tensor4 =gros[0,[0,2]]#on prend l'intersection entre la  lignes 0 et les colonnes 0 et 2
    tensor5 =gros[0,0:2]#on prend l'intersection entre la  lignes 0 et les colonnes 0,1,2
    tensor6 =gros[1:,2:] #on prend l'intersection entre la  lignes 0... et les colonnes 2...
    tensor7 =gros[[0,2],:] #on prend entièrement les lignes 0 et 2


    """concaténons une liste de tenseurs"""
    list=[]
    for i in range(3):
        list.append(np.ones([2,3])*i)

    tensor8 =np.concatenate(list,axis=0)
    tensor9 =np.concatenate(list,axis=1)


    print("tensor0\n",tensor0)
    print("tensor1\n", tensor1)
    print("tensor2\n", tensor2)
    print("tensor3\n", tensor3)
    print("tensor4\n", tensor4)
    print("tensor5\n", tensor5)
    print("tensor6\n", tensor6)
    print("tensor7\n", tensor7)
    print("tensor8\n", tensor8)
    print("tensor9\n", tensor9)

    return





"""reshape"""
def step8():

    a=np.array([1,2,3,4,5,6])
    b=a.reshape([2,3])
    c=a.reshape([3,2,1])

    print('a\n',a)
    print('b\n',b)
    print('c\n',c)

    """ attention, reshape crée de nouvelle "view" (=présentation) des données.
    Les données sont partagées entre ces différentes view  """
    a[:]=0
    print('a\n', a)
    print('b\n', b)
    print('c\n', c)


"""
question :  numpy identifie-t-il
 * les vecteurs lignes et  matrices composés d'une ligne ?
 * les vecteurs lignes et les vecteurs colonnes ?
 connaissez vous des langages qui font l'une ou l'autre de ces identifications ?
 """

