import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

"""
suivez le lien suivant
http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html#quick-references

Vos arrivez à la fin d'un tuto très bien fait. Observez les différentes figures. Cela vous permettra de voir les opérations
de broadcasting et de reshaping graphiquement.

Voici une fonction qui permet de tracer les matrices. N'hésitez pas à l'utilisez là dans votre rapport : un beau graphique
vos toujours mieux qu'un tableau de chiffre.

"""

def showMatrix(Z, filename=None):
    """trace une matrice en niveau de violet"""
    """si on rentre un vecteur, cela le transforme en matrice"""
    Z = np.atleast_2d(Z)

    plt.figure(figsize=(Z.shape[1]/2.,Z.shape[0]/2.), dpi=72)
    plt.imshow(Z, cmap='Purples', extent=[0,Z.shape[1],0,Z.shape[0]],vmin=0, vmax=max(1,Z.max()), interpolation='nearest', origin='upper')
    plt.xticks([]), plt.yticks([])
    plt.xlim(0,Z.shape[1])
    plt.ylim(0,Z.shape[0])

    if filename is not None:plt.savefig(filename,dpi=72)
    plt.show()



def step0():
    Z1= np.linspace(0,1,10)
    Z2= np.linspace(0,1,5)
    """Z3[i,j]=Z1[j]*Z2[i]"""
    Z3= Z1* np.expand_dims(Z2,1)
    showMatrix(Z3)


def step1():
    sample_size = 10
    x0 = np.random.random([sample_size])
    x1 = 3 * np.random.random([sample_size])
    epsilon = 0.1
    x2 = x0 + x1 + epsilon * np.random.random([sample_size])
    x = np.transpose(np.array([x0, x1, x2]))

    """Afficher la matrice"""
    print(x)
    """Calculons les moyennes pour colonnes"""
    means1 = [np.mean(x0), np.mean(x1), np.mean (x2)]
    means2 = [np.sum(x0)/sample_size, np.sum(x1)/sample_size, np.sum(x2)/sample_size]
    print(means1)
    print(means2)
    """Calculons les écart types"""
    et=[np.std(x0), np.std(x1),np.std(x2) ]
    print(et)
    """Correlations"""
    c1 = np.corrcoef(x0, x1)
    c2 = np.corrcoef(x0, x2)
    c3 = np.corrcoef(x1, x2)
    print(c1)
    print(c2)
    print(c3)
    """Covatiations"""
    cv1 = np.cov(x0, x1)
    cv2 = np.cov(x0, x2)
    cv3 = np.cov(x1, x2)
    print(cv1)
    print(cv2)
    print(cv3)







def step2():


    sample_size = 10
    x0 = np.random.random([sample_size])
    x1 = 3 * np.random.random([sample_size])
    epsilon = 0.1
    x2 = x0 + x1 + epsilon * np.random.random([sample_size])
    x = np.transpose(np.array([x0, x1, x2]))

    """Afficher la matrice"""

    print("Dataframe \n", x)
    """Calculons les moyennes pour colonnes"""
    means1 = [np.mean(x0), np.mean(x1), np.mean (x2)]
    means2 = [np.sum(x0)/sample_size, np.sum(x1)/sample_size, np.sum(x2)/sample_size]
    print("Moyennes par np.mean",means1)
    print("Moyennes par np.sum",means2)
    """Calculons les écart types"""
    et=[np.std(x0), np.std(x1),np.std(x2) ]
    print("Ecart-types",et)
    """Centrées requites"""
    cr0 = [(x0- (np.sum(x0)/sample_size))/np.std(x0)]
    print("Centrées réduites pour colonne 0 \n",cr0)
    """Correlations"""
    c1 = np.corrcoef(x0, x1)
    c2 = np.corrcoef(x0, x2)
    c3 = np.corrcoef(x1, x2)
    print("Correlation par np.corrcoef 0/1 \n",c1)
    print("Correlation par np.corrcoef 0/2 \n",c2)
    print("Correlation par np.corrcoef 1/2\n",c3)

    """Covatiations"""
    cv01 = np.cov(x0, x1)
    cv02 = np.cov(x0, x2)
    cv12 = np.cov(x1, x2)

    cv00 = np.cov(x0, x0)
    cv11 = np.cov(x1, x1)
    cv22 = np.cov(x2, x2)

    """Notre Correlations"""
    cc01 = cv01 / (np.sqrt(cv00 * cv11))
    cc02 = cv02 / (np.sqrt(cv00 * cv22))
    cc12 = cv12 / (np.sqrt(cv11 * cv22))

    print ("Correlation par covariances 0/1 \n", cc01)
    print ("Correlation par covariances 0/2 \n", cc02)
    print ("Correlation par covariances 1/2 \n", cc12)


    ce01 = np.cov(x0,x1)/(np.std(x0)*np.std(x1))
    ce02 = np.cov(x0,x2)/(np.std(x0)*np.std(x2))
    ce12 = np.cov(x1,x2)/(np.std(x1)*np.std(x2))

    print ("Correlation par covariances et sigma 0/1 \n", cc01)
    print ("Correlation par covariances et sigma 0/2 \n", cc02)
    print ("Correlation par covariances et sigma 1/2 \n", cc12)




