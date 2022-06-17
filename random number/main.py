import pyautogui as pg
import keyboard
import mouse
from time import sleep
import random

li = []
i = 1
while i < 10000000:
    rnd = random.randrange(0,1000)
    st = any(li in rnd for li in li)
    if st == True:
        li.append(rnd)
 #   if keyboard.is_pressed('space'):
  #      print(rnd)
    i += 1
print(li)





    


