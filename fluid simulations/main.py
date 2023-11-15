import pygame
import math

pygame.init()

X_LEN = 400

Y_LEN = 900

ratio = X_LEN / Y_LEN

hScreen = 600
wScreen = Y_LEN * ratio

win = pygame.display.set_mode((wScreen, hScreen))

U_FIELD = 0
V_FIELD = 1
S_FIELD = 2

cnt = 0
def cX(x):
    return x * cScale




class Fluid():
    def __init__(self, density, numX, numY, h):
        self.density = density
        self.numX = numX
        self.numY = numY
        self.numCells = self.numX * self.numY
        self.h = h
        self.u = [] * self.numCells
        self.v = [] * self.numCells
        self.newU = [] * self.numCells
        self.newV = [] * self.numCells
        self.p = [] * self.numCells
        self.s = [] * self.numCells
        self.m = [1] * self.numCells
        self.newM = [] * self.numCells
        num = numX * numY

    def integrate(self, dt, gravity):
        n = self.numY
        for i in range(1, self.numX):
            for j in range(1, self.numY-1):
                if (self.s[i*n + j] != 0) and (self.s[i*n + j-1] != 0):
                    self.v[i*n + j] += gravity *dt

    def solveIncompressibility(self, numIters, dt):

        n = self.numY
        cp = self.density * self.h / dt

        for iter in range(numIters):
            for i in range(1, self.numX-1):
                for j in range(1, self.numY-1):
                    if self.s[i*n + j] == 0:
                        continue

                    s = self.s[i*n +j]
                    sx0 = self.s[(i-1)*n +j]
                    sx1 = self.s[(i + 1) * n + j]
                    sy0 = self.s[i* n + j-1]
                    sy1 = self.s[i*n + j + 1]
                    s = sx0 + sx1 + sy0 + sy1
                    if s==0:
                        continue

                    div = self.u[(i+1)*n + j] - self.u[i*n + j] + self.v[i*n +j+1] - self.v[i*n + j]
                    p = -div/s
                    p *= scene.overRelaxation
                    self.p[i*n + j+1] += cp*p

                    self.u[i*n + j] -= sx0 *p
                    self.u[(i + 1) * n + j] += sx1 * p
                    self.v[i * n + j] -= sy0 * p
                    self.v[i * n + j + 1] += sy1 * p

    def extrapolate(self):
        n = self.numY
        for i in range(self.numX):
            self.u[i*n + 0] = self.u[i*n +1]
            self.u[i*n + self.numY-1] = self.u[i*n + self.numY - 2]

        for j in range(self.numY):
            self.v[0*n + j] = self.v[1*n+j]
            self.v[(self.numX -1)*n+j] = self.v[(self.numX-2)*n +j]

    def sampleField(self, x, y, field):
        n = self.numY
        h = self.h
        h1 = 1/h
        h2 = h/2

        x = max(min(x, self.numX * h), h)
        y = max(min(y, self.numY * h), h)

        dx = 0
        dy = 0

        if field == U_FIELD:
            f = self.u
            dy = h2
        elif field == V_FIELD:
            f = self.v
            dx = h2
        elif field == S_FIELD:
            f = self.m
            dx = h2
            dy = h2

        x0 = min(math.floor((x-dx)*h1), self.numX-1)
        tx = ((x-dx) - x0*h) * h1
        x1 = min(x0 + 1, self.numX-1)

        y0 = min(math.floor((y-dy)*h1), self.numY-1)
        ty = ((x - dx) - x0 * h) * h1
        y1 = min(y0 + 1, self.numY - 1)

        sx = 1 - tx
        sy = 1 - ty

        val = sx*sy * f[x0*n + y0] + tx*sy * f[x1*n + y0] + tx*ty * f[x1*n + y1] + sx*ty * f[x0*n + y1]

        return val












