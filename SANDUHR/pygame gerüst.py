import pygame
from getthefuckingposis import getGridCords

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

class grid(object):
    def __init__(self, pos):
        self.pos = pos

        self.on = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.color = (255, 140, 140)

        self.ledpos = getGridCords(4, 15)

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (50, 50), 15)

def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()
    og.draw(win)


run = True

og = grid((100, 100))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redrawWindow()






