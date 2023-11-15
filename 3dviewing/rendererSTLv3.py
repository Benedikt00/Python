import pygame
import numpy as np
import math
from renderv2Functions import *

pygame.init()

wScreen = 1000
hScreen = 500

# win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win = pygame.display.set_mode((wScreen, hScreen))

clock = pygame.time.Clock()
fps = 50

file = "benedikt v2.STL"

listTriangle = STLtoList(file, True)

normals = getSurfaceNormals(file)

center = [wScreen//2, hScreen//2]

camera = [0, 0, 1]

lightDirection = [0, 0, 1]

xScale = 1
yScale = 1
zScale = 2

lastZScale = zScale

for x in range(len(listTriangle)):
    for y in range(len(listTriangle[x])):
        listTriangle[x][y][0] = listTriangle[x][y][0] * xScale
        listTriangle[x][y][1] = listTriangle[x][y][1] * yScale
        listTriangle[x][y][2] = listTriangle[x][y][2] * zScale

ProjectionMatrix = [[1, 0, 0],
                    [0, 1, 0]]

background_color = (0, 0, 0)

angle = 3.14/3
angular_change = 0.01
distance = 3.001
Scale = 10

circle_radius = 2

yMove = 0
xMove = 0

MoveDistance = 3

def drawtriangle(xy1, xy2, xy3):
    color = (255, 255, 255)
    pygame.draw.lines(win, color, True, (xy1, xy2), 2)
    pygame.draw.lines(win, color, True, (xy2, xy3), 2)
    pygame.draw.lines(win, color, True, (xy3, xy1), 2)


def drawpolygone(xy1, xy2, xy3, color):
    pygame.draw.polygon(win, color, [xy1, xy2, xy3])


def getRotationMatrix(angle):
    rotation_matrix_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotation_matrix_y = [
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ]

    rotation_matrix_z = [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]

    # compute the final matrix:
    rotation_matrix = np.matmul(rotation_matrix_x, rotation_matrix_y)
    rotation_matrix = np.matmul(rotation_matrix_z, rotation_matrix)

    return(rotation_matrix)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    win.fill(background_color)
    angle += angular_change

    try:
        z = 1 / distance
    except ZeroDivisionError:
        pass

    projection_matrix = [
        [z, 0, 0],
        [0, z, 0]
    ]

    rotation_matrix = getRotationMatrix(angle)

    projection_rotation_matrix = np.matmul(projection_matrix, rotation_matrix)

    TriAfterRotation = []
    for el in range(len(listTriangle)):
        av = [np.matmul(rotation_matrix, np.transpose(listTriangle[el][0])), np.matmul(rotation_matrix, np.transpose(listTriangle[el][1])), np.matmul(rotation_matrix, np.transpose(listTriangle[el][2]))]
        TriAfterRotation.append(av)

    sortListforZ(TriAfterRotation)

    #print(TriAfterRotation)

    for el in range(len(TriAfterRotation)):
        normal = np.matmul(rotation_matrix, normals[el])

        ck = normal[0] * camera[0] + normal[1] * camera[1] + normal[2] * camera[2] #dot product

        if ck > 0:

            sth = normal[0] * lightDirection[0] + normal[1] * lightDirection[1] + normal[2] * lightDirection[2]
            rgb = abs(255 * sth)

            color = (rgb, rgb, rgb)

            el = listTriangle[el]

            p0 = np.matmul(projection_rotation_matrix, np.transpose(el[0]))
            p1 = np.matmul(projection_rotation_matrix, np.transpose(el[1]))
            p2 = np.matmul(projection_rotation_matrix, np.transpose(el[2]))
            #                       x                                    y
            p0ap = ((center[0] + p0[0] * Scale) + xMove, (center[1] + p0[1] * Scale) + yMove)
            p1ap = ((center[0] + p1[0] * Scale) + xMove, (center[1] + p1[1] * Scale) + yMove)
            p2ap = ((center[0] + p2[0] * Scale) + xMove, (center[1] + p2[1] * Scale) + yMove)

            drawpolygone(p0ap, p1ap, p2ap, color)

    keys = pygame.key.get_pressed()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_s]:
        yMove += MoveDistance

    if key_input[pygame.K_w]:
        yMove -= MoveDistance

    if key_input[pygame.K_a]:
        xMove -= MoveDistance

    if key_input[pygame.K_d]:
        xMove += MoveDistance

    if key_input[pygame.K_SPACE]:
        xMove = 0
        yMove = 0

    if key_input[pygame.K_q]:
        if distance > 1:
            distance -= 0.1

    if key_input[pygame.K_e]:
        distance += 0.1

    if key_input[pygame.K_ESCAPE]:
        run = False

    pygame.display.update()