import pygame
import time
from getthefuckingposis import getGridCords


pygame.init()

wScreen = 500
hScreen = 700

WIN = pygame.display.set_mode((wScreen, hScreen))

class ledfield(object):
    def __init__(self, pos):

        self.pos = pos

        self.on = [0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0]
        self.color = (255, 140, 140)

        self.ledpos = getGridCords(4, 50)


    def draw(self, win):
        for el in range(len(self.ledpos)):
            pygame.draw.circle(win, self.color, (round(self.ledpos[el][0]) + 100, round(self.ledpos[el][1] + 700)), 15)




win = pygame.display.set_mode((wScreen, hScreen))


def redrawWindow():
    win.fill((0, 0, 0))
    upf.draw(WIN)
    pygame.display.update()


run = True

upf = ledfield((50, 50))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redrawWindow()


