import keyboard
import mouse
import image

from time import sleep

sleep(5)

i = 1

while i < 1000:
    i += 1
    mouse.press('left')
    sleep(0.1)
    mouse.release('left')
    sleep(300)
    print(i)
else:
    print("Stopped")

#-200 1400



