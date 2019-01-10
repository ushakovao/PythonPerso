
import numpy as np
import matplotlib.pyplot as plt
import time


""" Nous traçons l'ensemble de Julia.
 Vous n'étes pas obligé de comprendre ce programme en détail : observez uniquement les opérations sur les nombres complexes.

  BONUS : modifier ce programme pour tracer l'ensemble de Mandelbrot.
  BONUS :  allez  regarder le step d'après qui est une optimisation faite par Gwenael"""



def step0():
    """"""
    """ Le domaine sera :[-xlim,xlim] × i[-xlim,xlim] """
    xlim = 1.5
    """ nombre de pixel par ligne"""
    nx = 500
    """ nombre d'itération"""
    niter = 50

    x = np.linspace(-xlim, xlim, nx)
    y = np.linspace(-xlim, xlim, nx)
    """ 2 tableaux 2D de réel"""
    xx, yy = np.meshgrid(x, x)
    """  1 tableau 2D de complexes"""
    z = xx + 1j * yy
    c = complex(-0.9, 0)
    """ une matrice où il y a que des c """
    cc=np.empty((nx,nx),dtype=np.complex)
    cc[:]=c



    """pour stocker les vitesses de divergence"""
    divergence_speed = np.empty((nx,nx), dtype=np.int_)
    mandel = np.empty((nx, nx), dtype=np.int_)
    """on affecte une valeur par défaut"""
    divergence_speed[:] = niter

    startingTime=time.time()

    for i in range(niter):
        z = z ** 2 + cc

        indexDiv = (np.abs(z)>2)

        divergence_speed[indexDiv]=i

        z[indexDiv] = 0
        cc[indexDiv] = 0

    print("duration for %d points and %d iterations:"%(nx*nx,niter),time.time()-startingTime)
    plt.imshow(divergence_speed, extent=[-xlim, xlim, -xlim, xlim])
    plt.title(c)
    plt.show()


def mandel():

    xlim = 2
    nx = 500
    niter = 200

    x = np.linspace(-xlim, xlim, nx)
    xx, yy = np.meshgrid(x, x)

    c = xx + 1j * yy
    z = 0

    for g in range(niter):
        z = z ** 2 + c

    seuil = 2
    toplot = np.abs(z) < seuil

    plt.imshow(toplot, extent=[-2, 1, -1.5, 1.5])
    plt.show()

mandel()




""" BONUS : Le même programme par Gwenael.  Remarquez plusieurs optimisation intéressantes (cf commentaires).
 Ces optimisations ne se font ressentir qu'à partir d'un grand nombre de point. Ex : avec 2000*2000 points le programme
 de Gwenael est 2 fois plus rapide
 BONUS DU BONUS : trouvez ce qui fait gagner le plus de temps : l'utilisation du in-place, ou bien du masque de calcul (le where=)
 """


def step1() :
    ax,bx = -1.5,1.5
    ay,by = -1.5,1.5
    N,M = 500,500
    shape =(N,M)

    niter = 500
    XT = np.linspace(ax,bx,N)
    YT = np.linspace(ay,by,M)
    XV,YV = np.meshgrid(XT,YT)
    z = XV + YV * 1j
    C = complex(0.284, 0.0122)

    divergence_speed = np.empty(shape,dtype=np.int_)
    divergence_speed[:]=niter

    abs_z = np.empty(shape,dtype = np.complex)
    activeIndices = np.empty(shape,dtype = np.bool)
    startingTime = time.time()


    for i in range(niter) :
        """les indices actifs sont ceux où l'on la vitesse de divergence est encore égale à la valeur par défaut """
        np.equal(divergence_speed,niter,out=activeIndices)

        """on effectue les opérations z = z^2 + C puis abs_z=|z| uniquement sur les indices actifs.
          De plus, en précisant un argument de sortie équal à l'argument d'entrée, on fait du in-place """
        np.multiply(z,z,out=z,where = activeIndices) # Au tour de la bibliothèque numpy d'être mal foutue
        np.add(z,C,out=z,where = activeIndices)
        np.abs(z,out=abs_z,where = activeIndices)
        """on mémorise l'indice de divergence"""
        divergence_speed[activeIndices & (abs_z>2)] =  i

    print("duration for %d points and %d iterations:"%(N*M,niter),time.time()-startingTime)

    plt.imshow(np.sqrt(divergence_speed), extent=[ax, bx, ay, by])
    plt.title(C)
    plt.show()





