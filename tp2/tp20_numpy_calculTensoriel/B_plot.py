
"""Attention : même si les 2 premiers import semblent inutiles, ils servent quelque part
(matplotlib est mal conçue)"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jn                # Import Bessel function.


np.set_printoptions(linewidth=2000)

def step1():

    #des vecteurs composés de 20 points régulièrement espacé de -5 à 5
    x = np.linspace(0, 1, 5)
    y = np.linspace(0, 1, 5)
    #on créer des matrices où se répètent x et y
    X, Y = np.meshgrid(x, y)
    #on fait un calcul terme à terme sur les matrices
    R = np.sqrt(X ** 2 + Y ** 2)
    #on applique une fonction sin à notre matrice R
    Z = np.sin(R)

    print('x\n',x)
    print('y\n',y)
    print('X\n',X)
    print('Y\n',Y)
    print('R\n',R)
    print('Z\n',Z)


def step2(colorPlot=False):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)
    X = np.linspace(-5, 5, 60)
    Y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.cos(np.sqrt(X ** 2 + Y ** 2))

    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()


def step3(colorPlot=False):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)


    X = np.linspace(-5, 5, 60)
    Y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(X, Y)
    Z=np.sin(X / 4) * np.cos(Y / 4)



    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()




def step4(colorPlot=False):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)


    X = np.linspace(-1, 1, 60)
    Y = np.linspace(-1, 1, 60)
    X, Y = np.meshgrid(X, Y)
    Z=X**2-Y**2



    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()



def step5(colorPlot=False):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)


    X = np.linspace(-15, 15, 60)
    Y = np.linspace(-15, 15, 60)
    X, Y = np.meshgrid(X, Y)


    R = np.sqrt(X ** 2 + Y ** 2)
    Z = jn(0, R)

    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()





def step6(colorPlot=True):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)


    X = np.linspace(-5, 5, 60)
    Y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(X, Y)

    #Z = np.sin(X+np.sin(np.pi))+np.cos(Y)
    Z = np.sin(X) + np.cos(Y)

    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()



def step7(colorPlot=False):
    #la figure
    fig = plt.figure()
    #
    #

    #on créer la fonction à représenter (cf step 1)
    X = np.linspace(-5, 5, 60)
    Y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(X, Y)
    Z =  np.tan(X **3 + Y ** 3)

    if not colorPlot:
        """la partie mathématique de la figure (la partie dans les axes)"""
        axis = fig.gca(projection='3d')
        #voici ce qu'on va tracer
        surf = axis.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='coolwarm',
                               linewidth=0, antialiased=False)
        """options de présentation"""
        #les limites en Z
        axis.set_zlim(-1.01, 1.01)
        #pour préciser que l'on veut 10 graduations en Z, et préciser le format des graduations
        axis.zaxis.set_major_locator(LinearLocator(10))
        axis.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        #la bare de couleur sur les côtés
        fig.colorbar(surf, shrink=0.5, aspect=5)
        #tout est prêt : on trace
        plt.show()
    else:

        """rajouter  interpolation='nearest' si l'on ne veut pas lisser l'image"""
        im = plt.imshow(Z,
                        aspect='auto',#pour que la fenetre s'adapte à l'image
                        extent=[-5, 5,-5,5],#pour choisir ses graduation (par défaut, c'est les indices de la matrice)
                        cmap='jet',#ma color-map préféré
                        norm=plt.Normalize(vmin=-1.01, vmax=1.01)#équivalent de axis.set_zlim
                        )
        plt.colorbar(im)
        plt.show()









step2()
step3()
step4()
step5()
step6()
