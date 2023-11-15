import pygame

pygame.init()

resolution_x = 100
resolution_y = 50

pixel_size = 4

wScreen = resolution_x * pixel_size
hScreen = resolution_y * pixel_size

win = pygame.display.set_mode((wScreen, hScreen))



class box(object):

    def __init__(self, x, y, width, hight, color):
        self.x = x
        self.y = y
        self.hight = hight
        self.width = width
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, (self.color), pygame.Rect(round(self.x), round(self.y), self.width, self.hight))


def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redrawWindow()






