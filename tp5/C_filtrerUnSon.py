import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
"""
Comment lire et écrire des fichiers son ?
Sur google -> "python read write sound file"
Sur stackoverflow -> je regarde les débats sur ce sujet. Plusieurs librairies sont disponibles. La meilleure semple être PySoundFile

J'installe PySoundFile. Chez moi cela a marché du premier coup via l'IDE : preference-> projet interpreter -> +  ...
Sinon tentez le classique sudo apt-get install ...
Sinon -> google

J'ai utilisé le tuto suivant sur PySoundFile (dans le même github, il compare avec les autres lib disponibles).
https://github.com/mgeier/python-audio/blob/2be5c5f2fcfa0adfcddab83d7a1b974208f6140a/audio-files/audio-files-with-pysoundfile.ipynb """

"""
J'ai des trouvé des sons courts ici :
http://www.pa.msu.edu/~nila/wav.html"""


""" lire un son existant"""
def step0():
    sig, samplerate = sf.read('/home/ushakova/PycharmProjects/Output.wav')

    """samplerate est la fréquence d'échantillonnage = le nombre de mesure du son effectuée par seconde.
    donc 1/samplerate c'est le pas de discrétisation """

    """  """
    print(sig.shape)
    print(samplerate)

    """ affichons le signal"""
    plt.plot(sig)
    plt.show()


""" créons un son : l'oreille la note 'la' à la fréquence 440 : c'est la référence pour l'accord des instruments de musique.
Cette note a une intensité qui oscille. Essayer de lire tout cela dans la formule mathématique du signal.
  """



def step1():
    samplerate=11025
    duration=3
    d2=1
    t=np.linspace(0,duration,duration*samplerate)
    t1 = np.linspace(0, 0.1, 0.1*samplerate)

    amplification=10 #essayer avec 10 puis 1000, que se passe-t-il ?
    """on crée un signal avec une fonction mathématique"""
    sig=amplification*np.sin(2*np.pi*440*t)*np.sin(2*np.pi*t)



    sf.write('la440.wav', sig, samplerate)

    """traçons l'intégralité du signal ; essayez de tracer le tout début seulement pour voir les oscillations rapides"""
    plt.plot(t,sig)
    plt.show()

def step1a():
    sig, samplerate = sf.read('/home/ushakova/PycharmProjects/Signals/tp5/la440.wav')
    N=1000;

    FFT_signal=1/N*np.fft.rfft(sig) #type: np.ndarray

    new_s=FFT_signal.copy()
    seuil1=0.7*((abs(new_s)).max())
    new_s[abs(new_s)>seuil1]=0

    plt.subplot(4,1,1)
    plt.plot(sig)

    plt.subplot(4,1,2)
    plt.plot(np.abs(FFT_signal))

    plt.subplot(4,1,3)
    plt.plot(np.abs(new_s))

    plt.subplot(4,1,4)
    plt.plot(np.fft.irfft(new_s))


    plt.show()


    sf.write('newla440.wav',new_s, samplerate)





def saw():
    samplerate=11025
    duration=3
    d2=1
    t=np.linspace(0,duration,duration*samplerate)
    t1 = np.linspace(0, 0.1, 0.1*samplerate)

    amplification=10 #essayer avec 10 puis 1000, que se passe-t-il ?
    """on crée un signal avec une fonction mathématique"""
    sig=amplification*np.cos(np.pi*500*t)*np.cos(0.50*np.pi*t)*np.cos(105*np.pi*t)



    sf.write('la440.wav', sig, samplerate)

    """traçons l'intégralité du signal ; essayez de tracer le tout début seulement pour voir les oscillations rapides"""
    plt.plot(t,sig)
    plt.show()


saw()



"""
BONUS : en collant des fonctions mathématique créer une petite mélodie. Vous trouverez facilement la correspondance
note<->fréquence sur le net. Si vous avez le temps expliquer rapidement la logique qui explique cette correspondance.

Attention : si vous voulez que les transitions entre note soit jolies, il faut effectuer des recollages "continus".
Utilisez pour cela des deux steps suivants.
"""



def step3(windowChoice):
    samplerate = 11025

    duration0=1.3
    duration1=2.6

    nb0=int(duration0*samplerate)
    nb1=int(duration1*samplerate)
    nb=nb0+nb1
    t=np.linspace(0,duration0+duration1,nb)
    signal0=np.sin(2*np.pi*t*2)
    signal1=np.sin(2*np.pi*t*5)


    window0 = np.zeros(nb)
    window1 = np.zeros(nb)

    if windowChoice==0:
        """transition abrupte"""
        window0[:nb0]=1
        window1[nb0:]=1
    else:
        """transition douce"""
        demiTransition = int(0.1 * samplerate)
        montee = np.linspace(0, 1, 2 * demiTransition)
        descente = 1 - montee
        window0[:nb0 - demiTransition] = 1
        window0[nb0 - demiTransition:nb0 + demiTransition] = descente
        window1[nb0 + demiTransition:] = 1
        window1[nb0 - demiTransition:nb0 + demiTransition] = montee


    plt.subplot(3,1,1)
    plt.plot(window0)
    plt.plot(window0*signal0)
    plt.ylim([-2,2])
    plt.subplot(3,1,2)
    plt.plot(window1)
    plt.plot(window1*signal1)
    plt.ylim([-2, 2])
    plt.subplot(3,1,3)
    plt.plot(window0+window1)
    plt.plot(window0*signal0+window1*signal1)
    plt.ylim([-2, 2])
    plt.show()






def step4():
    samplerate = 11025

    duration0=int(1*samplerate)
    duration1=int(1.5*samplerate)
    totalDuration=duration0+duration1

    demiTransition=int(0.1*samplerate)
    montee=np.linspace(0,1,2*demiTransition)
    descente=1-montee


    window0=np.zeros(totalDuration)
    window1=np.zeros(totalDuration)
    window0[:duration0-demiTransition]=1
    window0[duration0-demiTransition:duration0+demiTransition]=descente
    window1[duration0+demiTransition:]=1
    window1[duration0-demiTransition:duration0+demiTransition]=montee


    plt.subplot(3,1,1)
    plt.plot(window0)
    plt.ylim([0,2])
    plt.subplot(3,1,2)
    plt.plot(window1)
    plt.ylim([0, 2])
    plt.subplot(3,1,3)
    plt.plot(window0+window1)
    plt.ylim([0, 2])
    plt.show()



