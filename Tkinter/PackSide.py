"""
By default, pack() places widgets from top to bottom, but it takes a side argument
This argument indicates the side of the window that widgets must place on:
    tk.TOP (default)
    tk.BOTTOM
    tk.LEFT
    tk.RIGHT
"""

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()