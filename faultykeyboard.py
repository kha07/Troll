import time
import keyboard
import random

listABCS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def typoSim():
    def on_key(event):
        if random.randint(1, 10) > 8:  # 20% chance of happening
            keyboard.write(random.choice(listABCS))
            return False  # Block the original key event

    keyboard.hook(on_key)
    print("CTRL + C TO STOP")

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("Stopped typo simulator.")

if __name__ == "__main__":
    typoSim()



