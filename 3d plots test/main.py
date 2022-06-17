from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

def cos(ang):
    return np.cos((ang))

def floor(i):
    return np.floor(i)

def f(x, y):
    #return cos(abs(x)+abs(y))*(abs(x)+abs(y))
    e = np.exp(1)

    return (floor(-e**(-x*y/1)*cos( (x**2+y**2)/10 ))+14*np.log(10000/(x**2+y**2)+.01))*floor( cos(x**2+y**2)/10)+3*(np.ceil(x)-floor(x))*(np.ceil(y)-floor(y))



x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-150, 150)


plt.show()

