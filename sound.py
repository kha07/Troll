'''
The frequency of the beep must be in the range 37 through 32767 hertz
'''
import time
import winsound
import keyboard


def Beep(freq, dur):
    winsound.Beep(freq,dur)

def AskDuration():
    
    FREQUENCY = input("F: ")
    TIME = input("Time(MilliSecond): ")
    
    
    print("Infinite or Single (I/S)")
    userIn = input(": ")
    try:
        if userIn.lower() == "i":
            while True:
                print()
        elif userIn.lower() == 's':
            Beep(freq=int(FREQUENCY),dur=int(TIME))
    except ValueError:
        print("frequency must be in 37 through 32767")


AskDuration()