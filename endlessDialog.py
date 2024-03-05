#Endless Dialog (Literally)


import tkinter as tk
from tkinter import messagebox




def InfiniteLoops():
    while True:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("ERROR")






InfiniteLoops()