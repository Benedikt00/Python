import pygame

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))


def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redrawWindow()






