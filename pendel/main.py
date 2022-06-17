import pygame
import math
from time import sleep

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

def newcord(x ,y):
    newy = round(hScreen * 0.25 - x)
    newx = round(wScreen/2 + y)
    return(newx, newy)


class pend(object):
    def __init__(self, ang, lengthstr, radius):
        self.ang = math.radians(ang + 180)

        self.lengthstr = lengthstr
        self.radius = radius

        self.pos_xy = newcord(round(lengthstr * math.cos(self.ang)), round(lengthstr * math.sin(self.ang)))

        self.x = self.pos_xy[0]
        self.y = self.pos_xy[1]

    def draw (self, win):
        pygame.draw.circle(win, (0,0,0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (144, 144, 144), (self.x, self.y), self.radius-1)

pen1 = pend(0, 300, 10)


def redrawWindow():
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0, 0, 0), line[0], line[1])
    pen1.draw(win)

    pygame.display.update()

run = True
i = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    line = ((pen1.x, pen1.y), newcord(0, 0))

    if i < 360:
        i += 1
        pen1 = pend(i, 300, 12)

    sleep(0.01)



    redrawWindow()