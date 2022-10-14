import pygame

pygame.init()

X_LEN = 400

Y_LEN = 900

ratio = X_LEN / Y_LEN

hScreen = 600
wScreen = Y_LEN * ratio

zero = [30, hScreen - 80]

win = pygame.display.set_mode((wScreen, hScreen))

def convertFromMachineToCoords(cords):
    corners = [zero, [wScreen - 30, zero[1]], [wScreen - 30, 30], [30, 30]]
    LW_Bed = [corners[2][0] - corners[3][0], corners[0][1] - corners[3][1]]
    eg = [int(cords[0] * LW_Bed[0]) / X_LEN, int(cords[1] * LW_Bed[1]) / Y_LEN]
    return eg

def checkIfPositionIsValid(position):
    if (-1 < position[0] < X_LEN) and (-1 < position[1] < Y_LEN):
        return True
    return False


class bed():
    def __init__(self, screenDimensions, bedSzise):
        self.screenWidth = screenDimensions[0]
        self.screenHeight = screenDimensions[1]

        self.bedWidth = bedSzise[0]
        self.bedHeight = bedSzise[1]
        self.zero = zero
        self.frameThickness = 20

    def draw_bed(self, win):

        pygame.draw.rect(win, (155, 155, 155), pygame.Rect(10, 10, self.frameThickness, self.screenHeight - 80))
        pygame.draw.rect(win, (155, 155, 155), pygame.Rect(self.screenWidth - 10 - self.frameThickness, 10, self.frameThickness, self.screenHeight - 80))

class motor(object):
    def __init__(self, position, rotation):
        self.x = position[0]
        self.y = position[1]
        self.rotation = rotation
        self.height = 60


    def draw(self, win):
        pygame.draw.rect(win, (100, 100, 100), pygame.Rect(round(self.x - self.height / 2), round(self.y - self.height / 2), self.height, self.height))
        pygame.draw.circle(win, (192, 192, 192), (self.x, self.y), 18)


class cnc_head():
    def __init__(self, position):
        self.position = position
        self.zero = zero

    def draw(self, win):

        self.PosRelToZero = [self.zero[0] + self.position[0], self.zero[1] - self.position[1]]

        pygame.draw.circle(win, (0, 0, 0), self.PosRelToZero, 5)
        pygame.draw.rect(win, (144, 144, 144), pygame.Rect(1, self.PosRelToZero[1] - 15, wScreen, 15))
        #print(self.position)

def home(ak_pos):
    homed_x = False
    homed_y = False

    x = ak_pos[0]
    y = ak_pos[1]

    while not homed_x:
        x -= 1
        if x <= 0:
            x = 0
            homed_x = True
        head.position = convertFromMachineToCoords([x, y])
        redraw_window()

    while not homed_y:
        y -= 1
        if y <= 0:
            y = 0
            homed_y = True
        head.position = convertFromMachineToCoords([x, y])
        redraw_window()


bed = bed([wScreen, hScreen], [X_LEN, Y_LEN])
motor1 = motor([40, hScreen - 40], 0)
motor2 = motor([wScreen - 40, hScreen - 40], 0)
head = cnc_head([0, 0])


def redraw_window():
    win.fill((255, 255, 255))

    bed.draw_bed(win)
    motor1.draw(win)
    motor2.draw(win)
    head.draw(win)

    pygame.display.update()


run = True

xy_head_pos = [0, 0]

clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_w]:
        if checkIfPositionIsValid([xy_head_pos[0], xy_head_pos[1] + 5]):
            xy_head_pos[1] += 5

    if key_input[pygame.K_s]:
        if checkIfPositionIsValid([xy_head_pos[0], xy_head_pos[1] - 5]):
            xy_head_pos[1] -= 5

    if key_input[pygame.K_a]:
        if checkIfPositionIsValid([xy_head_pos[0] - 5, xy_head_pos[1]]):
            xy_head_pos[0] -= 5

    if key_input[pygame.K_d]:
        if checkIfPositionIsValid([xy_head_pos[0] + 5, xy_head_pos[1]]):
            xy_head_pos[0] += 5

    if key_input[pygame.K_SPACE]:
        home(xy_head_pos)
        xy_head_pos = [0, 0]

    if checkIfPositionIsValid(xy_head_pos):
        head.position = convertFromMachineToCoords(xy_head_pos)

    redraw_window()

    clock.tick(30)
