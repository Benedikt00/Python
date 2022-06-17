import pygame
from time import sleep

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

win.fill((255, 255, 255))
pygame.draw.circle(win, (0, 0, 0), (20, 20), 7)
pygame.display.update()
sleep(2)