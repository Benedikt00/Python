import cmath
import math


def comp_to_deg(cnum):
    return round(abs(cnum), 3), round(math.degrees(cmath.phase(cnum)), 3)


def deg_to_comp(abs, ang):
    return cmath.rect(abs, math.radians(ang))


U = 400

dreileiter = False

Uq1 = deg_to_comp(400 / math.sqrt(3), 90)
Uq2 = deg_to_comp(400 / math.sqrt(3), -30)
Uq3 = deg_to_comp(400 / math.sqrt(3), 210)

Z1 = deg_to_comp(82, 0)
Z2 = deg_to_comp(5.124, 90)
Z3 = deg_to_comp(38.8183, -90)

I1 = Uq1/Z1
I2 = Uq2/Z2
I3 = Uq3/Z3

I0 = -(I1 + I2 + I3)

U0 = I0/(1/Z1 + 1/Z2 + 1/Z3)

U1 = Uq1 + U0
U2 = Uq2 + U0
U3 = Uq3 + U0

I1d = U1/Z1
I2d = U2/Z2
I3d = U3/Z3

if dreileiter:
    print(f"3 Leiter \n"
          f"U1: {comp_to_deg(U1)}\nU2: {comp_to_deg(U2)}\nU3: {comp_to_deg(U3)}\n\nU0: {comp_to_deg(U0)}\n\n"
          f"I1: {comp_to_deg(I1d)}\nI2: {comp_to_deg(I2)}\nI3: {comp_to_deg(I3d)}")
else:
    print(f"4 Leiter\n"
          f"I1: {comp_to_deg(I1)}\nI2: {comp_to_deg(I2)}\nI3: {comp_to_deg(I3)}\n\nI0: {comp_to_deg(I0)}")