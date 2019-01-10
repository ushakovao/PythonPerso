import wave
from struct import pack
import math
import re
from sys import argv


c2 = 523.251
b = 493.883
aSharp = 466.164
a = 440.000
gSharp = 415.305
g = 391.995
fSharp = 369.994
f = 349.228
e = 329.628
dSharp = 311.127
d = 293.665
cSharp = 277.183
c1 = 261.626

sig=np.sin(2*np.pi*440*t)*np.sin(2*np.pi*t)



sf.write('la440.wav', sig, samplerate)

"""traçons l'intégralité du signal ; essayez de tracer le tout début seulement pour voir les oscillations rapides"""
plt.plot(t,sig)
plt.show()
