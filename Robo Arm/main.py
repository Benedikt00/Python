from math import sqrt, radians, degrees , sin, cos, tan, atan, acos, asin

def angles(x, z):
    x = x
    c = sqrt(x**2 + z**2)
    if c > 1.0001:
        return
    if x != 0:
        phi = round(degrees(atan(z/x)))
    else:
        phi = 90
    a = 0.5000001
    alpha = round(degrees(acos((a**2 + a**2 - c**2)/(2*a*a))))
    beta = round((180 - alpha)/2)


    print("c ", round(c, 2), "phi + beta ", phi + beta, "alpha ", alpha, "beta ", beta)


angles(0, 1)
angles(0.5, 0.5)
angles(1, 0)
print()
angles(-0, 1)
angles(-0.5, 0.5)
angles(-1, 0)


