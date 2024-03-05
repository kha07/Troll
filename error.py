import random
import tkinter as tk
from tkinter import messagebox
import os
#Fake error Message 
windows_error_messages = [
    "Error: The system ran into a fatal error, Restarting Now...",
    "Error: Access is denied.",
    "Error: The operation completed successfully.",
    "Error: The system cannot find the path specified.",
    "Error: There is not enough space on the disk.",
    "Error: Your PC ran into a problem and needs to restart.",
    "Error: This operation has been cancelled due to restrictions in effect on this computer.",
    "Error: The directory name is invalid.",
    "Error: The filename or extension is too long.",
    "Error: The process cannot access the file because it is being used by another process."
]



def FakeErrorMessage():
    root = tk.Tk()
    root.withdraw()

    test = messagebox.showerror(random.choice(windows_error_messages))


    if test == windows_error_messages[0]: #matches index of first one in list
        print("Restarting PC")
        os.system("shutdown /r /t 1")

FakeErrorMessage()