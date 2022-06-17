import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sine Wave")

class circle:
    def __init__(self, radius):
        self.radius = radius

        self.x = self.radius + 30
        
        self.y = HEIGHT/2

        self.distanceToMiddlepoint = self.radius/1.3
        self.radiusSmallCircle = self.radius/10

        self.ang = 0

        self.kcy = 0
        self.kcx = 0

    def draw(self, win):
        pygame.draw.circle(win, (250, 60, 40), (self.x, self.y), self.radius)
        pygame.draw.circle(win, (0, 0, 0), (round(self.x - self.kcx), round(self.y + self.kcy)), self.radiusSmallCircle)

class ball:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, (30, 30, 30), (self.x, self.y), self.radius)



def newPos(ang, distanceToMiddlepoint):
    kcy = round(distanceToMiddlepoint * math.sin(math.radians(ang * -1)))
    kcx = round(distanceToMiddlepoint * math.cos(math.radians(ang + -1)))
    return kcx, kcy

circlel = circle(HEIGHT / 3)
drawb = ball(3, 200, HEIGHT/2)

def main():

    time = 0
    i = 0

    run = True
    clock = pygame.time.Clock()

    time = 0

    while run:

        clock.tick(60)
        WIN.fill((255, 255, 255))

        time += 1

        newXY = newPos(time , circlel.distanceToMiddlepoint)

        circlel.kcy = newXY[1]
        circlel.kcx = newXY[0]

        drawb.y = round(circlel.y + newXY[1])
        drawb.x = time + (circlel.radius * 2 * 1.7)


        drawb.draw(WIN)
        circlel.draw(WIN)
        pygame.draw.lines(WIN, (0, 0, 0), False, [(450, HEIGHT/2), (WIDTH, HEIGHT/2)], 2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main()




