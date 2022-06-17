import cmath
import math
import numpy as np

i = 64.79*10**-3
r = 10000
l = 5*10^-3
c = 10^-6

f = 2.25*10**-3

w = 2 * math.pi * f

Xl = w * 1j * l
Xc = 1/(w* 1j * c)

def P2R(radii, angles):
    return radii * np.exp(1j*angles)

def R2P(x):
    return abs(x), np.angle(x)


    
z = 1/((1/r)+(1/Xl)+(1/Xc))

U = i * z

Ir = U/r

Ic = U/Xc

Il = U/Xl

Is = i*-1

S = U * Is

S_r = Ir*-1*U
S_c = Ic *-1 * U
S_l = Il * -1 * U

S_c = R2P(S_c)

S_c = list(S_c)

S_c[1] = math.degrees(S_c[1])

print(S_c)

#print(R2P(Xc))