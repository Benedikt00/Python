import matplotlib.pyplot as plt
import math as maths

def getGridCords(lenght, distance):
    cb = []
    x = 0
    y = 4
    ds = distance
    a, b, d = 0, 0, 0
    c = lenght - 1
    for i in range(1, lenght * 2):
        if i <= lenght:
            if i % 2 == 1:
                x -= (i - 1) * ds / 2
                for k in range(i):
                    cb.append((x, y))
                    x += ds
            if i % 2 == 0:

                x -= ds * (0.5 + a)
                for n in range(i):
                    cb.append((x, y))
                    x += ds
                a += 1
            x = 0
            y -= ds

        else:

            if c % 2 == 1:
                x -= (c - 1) * ds / 2
                for k in range(c):
                    cb.append((x, y))
                    x += ds

            if c % 2 == 0:

                if lenght % 2 == 0:
                    x -= ds * (0.5 + a - 2)
                else:
                    x -= ds * (0.5 + a - 1)
                a -= 1
                for n in range(c):
                    cb.append((x, y))
                    x += ds
            x = 0
            y -= ds
    return cb

t = getGridCords(4, 50)
y = []
x = []

for el in t:
    y.append(el[0])

for el in t:
    x.append(el[1])

plt.scatter(x, y)
plt.show()



