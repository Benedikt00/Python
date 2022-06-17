import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = np.linspace(0, 2* np.pi, 100)
Y = np.sin(X)

fig, ax = plt.subplots(1,1)
ax.set_xlim([0, 2 * np.pi])
ax.set_ylim([-1.1, 1.1])

sinegraph, = ax.plot([], [])
dot, = ax.plot([], [], 'o', color='red')

def sine(i):
    sinegraph.set_data(X[:i],Y[:i])
    dot.set_data(X[i],Y[i])

anim = animation.FuncAnimation(fig, sine, frames=len(X), interval=50)
plt.show()