import pygame
import random
from time import sleep

lenList = 150

randList = []

for i in range(lenList):
    randList.append(i)

random.shuffle(randList)

wBlock = 5

pygame.init()

wScreen = (wBlock + 1)*lenList
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

def swap(list, a, b):
    n1 = list[a]
    n2 = list[b]

    list[a] = n2
    list[b] = n1
    return list

def redrawWindow():
    win.fill((255, 255, 255))
    for x in range(1, len(randList)):
        height = randList[x] * (hScreen/lenList)
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(round((wScreen/lenList) * x), round(hScreen - height), wBlock, height))
    pygame.display.update()




run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(0, len(randList) - 1):
        a = randList[i]
        b = randList[i + 1]
        if a > b:
            swap(randList, i, i + 1)
        redrawWindow()
        sleep(10/lenList**2)











