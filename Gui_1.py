import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
win.resizable(0,0)
ttk.Label(win,text = "Our first Label!").grid(column = 0, row = 0)
win.mainloop()
