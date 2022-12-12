import pyautogui as gui
import time
from numpy import random

#Removing Fail safe options
gui.FAILSAFE = False

while True:
    time.sleep(1)
    x1,y1 = gui.position() #initial position
    time.sleep(1)
    x2, y2 = gui.position() #final position
    x = random.randint(1000)
    y = random.randint(1000)

    # print(f'{x} & {y}')

    #if position remains the same in a given time
    #it will automatically move the mouse to a random position
    if x2 - x1 == 0 & y2 - y1 == 0:
        gui.moveTo(x,y)

#old automation just simply pressing the key 'numlock'

# while True:
#     time.sleep(100)
#     gui.keyDown('numlock')
#     time.sleep(1)
#     gui.keyUp('numlock')
#
