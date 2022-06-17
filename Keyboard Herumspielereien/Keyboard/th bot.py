import pyautogui as pg
import keyboard
import mouse
from time import sleep

#th bot

while True:
        if keyboard.is_pressed('m'):
            sleep(1)
            pg.hotkey('backspace')
            mouse.move(1050, 930, absolute=True)
            mouse.wheel(50)
            sleep(0.5)
            mouse.wheel(50)
            for i in range(5):
                mouse.wheel(-5)
                sleep(1.7)
            mouse.click('left')



        elif keyboard.is_pressed('space'):
            exit()



