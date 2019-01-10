
from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

"""
Les signaux non-périodiques sont analysées à l'aide d'un spectrogram :
On découpe de signal en petite tranche (Suffisamment petite pour que sur chaque tranche le signal soit a peu prêt périodique).
Puis on calcul  la fft sur chaque tranche. Ci-dessous, le spectrogram est affiché en niveau de couleur. """
"""
epsilon = 0.0001
t = np.arange(0, 1, epsilon)

sig_debut = 0.5 * np.sin(t * 2 * np.pi * 440) + np.sin(t * 2 * np.pi * 220)
sig_fin = 0.5 * np.sin(t * 2 * np.pi * 880) + np.sin(t * 2 * np.pi * 440)
sig=np.concatenate((sig_debut, sig_fin))
"""

sig,samplerate = sf.read("knock.wav")
sig = sig[0:300000,0]

"""d'après l'aide officielle : https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html """
f, t, Sxx = signal.spectrogram(sig, samplerate/60)
plt.pcolormesh(t, f, ((Sxx)))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

"""travail : faite le spectrogram d'un extrait de musique. Essayer de lier le dessins à la musique.

BONUS : le logiciel shazam est fameux pour sa capacité à reconnaître de titre d'un morceau à partir d'un extrait de ce morceau.
Décrivez en quelques lignes, avec vos mots, comment fonctionne l'algorithme de shazam.
"""
