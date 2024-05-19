"""
pack() supports additional arguments:
    tk.X - fill the horizontal direction
    tk.Y - fill the vertical direction
    tk.BOTH - fill both directions
    filing the window this way makes the width argument unnecessary and is responsive to window resizing
"""

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()