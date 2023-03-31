from sympy import *


x = symbols('x', real=True)
f = 3*x**3 + x**2 + 4

#2 Ableitungen
fs = diff(f, x)
fss = diff(fs, x)
fsss = diff(fss, x)

#3 Nulstellen
ns = solve(f, x, domain=S.Reals)
print(round(ns[0], 2))
