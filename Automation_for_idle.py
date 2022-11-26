import pyautogui as gui
import time



while True:
    time.sleep(100)
    gui.keyDown('numlock')
    time.sleep(1)
    gui.keyUp('numlock')

