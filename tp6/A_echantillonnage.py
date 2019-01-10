
import numpy as np
np.set_printoptions(precision=5,linewidth=5000)
import matplotlib.pyplot as plt
import soundfile as sf



"""on construit un signal et on le sous-échantillonne en le décimant"""
def step0():

    """"""
    """un signal de 2 secondes échantillonné très finement : il est lisse, on l'assimile à un 'vrai' signal physique en temps continu"""
    epsilon=0.0001
    t=np.arange(0,2,epsilon)
    signal=0.5*np.sin(t*2*np.pi*880)+np.sin(t*2*np.pi*220) #type: np.ndarray
    FFT_signal=1/len(t)*np.fft.rfft(signal) #type: np.ndarray

    """ l'indice qui permet de tracer les 0.05 secondes du signal """
    n=len(t[t<0.05])
    plt.subplot(4,1,1)
    plt.plot(t[:n],signal[:n])
    plt.subplot(4,1,2)
    """on met la bonne échelle des fréquences en abscisse"""
    plt.plot(np.linspace(0,1/epsilon/2,len(FFT_signal)),np.abs(FFT_signal))

    """on décime le signal = on le sous-échantillonne en prenant un élément sur 10"""
    t_dec=t[::10]
    signal_dec=signal[::10]
    FFT_signal_dec=1/len(t_dec)*np.fft.rfft(signal_dec) #type: np.ndarray


    """ l'indice qui permet de tracer les 0.05 secondes du signal décimé"""
    n = len(t_dec[t_dec < 0.02])
    plt.subplot(4, 1, 3)
    plt.plot(t[:10*n],signal[:10*n])
    plt.plot(t_dec[:n], signal_dec[:n])
    plt.subplot(4, 1, 4)
    plt.plot(np.linspace(0, 1 / epsilon/10 / 2, len(FFT_signal_dec)), np.abs(FFT_signal_dec))

    np.savetxt("signal_dec.csv",signal_dec)
    sf.write('signal.wav', signal, int(1 / epsilon))
    sf.write('signal_dec.wav', signal_dec, int(1 / epsilon/10))
    print("les taux d'echantillonnage sont",int(1 / epsilon),int(1 / epsilon/10))

    plt.show()



"""on récupère le signal décimé. """
def step1():
    """"""
    signal_dec=np.loadtxt("signal_dec.csv")
    taille_dec=signal_dec.shape[0]
    taille=10*taille_dec

    FFT_dec=np.zeros(taille//2+1,dtype=np.complex)
    FFT_dec[:taille_dec//2+1]+=np.fft.rfft(signal_dec)
    plt.figure("transformee de la decompression")
    plt.plot(np.abs(FFT_dec))
    plt.figure("comparaison entre le signal compresse et decompression")
    plt.plot(np.fft.irfft(10*FFT_dec)[:100], label="signal decompresse")
    sf.write("signal_decomp.wav",np.fft.irfft(10*FFT_dec),taille)

    t=np.linspace(0,2,taille,endpoint=False)
    plt.plot(np.arange(0,100,10),np.fft.irfft(FFT_dec[:taille_dec//2+1])[:10], label="signal compresse")
    plt.legend()
    plt.show()


step0()
step1()
plt.show()



"""travail à effectuer :
imaginez que vous  disposez uniquement du signal décimé, comme dans le step 1.
Vous disposez aussi de la fréquence d'échantillonnge de ce signal :
1/epsilon/10 (10 fois moins que la fréquence d'échantillonnge initiale)

Commencez par tracez les 0.05 secondes de ce signal (recréez un vecteur t_dec).

Maintenant, vous devez reconstituer le signal lisse. Première étape :
 pralonger la TF avec des zéros. Remarquez que cette technique permet d'effectuer un sur-échantillonnage de la taille
  qu'on veut.


Limite de cette méthode : on ne peut utiliser cette  méthode que si la fréquence maximale du signale (ici 440)
est inférieure à la moitié de la fréquence d'échantillonnage (= la fréquence de Nyquist). Sinon l'enroullement du spectre
fera que le pic haute-fréquence se retrouvera en basse fréquence !

Rendez le signal initial plus aigu pour faire en sorte que la reconstitution se passe mal.
Ecoutez les sons produit. Commentez.

"""




