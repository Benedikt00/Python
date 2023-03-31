import cmath
import math


def comp_to_deg(cnum):
    return round(abs(cnum), 3), round(math.degrees(cmath.phase(cnum)), 3)


def deg_to_comp(abs, ang):
    return cmath.rect(abs, math.radians(ang))


U = 400


U12 = deg_to_comp(U, 120)
U23 = deg_to_comp(U, 0)
U31 = deg_to_comp(U, -120)

Z12 = deg_to_comp(80, 50)
Z23 = deg_to_comp(50, 60)
Z31 = deg_to_comp(80, -20)

I12 = U12/Z12
I23 = U23/Z23
I31 = U31/Z31

I1 = I12 - I31
I2 = I23 - I12
I3 = I31 - I23

print(f"I1: {comp_to_deg(I1)}\nI2: {comp_to_deg(I2)}\nI3: {comp_to_deg(I3)}")










