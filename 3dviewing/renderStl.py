import pygame
import numpy as np
import math
from test import *

pygame.init()

wScreen = 1000
hScreen = 500

#win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win = pygame.display.set_mode((wScreen, hScreen))

clock = pygame.time.Clock()
cube_center = {'y': hScreen // 2, 'x': wScreen // 2}
fps = 60

file = "benedikt v2.STL"

ar = Listaveraging(file)

normals = getSurfaceNormals(file)

cube_vertices = ar

if not len(cube_vertices)//3 == len(normals):
    l1 = len(cube_vertices)//3
    l2 = len(normals)
    raise ValueError(f"Lists are different lenght (%s/%s)" % (l1, l2))


PointsToConnect = []

l = 0
for i in range(len(cube_vertices)//3):
    tempList = []
    for x in range(3):
        tempList.append(l)
        l += 1
    PointsToConnect.append(tempList)


xScale = 1
yScale = 1
zScale = 2

for x in range(len(cube_vertices)):
    cube_vertices[x][0] = cube_vertices[x][0] * xScale
    cube_vertices[x][1] = cube_vertices[x][1] * yScale
    cube_vertices[x][2] = cube_vertices[x][2] * zScale

PointsOfCube = [[0, 0, 0],
                [1, 0, 0]]


ProjectionMatrix = [[1, 0, 0],
                    [0, 1, 0]]

def drawtriangle(xy1, xy2, xy3):
    color = (255, 255, 255)
    pygame.draw.lines(win, color, True, (xy1, xy2), 2)
    pygame.draw.lines(win, color, True, (xy2, xy3), 2)
    pygame.draw.lines(win, color, True, (xy3, xy1), 2)

def drawpolygone(xy1, xy2, xy3, color):
    pygame.draw.polygon(win, color, [xy1, xy2, xy3])

background_color = (0, 0, 0)


angle = 3.14/3
angular_change = 0.01
distance = 3.001
Scale = 10

circle_radius = 2

yMove = 0
xMove = 0

MoveDistance = 3

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    win.fill(background_color)
    angle += angular_change

    # region RotationmatrixStuff(angle, distance)
    # prepare rotation matrix:
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

    try:
        z = 1 / distance
    except ZeroDivisionError:
        pass

    projection_matrix = [
        [z, 0, 0],
        [0, z, 0]
    ]

    # compute the final matrix:
    rotation_matrix = np.matmul(rotation_matrix_x, rotation_matrix_y)
    rotation_matrix = np.matmul(rotation_matrix_z, rotation_matrix)
    projection_rotation_matrix = np.matmul(projection_matrix, rotation_matrix)

    # endregion

    projected_vertices = []



    for p in range(len(cube_vertices)):
        # apply projection matrix to each cube vertex:
        zComponentofnormal = np.matmul(rotation_matrix, np.transpose(normals[p//3]))[2]
        if True:
            projected = np.matmul(projection_rotation_matrix, np.transpose(cube_vertices[p]))
            x = (cube_center['x'] + projected[0] * Scale) + xMove
            y = (cube_center['y'] + projected[1] * Scale) + yMove
            projected_vertices.append([x, y])

    # draw vertices as circles:
    for p in projected_vertices:
        pygame.draw.circle(win, (0, 0, 0), (p[0], p[1]), circle_radius)
    
    for el in PointsToConnect:
        drawtriangle(projected_vertices[el[0]], projected_vertices[el[1]], projected_vertices[el[2]])

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
        distance += 0.1

    if key_input[pygame.K_e]:
        distance -= 0.1

    if key_input[pygame.K_ESCAPE]:
        run = False




    pygame.display.update()
