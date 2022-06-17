from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position : X 2536 Y:469
#Tile 2 Position : X 2619 Y:469
#Tile 3 Position : X 2717 Y:469
#Tile 4 Position : X 2804 Y:469

sleep(1)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(2536, 700)[0] == 0:
        click(2536, 700)
    if pyautogui.pixel(2619, 700)[0] == 0:
        click(2619, 700)
    if pyautogui.pixel(2717, 700)[0] == 0:
        click(2717, 700)
    if pyautogui.pixel(2804, 700)[0] == 0:
        click(2804, 700)

