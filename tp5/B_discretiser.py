
import numpy as np
np.set_printoptions(precision=5,linewidth=5000)
import matplotlib.pyplot as plt
import math

"""on définit la base sin-cos
Avec la méthode=0, on discrétise sans faire trop attention
Avec la méthode=1, on discrétise de manière à ce que les vecteurs obtenus soient exactement orthogonaux.
On observe la matrice des produits scalaires.
BONUS : quels seraient les points de discrétisation, qui permettraient à la base des polynomes Legendre
"""

def step0(methode):

    freqMax=3

    if methode==0:
        """un nbStep= 21 pour avoir un epsilon=0.1.  Mais quelque soit le nbStep, on a le même problème. """
        nbStep = 21
        ''' intervalle de travaille'''
        gauche = 0.
        droite = 2.
        T = droite - gauche
        ''' pas d'échantillonnage'''
        epsilon = T / nbStep
        '''la grille d'abscisses (np.array set uniquement à éviter les warning, les déclarations de type en numpy étant mal foutue)'''
        x = np.array(np.linspace(gauche, droite, nbStep))

    else:
        T = 2.
        """un pas de discrétisation qui divise exactement l'intervale [0,T]"""
        epsilon = 0.1
        """essayer avec un pas qui ne divise pas : """
        # epsilon=0.09
        """on utilise arange, une variante de linspace. Notez les différences."""
        x = np.arange(0, T, epsilon)

    """observons l'intervalle discrétisé"""
    print("epsilon",epsilon)
    print(x)

    basisAsList = []
    for i in range(1, freqMax + 1):
        basisAsList.append(np.sin(i * 2 * math.pi / T * x))
        basisAsList.append(np.cos(i * 2 * math.pi / T * x))

    """concaténation. Chaque ligne représente une fonction de la base"""
    basis = np.array(basisAsList)

    matrixProd = np.sum(np.expand_dims(basis, 1) * np.expand_dims(basis, 0), 2)
    allScalarProducts = np.round(T / 2 * epsilon * matrixProd, decimals=2)

    print(allScalarProducts)




"""on oublie l'intervalle temporel. On définit directement une base discrète. Et l'on travaille avec la base des exponentielles."""
def step2():
    """"""
    """taille de la base"""
    N=10
    base=[]
    x=np.arange(0,N,1)
    for k in range(4):
        e_n=np.exp(x*2*1j*np.pi*k/N)
        base.append(e_n)
    base=np.array(base)

    prodSca = np.matmul(base, np.conj(base.transpose()))/N
    print(np.round(np.abs( prodSca),5))

step2()




""" on calcul la TF discrete directement puis avec l'algo de la FFT (Fast Fourier Transform).
 Comparez les temps de calcul (faites varier N).
 Affichez les bonnes échelles en abscisses : supposez que le signal dure 2 secondes.
 reliez le premier pic de fréquence avec le nombre d'oscillation du signal.
 Reconstituez le signal avec sa TF à l'aide de la "formule d'inversion"
 """
def step3():
    N=1000
    x=np.arange(0,N,1)
    noise=np.multiply(np.sin(x/N*500),0.1)
    signal=np.log(np.clip(np.sin(x/N*50),0.001,1))+noise

    base=[]
    x=np.arange(0,N,1)
    for k in range(N):
        e_n=np.exp(x*2*1j*np.pi*k/N)
        base.append(e_n)
    base=np.array(base)

    """ F_signal[k] = sca(signal, base_k)=1/N  sum_j  signal[j] base[k,j] """
    F_signal=1/N*np.matmul(base,signal)
    FFT_signal=1/N*np.fft.fft(signal)

    plt.subplot(3,1,1)
    plt.plot(signal)
    plt.subplot(3,1,2)
    plt.plot(np.abs(F_signal))
    plt.subplot(3,1,3)
    plt.plot(np.abs(FFT_signal))
    plt.show()


""" on transforme le signal par la fft, puis avec la fft-inverse on retrouve le signal."""
def step4():
    N=500
    x=np.arange(0,N,1)
    noise=np.multiply(np.sin(x/N*500),0.1)
    signal=np.log(np.clip(np.sin(x/N*50),0.001,1))+noise

    FFT_signal=1/N*np.fft.fft(signal) #type: np.ndarray

    new_s=FFT_signal.copy()
    seuil1=0.7*((abs(new_s)).max()) #delete high freqs
    seuil2 = 1.2 * ((abs(new_s)).min())  #delete low freqs
    new_s[abs(new_s) > seuil1] = 0
    new_s[abs(new_s) < seuil2] = 0

    plt.subplot(4,1,1)
    plt.plot(signal)

    plt.subplot(4,1,2)
    plt.plot(np.abs(FFT_signal))

    plt.subplot(4,1,3)
    plt.plot(np.abs(new_s))

    plt.subplot(4,1,4)
    plt.plot(np.fft.ifft(new_s))

    plt.show()

""" A vous de jouer : essayer de supprimer le bruit dans ce signal en jouant avec la fft : supprimer des hautes fréquences
dans la fft avant de faire fft-inverse.
ATTENTION : dans la fft, les hautes fréquences sont située au milieu du vecteur. Il faut supprimer les hautes fréquences
de manière symétrique, pour pouvoir retomber sur un vecteur réel.
  """

step4()

""" On utilise maintenant la rfft : qui prend en compte le fait que le signal de départ est réel.
 Quelle petite optimisation fait numpy dans ce cas là ?
 Refaites le filtrage du bruit. C'est plus simple maintenant. """
def step5():
    N=1000
    x=np.arange(0,N,1)
    noise=np.multiply(np.sin(x/N*500),0.1)
    signal=np.log(np.clip(np.sin(x/N*50),0.001,1))+noise


    FFT_signal=1/N*np.fft.rfft(signal) #type: np.ndarray

    new_s=FFT_signal.copy()
    seuil1=0.7*((abs(new_s)).max())
    new_s[abs(new_s)>seuil1]=0

    plt.subplot(4,1,1)
    plt.plot(signal)

    plt.subplot(4,1,2)
    plt.plot(np.abs(FFT_signal))

    plt.subplot(4,1,3)
    plt.plot(np.abs(new_s))

    plt.subplot(4,1,4)
    plt.plot(np.fft.irfft(new_s))

    plt.show()
step5()