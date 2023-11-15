import cmath
import math


def comp_to_deg(cnum):
    return round(abs(cnum), 3), round(math.degrees(cmath.phase(cnum)), 3)


def deg_to_comp(abs, ang):
    return cmath.rect(abs, math.radians(ang))


U = 400


U12 = deg_to_comp(U, 0)
U23 = deg_to_comp(U, 0)
U31 = deg_to_comp(U, -120)

zr = 78.5
g = -37

Z12 = deg_to_comp(zr, g)
Z23 = deg_to_comp(zr, g)
Z31 = deg_to_comp(zr, g)

I12 = U12/Z12
I23 = U23/Z23
I31 = U31/Z31

I1 = I12 - I31
I2 = I23 - I12
I3 = I31 - I23


print("I Strang: ", comp_to_deg(I12)[0])

S_ = (U12*I12*3)
S = abs(comp_to_deg(S_)[0])

print("S: ", S)

Phi = comp_to_deg(S_)[1]

P = math.cos(math.radians(Phi)) * S

Q = math.sin(math.radians(Phi)) * S

print("P: ", P, " W")
print("Q: ", abs(Q), " VAr")

print("I leiter: ", comp_to_deg(I12)[0] * math.sqrt(3))

#print(f"I1: {comp_to_deg(I1)}\nI2: {comp_to_deg(I2)}\nI3: {comp_to_deg(I3)}")










