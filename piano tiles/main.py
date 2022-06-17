import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui as pg
from time import sleep
import keyboard as k

screen_width = 0
screen_height = 0

speed = 10

from screeninfo import get_monitors
for m in get_monitors():
    if m.is_primary == True:
        screen_width = m.width
        screen_height = m.height

space = screen_width/5

row_x = []

for i in range(1,5):
    row_x.append(int(i * space))

pg.click(1800, 10)
sleep(0.1)
#img = np.array(pg.screenshot())
img = ImageGrab.grab()


run = True

score = 50

while run:
    img = ImageGrab.grab()

    for i in row_x:
        rgb = img.getpixel((i, screen_height - 400 + score))
        if rgb != (200, 200, 255) and rgb != (0, 129, 210):
            pg.click(i,screen_height - 250)
            score += 3


    if k.is_pressed('a'):
        run = False





