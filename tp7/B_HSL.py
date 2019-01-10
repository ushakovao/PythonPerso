import math

import imageio
import numpy as np
import matplotlib.pyplot as plt
import math
import colorsys
from PIL import Image

"""
RVB : rouge Vert bleu
défini l'espace 3d des couleurs
Attention 2 conventions possibles les composantes RGB peuvent prendre
des valeurs entière dans l'intervalle [0,255] ou bien
des valeurs réelles dans l'intervalle [0,1].


Deux autre systèmes, basée sur la perception psychologique de la lumière :
TSL : Teinte Saturation Luminosité = HSL : Hue Saturation Lightness
TSV : Teinte Saturation Valeur     = HSV : Hue Saturation Value
Pour voir la différence : https://en.wikipedia.org/wiki/HSL_and_HSV


Ici on va plutôt s'intéressre à TSL=HSL. Le mieux pour comprendre comment on passe de RVB à TSL est
d'observer cette petite appli javascript :
http://www.f-legrand.fr/scidoc/simul/image/espaceRGB.html
Plus d'explication au tableau lors du TP.

Des explications écrite peuvent être trouvée en français ici :
http://www.f-legrand.fr/scidoc/docmml/image/niveaux/couleurs/couleurs.html
C'est de cette page que sont tiré les bouts de code ci-dessous.


Signalons un autre système très important, le systèem Luminance/chrominance
son petit nom étant YCbCr
qu'on verra plus tard lors de la compression JPEG


Signalons enfin qu'il a des dizaines d'autres systèmes de colorimétrie qui ont leur défenseurs et leur détracteurs.

"""



def rvb2tsl(rvb):
    r = rvb[0] * 1.0
    v = rvb[1] * 1.0
    b = rvb[2] * 1.0
    somme = r + v + b
    r /= somme
    v /= somme
    b /= somme
    Max = max(r, v, b)
    Min = min(r, v, b)
    C = Max - Min
    L = Max
    if L == 0:
        return [0, 0, 0]
    S = C / L
    if C == 0:
        return [0, 0, L]
    if max == r:
        T = 60.0 * (v - b) / C % 360
    elif max == v:
        T = 120.0 + 60.0 * (b - r) / C
    else:
        T = 240.0 + 60.0 * (r - v) / C
    return [T, S, L]


def tsl2rvb(tsl):
    T = tsl[0] * 1.0
    S = tsl[1] * 1.0
    L = tsl[2] * 1.0
    C = L * S
    Min = L - C
    if (T > 300) and (T <= 360):
        r = L
        v = Min
        b = v + C * (360.0 - T) / 60
    elif (T >= 0) and (T <= 60):
        r = L
        b = Min
        v = b + C * (T / 60)
    elif (T > 60) and (T <= 120):
        v = L
        b = Min
        r = b + C * (120.0 - T) / 60
    elif (T > 120) and (T <= 180):
        v = L
        r = Min
        b = r + C * (T - 120.0) / 60
    elif (T > 180) and (T <= 240):
        b = L
        r = Min
        v = r + C * (240.0 - T) / 60
    else:
        b = L
        v = Min
        r = v + C * (T - 240.0) / 60
    return [r, v, b]


def disqueTSL():
    Ncol = 300
    Nlignes = 300
    img = np.zeros((Nlignes,Ncol,4))
    dx = 2.0/(Ncol-1)
    dy = 2.0/(Nlignes-1)
    rad2deg = 180.0/math.pi
    for i in range(Ncol):
        for j in range(Nlignes):
            x=-1.0+i*dx
            y=-1.0+j*dy
            r = math.sqrt(x*x+y*y)
            if r<1.0:
                if x==0:
                    if y>0:
                        a = 90.0
                    else:
                        a = -90.0
                else:
                    a = math.atan(y/x)*rad2deg
                if x<0:
                    a += 180.0
                a %= 360
                rvb = tsl2rvb([a,r,1.0])
                img[j][i] = np.array([rvb[0],rvb[1],rvb[2],1.0])
            else:
                img[j][i] = np.array([1.0,1.0,1.0,0.0])
    plt.imshow(img,origin='lower',extent=[-1,1,-1,1])
    plt.show()

def plasma (w, h):
	out = Image.new("RGB", (w, h))
	pix = out.load()
	for x in range (w):
		for y in range(h):
			hue = 4.0 + math.sin(x / 19.0) + math.sin(y / 9.0) \
				+ math.sin((x + y) / 25.0) + math.sin(math.sqrt(x**2.0 + y**2.0) / 8.0)
			hsv = colorsys.hsv_to_rgb(hue/8.0, 1, 1)
			pix[x, y] = tuple([int(round(c * 255.0)) for c in hsv])
	return out


def mystep():
    img = imageio.imread("../assets/img/ernst.jpg")

    img_new = rvb2tsl(img)

    t = img_new[:,:,0]
    l = img_new[:,:,1]
    c = img_new[:,:,2]

    plt.subplot(1, 3, 1)
    plt.imshow(t)
    plt.subplot(1, 3, 2)
    plt.imshow(l)
    plt.subplot(1, 3, 3)
    plt.imshow(c)
    plt.show()

def notmine():

    LenaImage1 = Image.open('../assets/img/bb.jpg')
    r, g, b = LenaImage1.split()
    Hdat = []
    Ldat = []
    Sdat = []
    for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
        h, l, s = colorsys.rgb_to_hls(rd / 255., gn / 255., bl / 255.)
        Hdat.append(int(h * 255.)%360)
        Ldat.append(int(l * 255.))
        Sdat.append(int(s * 255.))

    r.putdata(Hdat)
    g.putdata(Ldat)
    b.putdata(Sdat)
    LenaImage1.save('r.jpg')
    newimg = Image.merge('RGB', (r, g, b))
    newimg.save('lenaHSV.jpg')


if __name__=='__main__':
    notmine()


"""Travail : prenez une image RGB sympa, transformez la en une image TSL,
 effectuer un décalage des teintes (modulo 360), puis re-transformez-là en rgb pour l'afficher """
