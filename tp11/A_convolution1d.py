
import numpy as np
from scipy import signal as sg
from scipy import ndimage
import  matplotlib
matplotlib.use('TkAgg')
import  matplotlib.pyplot as plt

np.set_printoptions(precision=1,linewidth=5000)


"""
Implémentation des (anti)-convolutions rapide via la fft.
On teste sur un exemple très simple. Comprenez bien cela avant de passer à la suite
"""




def convolution_rapide1d_circulaire(signal1: np.ndarray, signal2: np.ndarray) -> np.ndarray:
    max_len = max(len(signal1), len(signal2))

    enlarged1 = np.zeros(max_len)
    enlarged2 = np.zeros(max_len)
    enlarged1[:len(signal1)] = signal1
    enlarged2[:len(signal2)] = signal2
    return np.real(np.fft.ifft(np.fft.fft(enlarged1)*np.fft.fft(enlarged2)))


def convolution_rapide1d(signal1: np.ndarray, signal2: np.ndarray) -> np.ndarray:
    max_len = max(len(signal1), len(signal2))

    enlarged1 = np.zeros(2*max_len)
    enlarged2 = np.zeros(2*max_len)
    enlarged1[:len(signal1)] = signal1
    enlarged2[:len(signal2)] = signal2

    return np.real(np.fft.ifft(np.fft.fft(enlarged1)*np.fft.fft(enlarged2)))[:max_len]



""" renvoie
     x-> sum_i  signal1[i] signal2[i - x].
     x varie sur [0,2N-1] où N est la taille du plus long des deux signaux
     la soustraction i-x doit être comprise modulo 2N.
     """
def anti_convolution_rapide1d(signal1: np.ndarray, signal2: np.ndarray) -> np.ndarray:
    N = max(len(signal1), len(signal2))

    enlarged1 = np.zeros(2*N)

    enlarged2 = np.zeros(2*N)
    enlarged1[:len(signal1)] = signal1
    enlarged2[:len(signal2)] = signal2

    enlarged1=enlarged1[::-1]

    """attention :
       1/ il faut retourner après avoir élargit
       2/ en retournant le premier, c'est le second qui est décallé """

    return np.real(np.fft.ifft(np.fft.fft(enlarged1) * np.fft.fft(enlarged2)))[::-1]





def step0():
    a=np.array([1,2,3,4,10,100])
    b=np.array([2,-1])
    print(convolution_rapide1d_circulaire(a,b))
    print(convolution_rapide1d(a,b))
    """observez bien le tout dernier coefficient : celui d'incide 2N-2 (ici N=6).
    il a son importance : il correspond à un decalage négatif du petit vecteur sur le gros"""
    print(np.round(anti_convolution_rapide1d(a,b),1))


if __name__=='__main__':
    step0()







