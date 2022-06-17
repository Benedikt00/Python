import cmath
import matplotlib.pyplot as plt

data = []
s = []

stepSzise = 0.005

ymin = -1
ymax = 1
xmin = -1.5
xmax = 0.5

def checkifconw(cp):
    v = 0
    for x in range(100):
        v = v*v + cp

        if v.imag + v.real >= 100:
            return True
    return False



while ymin <= ymax:
    newxmin = xmin
    imgPt = ymin
    ymin += stepSzise
    while newxmin <= xmax:
        relPt = newxmin
        newxmin += stepSzise
        cNum = complex(round(relPt, 3), round(imgPt, 3))
        if checkifconw(cNum):
            data.append(cNum)
            s.append(0.1)

# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]

# plot the complex numbers
plt.scatter(x, y, s)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()