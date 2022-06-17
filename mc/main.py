import keyboard
import mouse
from time import sleep

sleep(5)

i = 0

while i < 250:
    i += 1
    mouse.press('left')
    sleep(0.1)
    mouse.release('left')

    print(i)
    sleep(10)
    keyboard.press('w')
    sleep(1)
    keyboard.release('w')
    keyboard.press('s')
    sleep(2)
    keyboard.release('s')

    sleep(300)


else:
    print("Stopped")
    keyboard.press_and_release('esc')
    mouse.move(1804, 14, absolute=True, duration=0.2)
    sleep(0.1)
    mouse.click('left')

#-200 1400



