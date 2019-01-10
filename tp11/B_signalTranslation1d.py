import  matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

from tp11.A_convolution1d import anti_convolution_rapide1d

np.set_printoptions(linewidth=5000,precision=2)

#plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

"""
On recale des signaux 1d
"""


def twoSignals(N):

    x=np.arange(0,N)
    taille=int(N/20)
    bosse=np.concatenate([np.arange(0,taille)/taille,-np.arange(0,taille)/taille+1])

    signal1=np.zeros(N)
    signal2=np.zeros(N)

    signal1[int(N*0.4):int(N*0.4)+2*taille]=bosse
    signal2[int(N*0.3):int(N*0.3)+2*taille]=np.sqrt(bosse)


    return signal1,signal2



def step0():
    N = 100
    signal1,signal2=twoSignals(N)
    plt.plot(signal1,label="signal1")
    plt.plot(signal2,label="signal2")
    plt.legend()
    plt.show()

def step00():

    N = 100
    taille=int(N/20)
    t=np.linspace(0,taille,N)
    bosse=np.concatenate([np.arange(0,taille)/taille,-np.arange(0,taille)/taille+1])
    phi = 15;
    signal1=(np.sin(2*np.pi*440*t))+(0.5*np.sin(2*np.pi*t*800))
    signal2=(np.sin(2*np.pi*440*(t-phi)))+(0.5*np.sin(2*np.pi*(t-phi)*800))
    plt.plot(signal1,label="signal1")
    plt.plot(signal2,label="signal2")
    plt.legend()
    plt.show()

def step1():
    N=100
    signal1,signal2=twoSignals(N)
    t = np.linspace(0, 50, 100)
    dec = 0.005
    #signal1 = (np.sin(2 * np.pi * 440 * t)) + (0.5 * np.sin(2 * np.pi * t * 800))
    #signal2 = (np.sin(2 * np.pi * 440 * (t - dec))) + (0.5 * np.sin(2 * np.pi * (t - dec) * 800))

    correlation=anti_convolution_rapide1d(signal1,signal2)

    enlarged1=np.zeros(2*N)
    enlarged1[:N]=signal1
    enlarged2=np.zeros(2*N)

    decay_to_distance = np.empty(N)
    for i in range(N):
        enlarged2[i:i+N]=signal2
        decay_to_distance[i]=np.sum(np.square(enlarged1-enlarged2))

    best_decay=np.argmin(decay_to_distance)
    print("best decay for signal1:",best_decay)
    plt.plot(signal1,label="signal1")
    plt.plot(signal2,label="signal2")
    plt.legend()
    plt.show()

def step2():
    N = 100
    signal1, signal2 = twoSignals(N)
    correlation=anti_convolution_rapide1d(signal1,signal2)

    best_decay = np.argmax(correlation)
    print("best decay of signal1:", best_decay)

    correlation = anti_convolution_rapide1d(signal2, signal1)
    best_decay = np.argmax(correlation)



    print("best decay of signal2:", best_decay)
    """comment interpréter ce second résultat ?"""




"""là où les problèmes arrivent à cause des supports des signaux : """
def step3():
    N = 100
    signal1, signal2 = twoSignals(N)
    signal1+=16
    signal2+=4



    correlation=anti_convolution_rapide1d(signal1,signal2)
    best_decay = np.argmax(correlation)
    print("best decay of signal1:", best_decay)

    correlation = anti_convolution_rapide1d(signal2, signal1)
    best_decay = np.argmax(correlation)
    print("best decay of signal2:", best_decay)

    """pourquoi est-ce que le meilleurs ici décalage est zéro dans ce cas là ?
    Imaginons que l'on ai vraiment envie de caller les bosses entre-elles (c'est naturel)
    Quel pré-traitement des données doit-on faire ?
    (si vous n'avez pas d'idée, la réponse se trouve cachée dans le blabla à la fin du fichier)
    """



if __name__=='__main__':
    step1()


"""


Travail :
Construisez les signaux
t -> sin (2 pi t*440) + 0.5 sin (2 pi t*800)
et
t -> sin (2 pi (t-phi)*440) + 0.5 sin (2 pi (t-phi)*800)
où phi est un paramètre de déphasage. Retrouver le déphasage à l'aide d'une anti-convolution (utilisez la plus adaptée).

BONUS : repérez ce déphasage avec le module de la fft ?


Inventez un signal pour lesquels il ne faudrait surtout pas utiliser l'anti-convolution circulaire pour
retrouver un décallage (cherchez à exagérer les problèmes de repliement sur les bords).




VOCABULAIRE :
'anti-convolution' est un terme inventé pour ce TP. Le terme officiel est 'cross-correlation'.

 Dans la définition wikipédia, la cross-correlation inclus l'opération de "centrer-réduire".
https://en.wikipedia.org/wiki/Digital_image_correlation

Par contre, dans numpy-scipy les fonction correlate ne font apparemment pas l'opération de "centrer-réduire".

Pour les signaux complexe, il faut aussi prendre le conjugué du second terme (mais nous ne travaillons qu'avec des signaux réels).
Ainsi dans l'aide de numpy.correlate la formule indiquée est :
                            c'_{av} [k] = sum_n a[n] conj(v[n+k])
Notez la différence de signe : Notre anti-correlation effectue :
                                          sum_n a[n]      v[n-k]
Personnellement je trouve cela plus malin puisque cela donne directement le décallage à effectuer.






Travail mathématique :

Nous travaillons modulo N. Considérons les deux formules suivantes :


Dx = sum_i  (signal1[i] - signal2[i+x] )^2

Cx = sum_i  signal1[i] signal2[i+x]

avec
   sum_i  allant de i=0 à i=N-1
   i+x   étant à prendre modulo N

Montrez que minimisez la distance x-> Dx  est équivalent à maximiser  x-> Cx.


Travaillons maintenant sans les modulo. Les signaux sont porté par [0,N-1], mais prolongé par 0 en dehors. Ainsi
les expressions Dx et Cx peuvent être définies mais elles n'ont plus le même sens que précédemment.

Expliquez pourquoi la maximisation de x->Cx ne fonctionne plus pour trouver le meilleur décallage.
Expliquez avec ces formules, et avec vos mots, pourquoi le fait de centrer-réduire préalablement les signaux, permet de
 rentre similaire la minimisation de x-> Dx et de x-> Cx


"""


















