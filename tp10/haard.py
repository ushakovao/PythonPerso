from math import sqrt
import PIL.Image as Image
from numpy import array, linspace
import matplotlib.pyplot as plt
from numpy import abs
threshold = 0.9


image = Image.open('test.png').convert('L')
image = array(image) / 255.0



CL = [(1 + sqrt(3)) / (4 * sqrt(2)),
    (3 + sqrt(3)) / (4 * sqrt(2)),
    (3 - sqrt(3)) / (4 * sqrt(2)),
    (1 - sqrt(3)) / (4 * sqrt(2))]


#Coefs pour la transfromation D4
def hpf_coeffs(CL):
    N = len(CL)
    CH = [(-1)**k * CL[N - k - 1]
        for k in xrange(N)]
    return CH
#Convolution des paires : comme resultat on obtient des sommes poinderees a coefs de CL et CH
#Somme poinderee - le produit ligne par colonne, ligne paire-filtre freq basse, ligne non-paire - filtre freq haute
def convo(data, CL, CH, delta = 0):
    assert(len(CL) == len(CH))
    N = len(CL)
    M = len(data)
    out = []
    for k in xrange(0, M, 2):
        sL = 0
        sH = 0
        for i in xrange(N):
            sL += data[(k + i - delta) % M] * CL[i]
            sH += data[(k + i - delta) % M] * CH[i]
        out.append(sL)
        out.append(sH)
    return out
#les coefs de la matrice inverse
def icoeffs(CL, CH):
    assert(len(CL) == len(CH))
    iCL = []
    iCH = []
    for k in xrange(0, len(CL), 2):
        iCL.extend([CL[k-2], CH[k-2]])
        iCH.extend([CL[k-1], CH[k-1]])
    return (iCL, iCH)

#Transformation Ondolette directe
def transform2D(image, CL):
    CH = hpf_coeffs(CL)
    w, h = image.shape
    imageT = image.copy()
    for i in xrange(h):
        imageT[i, :] = convo(imageT[i, :], CL, CH)
    for i in xrange(w):
        imageT[:, i] = convo(imageT[:, i], CL, CH)

    data = imageT.copy()
    data[0:h/2, 0:w/2] = imageT[0:h:2, 0:w:2]
    data[h/2:h, 0:w/2] = imageT[1:h:2, 0:w:2]
    data[0:h/2, w/2:w] = imageT[0:h:2, 1:w:2]
    data[h/2:h, w/2:w] = imageT[1:h:2, 1:w:2]
    return data

#Transformation Ondolette inverse
def itransform2D(data, CL):
    w, h = data.shape

    imageT = data.copy()
    imageT[0:h:2, 0:w:2] = data[0:h / 2, 0:w / 2]
    imageT[1:h:2, 0:w:2] = data[h / 2:h, 0:w / 2]
    imageT[0:h:2, 1:w:2] = data[0:h / 2, w / 2:w]
    imageT[1:h:2, 1:w:2] = data[h / 2:h, w / 2:w]

    CH = hpf_coeffs(CL)
    iCL, iCH = icoeffs(CL, CH)
    image = imageT.copy()
    for i in xrange(w):
        image[:, i] = convo(image[:, i], iCL, iCH, delta=len(iCL) - 2)
    for i in xrange(h):
        image[i, :] = convo(image[i, :], iCL, iCH, delta=len(iCL) - 2)

    return image
#D4
CL = [(1 + sqrt(3)) / (4 * sqrt(2)), (3 + sqrt(3)) / (4 * sqrt(2)), (3 - sqrt(3)) / (4 * sqrt(2)), (1 - sqrt(3)) / (4 * sqrt(2))]
C = [0, 1, 2, 3]
CH = hpf_coeffs(CL)
iCL, iCH = icoeffs(CL, CH)
Y = convo(C, CL, CH)
C2 = convo(Y, iCL, iCH, len(CL) - 2)


#Haar
C = [1/sqrt(2), 1/sqrt(2)]
data3 = transform2D(image, C)
plt.imshow(data3, cmap='gray')



data2 = transform2D(image, CL)
plt.imshow(data2, cmap='gray')





data = image.copy()
data2 = image.copy()

w, h = data.shape
while (w >= len(CL) and h >= len(CL)):
    data[0:w, 0:h] = transform2D(data[0:w, 0:h], CL)
    w /= 2
    h /= 2

data[abs(data)<threshold] = 0


while (w >= len(CL) and h >= len(CL)):
    data2[0:w, 0:h] = itransform2D(data[0:w, 0:h], CL)
    w /= 2
    h /= 2
plt.imshow(data2, cmap='gray')
plt.show()



