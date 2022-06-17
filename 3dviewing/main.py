import pygame
import numpy as np
import math


pygame.init()

wScreen = 1000
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

clock = pygame.time.Clock()
cube_center = {'y': hScreen // 2, 'x': wScreen // 2}
fps = 60

VerteciesOfobject = [
    #Vorne
    [0, 0, 0,    0, 1, 0,    1, 1, 0],
    [0, 0, 0,    1, 1, 0,    1, 0, 0],

    #Rechts
    [1, 0, 0,    1, 1, 0,    1, 1, 1],
    [1, 0, 0,    1, 1, 1,    1, 0, 1],

    #Hinten
    [1, 0, 1,    1, 1, 1,    0, 1, 1],
    [1, 0, 1,    0, 1, 1,    0, 0, 1],

    #Links
    [0, 0, 1,    0, 1, 1,    0, 1, 0],
    [0, 1, 0,    1, 1, 1,    1, 1, 0],

    #Oben
    [0, 1, 1,    0, 1, 1,    1, 1, 1],
    [0, 1, 0,    1, 1, 1,    1, 1, 0],

    #Unten
    [1, 0, 1,    0, 0, 1,    0, 0, 0],
    [1, 0, 1,    0, 0, 0,    1, 0, 0]
]


cube_vertices = [
    [-1,-1, 1],
    [ 1,-1, 1],
    [ 1, 1, 1],
    [-1, 1, 1],
    [-1,-1,-1],
    [ 1,-1,-1],
    [ 1, 1,-1],
    [-1, 1,-1],
    [ 0, 0, 0],
    [ 2, 2, 2]
]

PointsToConnect = [
    [1, 2, 3],
    [1, 5, 8],
    [1, 4, 8],
    [6, 5, 2],
    [7, 2, 3],
    [7, 4, 3],
    [7, 6, 8]

]

PointsOfCube = [[0, 0, 0],
                [1, 0, 0]]


ProjectionMatrix = [[1, 0, 0],
                    [0, 1, 0]]

def drawtriangle(xy1, xy2, xy3):
    pygame.draw.lines(win, (0, 0, 0), True, (xy1, xy2), 2)
    pygame.draw.lines(win, (0, 0, 0), True, (xy2, xy3), 2)
    pygame.draw.lines(win, (0, 0, 0), True, (xy3, xy1), 2)




class olcEngine3D():
    pass






background_color = (240, 235, 240)


angle = 3.14/3
angular_change = 0.01
distance = 2
scale = 20
circle_radius = 7
xAngle = 0
yAngle = 0
zAngle = 0


xAngle = math.radians(xAngle)
yAngle = math.radians(yAngle)
zAngle = math.radians(zAngle)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(fps)
    win.fill(background_color)
    angle += angular_change

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

    z = 1 / distance

    projection_matrix = [
        [z, 0, 0],
        [0, z, 0]
    ]

    # compute the final matrix:
    rotation_matrix = np.matmul(rotation_matrix_x, rotation_matrix_y)
    rotation_matrix = np.matmul(rotation_matrix_z, rotation_matrix)
    projection_rotation_matrix = np.matmul(projection_matrix, rotation_matrix)
    projected_vertices = []


    for p in cube_vertices:
        # apply projection matrix to each cube vertex:
        projected = np.matmul(projection_rotation_matrix, np.transpose(p))
        x = cube_center['x'] + projected[0] * scale
        y = cube_center['y'] + projected[1] * scale
        projected_vertices.append([x, y])

    # draw vertices as circles:
    for p in projected_vertices:
        pygame.draw.circle(win, (0, 0, 0), (p[0], p[1]), circle_radius)

    # draw lines
    for el in PointsToConnect:
        drawtriangle(projected_vertices[el[0]-1], projected_vertices[el[1]-1], projected_vertices[el[2]-1])

    pygame.display.update()
