import pyautogui
import keyboard
from time import sleep
from random import randint
import sys

def check_screen_size():
    return pyautogui.size()

def start():
    screen_width, screen_height = check_screen_size()
    running = True
    paused = False

    while running:
        if keyboard.is_pressed('w') and not paused:  
            print("Paused. Press 'w' again to resume.")
            while keyboard.is_pressed('w'): 
                sleep(0.1)
            sleep(5)  # Pause for 5 seconds
            print("Resuming...")
            paused = False
        
        if keyboard.is_pressed('z'): 
            print("Exiting. Random number:", randint(1, 30000))
            sys.exit()

        if not paused:
            x = randint(1, screen_width)    
            y = randint(1, screen_height)
            pyautogui.moveTo(x=x, y=y)
            sleep(0.5) 

start()
