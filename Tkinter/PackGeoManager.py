"""
What does pack() do?

    'Compute a rectangular area called a parcel that’s just tall (or wide) enough to hold the widget and fills the
    remaining width (or height) in the window with blank space.
    Center the widget in the parcel unless a different location is specified.'
    Places widgets in the order they're packed, from top to bottom.

"""

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()