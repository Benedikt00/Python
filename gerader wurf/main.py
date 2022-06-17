import pygame

pygame.init()


g = 9.81

wScreen = 1800
hScreen = 600

win = pygame.display.set_mode((wScreen, hScreen))
win.fill((255, 255, 255))

class ball(object):
    def __init__(self, y, radius):
        self.y = y
        self.radius = radius
        self.x = 30

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (124, 3, 50), (self.x, self.y), self.radius + 1)

class box(object):
    def __init__(self,x ,y , hight, color):
        self.x = x
        self.y = y

        self.hight = hight
        self.color = color

    def draw (self, win):
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(round(self.x), round(self.y), self.hight, self.hight))
        pygame.draw.rect(win, (self.color), pygame.Rect(round(self.x) , round(self.y), self.hight - 2, self.hight - 2))


def pos(time, startvel):
    t = time
    y = startvel * t - 0.5 * g * t**2
    return y

ball = ball(570, 7)
tbox = box(100, 100, 10, (0, 0, 0))


def redrawWindow():

    pygame.draw.rect(win, (255, 255, 255), pygame.Rect( 0, 0, 100, hScreen))

    ball.draw(win)
    tbox.draw(win)
    pygame.display.update()


run = True
time = 0
i = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time += 0.01
    i += 1


    ball.y = hScreen - pos(time, 100)

    if ball.y > hScreen:
        time = 0

    tbox.y = ball.y
    tbox.x += 0.3

    redrawWindow()






