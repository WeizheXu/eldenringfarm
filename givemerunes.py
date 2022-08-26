#import pyautogui
import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
import time
import numpy as np

def smoothMove(mouse, x, y, duration, interval=0.01):
    
    action = np.arange(0, duration, interval)
    toMoveX = x/len(action)
    toMoveY = y/len(action)

    for i in action:
        mouse.move(toMoveX, toMoveY)
        time.sleep(interval)

def initialPath(keyboard):
    # with keyboard.pressed('w'):
    #     time.sleep(3.0)
    # with keyboard.pressed('a'):
    #     time.sleep(0.8)
    # with keyboard.pressed('w'):
    #     time.sleep(1.9)

    keyPress(keyboard, 'w', sleepTime=3.0)
    keyPress(keyboard, 'a', sleepTime=0.8)
    keyPress(keyboard, 'w', sleepTime=1.9)

def teleportBack(keyboard):
    keyPress(keyboard, 'g')
    keyPress(keyboard, 's', sleepTime=0.05)
    waitTime = 1.2
    time.sleep(waitTime/2)
    keyPress(keyboard, 'e')
    time.sleep(waitTime/2)
    keyPress(keyboard, 'e')
    
def useSkill(mouse):
    keyPress(mouse, Button.middle)

def keyPress(controller, key, sleepTime=1.0):
    global active, endProgram
    if active and not endProgram:
        controller.press(key)
        time.sleep(sleepTime)
        controller.release(key)

def runeHarvest(mouse, keyboard):
    time.sleep(5)
    initialPath(keyboard)
    useSkill(mouse)
    time.sleep(1)
    teleportBack(keyboard)

def on_press(key):
    pass

def on_release(key):
    global active, endProgram
    if key == Key.delete:
        active = not active
    if key == Key.f9:
        endProgram = True       
def main():
    keyboard = Controller()
    mouse = MouseController()
    global active, endProgram 
    active = False
    endProgram = False

    listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

    listener.start()
    while True:
        if endProgram:
            break
        if active:
            runeHarvest(mouse, keyboard)
        time.sleep(1)

    # for i in [0,1,2,3]:
    #     runeHarvest(mouse, keyboard)

if __name__ == "__main__":
    main()