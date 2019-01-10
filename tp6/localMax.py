import numpy as np


def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a,shape = shape,strides = strides)


def findLocalMax(data,windowLength):
    dataRoll = rolling_window(data,windowLength)
    # Goulot d'étranglement => argmax créé le tableau à partir de la vue avant de l'utiliser
    # Conclusion : Tableau de 40000 * 10001 qui peut être créé juste pour accéder aux éléments
    # armax = np.argmax(dataRoll,axis = 1)
    armax = np.apply_along_axis(np.argmax,1,dataRoll)

    where = np.where(armax == windowLength//2)
    return where[0] + windowLength//2


"""programme de test"""
if __name__=='__main__':
    data=np.ones(20)
    data[3]=2
    data[4]=2.1
    data[12]=1.01
    print(findLocalMax(data,5))
