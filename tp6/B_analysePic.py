import numpy as np

from tp6.localMax import findLocalMax

np.set_printoptions(precision=5,linewidth=5000)
import matplotlib.pyplot as plt
import soundfile as sf



"""Les signaux périodiques naturels (pas seulement les sons) possèdes des pics de fréquences répartis à des intervalles
  réguliers. Expliquez pourquoi en quelque lignes, avec des mots à vous (ne recopiez pas un truc d'internet). Dans ce step,
   nous analysons un signal physique en observant ces pics de fréquences."""
def step1():
    sig,samplerate = sf.read('Sample.wav')
    signal1 = sig[:,0]
    fft = np.fft.rfft(signal1)
    fft1 = np.abs(fft)
    max_freq = 50000
    min_freq = 0
    #fft1=fft1[min_freq:max_freq]
    freqs = np.fft.rfftfreq(signal1.shape[-1],d = 1/samplerate)
    #freqs = freqs[min_freq:max_freq]

    """En traçant le signal, j'ai vu que 3001 est une bonne fenêtre de fréquence pour détecter les pics de fft.
        Si on met 4001, 2001, 1001, 10001 est-ce que cela irait aussi ?  Pourquoi des chiffres impairs...
        Bref, expliquez l'algo de détection des pics.
        """

    window_length = 3001

    import time
    t = time.time()
    loc_max_index = findLocalMax(fft1, window_length)
    print("Time :",time.time() - t,"s")

    plt.plot(freqs,fft1)
    plt.plot(freqs[loc_max_index],fft1[loc_max_index], 'o')
    plt.show()

    fft2 = np.zeros(fft.shape,dtype = complex)
    fft2[loc_max_index] = fft[loc_max_index]
    # plt.plot(np.abs(fft2))
    # plt.show()

    sig = np.fft.irfft(fft2)
    sf.write("sample_dec.wav",sig,samplerate)





"""
Travail : Analyser le signal droit. Observez les différences et les ressemblances entre droite et gauche.
Comparez les régularités des signaux et de leur fft.
Ces signaux ont-ils la même fréquence fondamentale ?
Ces signaux sont-ils liés au-dela de la fondamentale ?
Ces signaux peuvent-ils provenir des pistes droite et gauche d'un enregistrement audio ?

Pouvez-vous imaginer une technique de compression extrême du signal, où l'on ne garderait que les pic ?


BONUS : Pour calculer la fréquence fondamentale d'un signal, on peut simplement regarder le premier pic (autre que zéro).
 Mais souvent, ce premier pic est très faible, soir inexistant. Quel technique robuste peux-t-on utiliser.
"""

def step2() :
    sig, samplerate = sf.read('Sample.wav')
    sigg = sig[:,0]
    sigd = sig[:,1]
    freqs = np.fft.rfftfreq(sigg.shape[-1],d = 1/samplerate)

    fftg = np.fft.rfft(sigg)
    fftd = np.fft.rfft(sigd)

    fftg = np.abs(fftg)
    fftd = np.abs(fftd)

    max_freq = 50000
    min_freq = 0
    fftd=fftd[min_freq:max_freq]
    fftg=fftg[min_freq:max_freq]
    freqs=freqs[min_freq:max_freq]


    window_length = 3001

    loc_g = findLocalMax(fftg,window_length)
    loc_d = findLocalMax(fftd,window_length)
    print(loc_g)

    plt.subplot(2,1,1)
    plt.plot(freqs,fftg)
    plt.plot(freqs[loc_g],fftg[loc_g],'*')

    plt.subplot(2,1,2)
    plt.plot(freqs,fftd)
    plt.plot(freqs[loc_d],fftd[loc_d],'*')

    plt.show()



step2()
