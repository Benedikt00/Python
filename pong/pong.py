import pygame
import sys
import math

pygame.init()

wScreen = 1000
hScreen = 900

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

class ball(object):
    def __init__(self, x, y, radius, color, velx, vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = round(vely)

        self.radius = radius

        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (self.color), (self.x, self.y), self.radius - 1)

def redrawWindow():
    win.fill((0, 0, 0))
    rpl.draw(win)
    lpl.draw(win)
    ball.draw(win)
    pygame.display.update()

lpl = box(20, (hScreen + 70)/2, 10, 70, (255, 255, 255))
rpl = box(wScreen - 40, (hScreen + 70)/2, 10, 70, (255, 255, 255))

ball = ball(wScreen/2, hScreen/2, 6, (255, 255, 255), 1, 0)


step = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_s]:
        if lpl.y <= hScreen - lpl.hight:
            lpl.y += step

    if key_input[pygame.K_w]:
        if lpl.y >= 0:
            lpl.y -= step

    if key_input[pygame.K_UP]:
        if rpl.y >= 0:
            rpl.y -= step

    if key_input[pygame.K_DOWN]:
        if rpl.y <= hScreen - rpl.hight:
            rpl.y += step

    ball.x = ball.x + round(ball.velx)
    ball.y = ball.y + round(ball.vely/20)

    if ball.x >= rpl.x and (ball.y >= rpl.y and ball.y <= rpl.y + rpl.hight):
        ball.velx = ball.velx * -1
        ball.vely = round(ball.y - (rpl.y + rpl.hight/2))

    if ball.x <= 30 and (ball.y >= lpl.y and ball.y <= lpl.y + rpl.hight):
        ball.velx = ball.velx * -1
        ball.vely = round(ball.y - (lpl.y + lpl.hight/2))

    if ball.y <= 0:
        ball.vely = ball.vely * -1

    if ball.y >= hScreen:
        ball.vely = ball.vely * -1

    if ball.x < -10 or ball.x > wScreen + 10:
        run = False

    redrawWindow()