if __name__=='__main__': step2()











#
# Z1 = np.random.uniform(0,1,(9,5))
# Z2 = np.ones((1,1))
# Z3 = np.ones(Z1.shape)
# show(Z1, Z1.shape, "../figures/broadcast-1.1.png")
# show(Z2, Z1.shape, "../figures/broadcast-1.2.png")
# show(Z3, Z1.shape, "../figures/broadcast-1.3.png")
# show(Z1+Z2, Z1.shape, "../figures/broadcast-1.4.png")
#
# Z2 = np.arange(9).reshape(9,1)
# Z3 = np.repeat(Z2,5).reshape(9,5)
# show(Z1, Z1.shape, "../figures/broadcast-2.1.png")
# show(Z2, Z1.shape, "../figures/broadcast-2.2.png")
# show(Z3, Z1.shape, "../figures/broadcast-2.3.png")
# show(Z1+Z2, Z1.shape, "../figures/broadcast-2.4.png")
#
# Z2 = np.arange(5).reshape(1,5)
# #Z3 = np.zeros(Z1.shape)
# Z3 = np.repeat(Z2,9).reshape(5,9).T
# show(Z1, Z1.shape, "../figures/broadcast-3.1.png")
# show(Z2, Z1.shape, "../figures/broadcast-3.2.png")
# show(Z3, Z1.shape, "../figures/broadcast-3.3.png")
# show(Z1+Z2, Z1.shape, "../figures/broadcast-3.4.png")
#
# Z = np.zeros((9,5))
# Z1 = np.arange(9).reshape(9,1)
# Z2 = np.arange(5).reshape(1,5)
# Z3 = np.repeat(Z1,5).reshape(9,5)
# Z4 = np.repeat(Z2,9).reshape(5,9).T
# show(Z1, Z.shape, "../figures/broadcast-4.1.png")
# show(Z2, Z.shape, "../figures/broadcast-4.2.png")
# show(Z3, Z.shape, "../figures/broadcast-4.3.png")
# show(Z4, Z.shape, "../figures/broadcast-4.4.png")
# show(Z1+Z2, Z.shape, "../figures/broadcast-4.5.png")


# def broadcast(Z1,Z2,Z3,Z4,Z5,filename):

#     filename ''.join(filename.split('.')[:-1])

#     show_array(Z1, filename+'.1.png')
#     show_array(Z1, filename+'.1.png')
#     show_array(Z1, filename+'.1.png')
#     show_array(Z1, filename+'.1.png')


#     def print_array(Z,ox,oy,C):
#         for x in range(Z.shape[1]):
#             for y in range(Z.shape[0]):
#                 if x >= C.shape[1] or y >= C.shape[0]:
#                     color = '.75'
#                     zorder=  -1
#                 else:
#                     color = 'k'
#                     zorder=  +1
#                 plt.text(ox+x+0.5, rows-0.5-oy-y, '%d' % Z[y,x],
#                          ha='center', va= 'center', size=24, color=color)
#                 rect = Rectangle((ox+x,rows-1+oy-y),1,1, zorder=zorder,edgecolor=color, facecolor='None')
#                 ax.add_patch(rect)
    
