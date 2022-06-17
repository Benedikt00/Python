import pyautogui
import time

print("""
Welcome to the autoclicker!

This program will click your mouse at a variable speed.

Press Ctrl-C to quit.
""")

#get the number of clicks
clicks = int(input("How many clicks do you want to make? "))

#get the interval between clicks
interval = int(input("How many seconds do you want to wait between clicks? "))

#get the starting position of the mouse
start_x, start_y = pyautogui.position()

#get the starting time
start_time = time.time()

#get the ending time
end_time = start_time + interval * clicks

#loop until the end time
while time.time() < end_time:
    #move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y)
    #click the mouse
    pyautogui.click()
    #wait for the interval
    time.sleep(interval)