import pygame

pygame.init()

wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

clock = pygame.time.Clock()

class box():
    def __init__(self, x, y, height, width, color, rotation = 0):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rotation = rotation
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

def redrawWindow():
    win.fill((0, 0, 0))
    b1.draw(win)
    b2.draw(win)
    pygame.display.update()


run = True

b1 = box(0, 0, 50, 50, (255, 255, 255))
b2 = box(200, 200, 50, 50, (100, 100, 100))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_s]:
        if b1.y <= hScreen - b1.height :
            b1.y += 1

    if key_input[pygame.K_w]:
        if b1.y >= 0:
            b1.y -=1

    if key_input[pygame.K_a]:
        if b1.x >= 0:
            b1.x -= 1

    if key_input[pygame.K_d]:
        if b1.x <= wScreen - b1.width :
            b1.x += 1

    if key_input[pygame.K_DOWN]:
        if b2.y <= hScreen - b2.height :
            b2.y += 1

    if key_input[pygame.K_UP]:
        if b2.y >= 0:
            b2.y -=1

    if key_input[pygame.K_LEFT]:
        if b2.x >= 0:
            b2.x -= 1

    if key_input[pygame.K_RIGHT]:
        if b2.x <= wScreen - b2.width :
            b2.x += 1

    redrawWindow()