#     rows = 4
#     cols = 5*3 + (5-1)
#     fig = plt.figure(figsize=(cols,rows), dpi=72, frameon=False)
#     ax = plt.axes([0.05,0.05,.9,.9], frameon=False)
#     plt.xlim(0,cols), plt.xticks([])
#     plt.ylim(0,rows), plt.yticks([])
#     ox,oy = 0.0125, 0.0125
#     print_array(Z1,ox+0,oy,Z1)
#     plt.text(3.5, 2, '+', ha='center', va= 'center', size=48)
#     print_array(Z2,ox+4,oy,Z2)
#     plt.text(7.5, 2, '=', ha='center', va= 'center', size=48)
#     print_array(Z3,ox+8,oy,Z1)
#     plt.text(11.5, 2, '+', ha='center', va= 'center', size=48)
#     print_array(Z4,ox+12,oy,Z2)
#     plt.text(15.5, 2, '=', ha='center', va= 'center', size=48)
#     print_array(Z5,ox+16,oy,Z5)
# #    plt.savefig('../figures/%s' % name, dpi=32)
# #    plt.show()




# Z  = np.zeros((4,3))
# Z1 = np.repeat(np.arange(4)*10,3).reshape(4,3)
# Z2 = np.zeros((1,1))
# Z3 = Z1+Z2
# broadcast(Z1,Z2,Z+Z1,Z+Z2,Z1+Z2, "../figures/broadcast-1.png")


# Z  = np.zeros((4,3))
# Z1 = np.repeat(np.arange(4)*10,3).reshape(4,3)
# Z2 = np.resize(np.arange(3),(4,3))
# Z3 = Z1+Z2
# broadcast(Z1,Z2,Z+Z1,Z+Z2,Z1+Z2, "../figures/broadcast-2.png")


# Z  = np.zeros((4,3))
# Z1 = np.repeat(np.arange(4)*10,3).reshape(4,3)
# Z2 = np.arange(3).reshape(1,3)
# Z3 = Z1+Z2
# broadcast(Z1,Z2,Z+Z1,Z+Z2,Z1+Z2, "../figures/broadcast-3.png")


# Z  = np.zeros((4,3))
# Z1 = np.arange(4).reshape(4,1)*10
# Z2 = np.arange(3).reshape(1,3)
# Z3 = Z1+Z2
# broadcast(Z1,Z2,Z+Z1,Z+Z2,Z1+Z2, "../figures/broadcast-4.png")



"""
def show_array(Z1, Z2, name, a):
    Z1 = np.atleast_2d(Z1)
    rows,cols = Z2.shape
    fig = figure(figsize=(cols,rows), dpi=72, frameon=False)
    ax = axes([0,0,1,1], frameon=False)
    if a:
        imshow(Z2, cmap='Purples', extent=[0,Z2.shape[1],0,Z2.shape[0]], alpha=.5,
               vmin=-0.1, vmax=1, interpolation='nearest', origin='lower')
        hold(True)
    imshow(Z1, cmap='Purples', extent=[0,Z1.shape[1],0,Z1.shape[0]],
           vmin=-0.1, vmax=1, interpolation='nearest', origin='lower')
    xlim(0,Z2.shape[1]), xticks([])
    ylim(0,Z2.shape[0]), yticks([])
    savefig('../figures/%s' % name, dpi=16)
    #show()


rows,cols = 5, 9

Z1 = np.array([1.0])
Z2 = np.resize(Z1,(5,9))
show_array(Z1,Z2, 'broadcasts-1-before.png', False)
show_array(Z1,Z2, 'broadcasts-1-after.png', True)

Z1 = np.linspace(0,1,cols).reshape(1,cols)
Z2 = np.repeat(Z1,rows,axis=0)
show_array(Z1,Z2, 'broadcasts-2-before.png', False)
show_array(Z1,Z2, 'broadcasts-2-after.png', True)

Z1 = np.linspace(0,1,rows).reshape(rows,1)
Z2 = np.repeat(Z1,cols,axis=1)
show_array(Z1,Z2, 'broadcasts-3-before.png', False)
show_array(Z1,Z2, 'broadcasts-3-after.png', True)
"""
