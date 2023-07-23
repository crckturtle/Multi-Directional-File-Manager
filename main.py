import os
from tkinter import *
from tkinter import ttk

root = Tk()

win = ttk.Frame(root, padding=10)
win.grid()

cleandir = r"shortcuts\cleandir.lnk"
moddir = r"shortcuts\moddir.lnk"

ttk.Label(win, text="What profile would you like to run?").grid(column=0, row=0)
ttk.Button(win, text="Modded", command=lambda: os.startfile(moddir)).grid(column=0, row=1)
ttk.Button(win, text="Clean", command=lambda: os.startfile(cleandir)).grid(column=0, row=2)

root.mainloop()