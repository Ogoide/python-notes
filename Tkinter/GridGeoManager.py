"""
from RealPython: 
".grid() works by splitting a window or Frame into rows and columns. You specify the location of 
a widget by calling .grid() and passing the row and column indices to the row and column keyword arguments, 
respectively. Both row and column indices start at 0, so a row index of 1 and a column index of 2 tells .grid() to 
place a widget in the third column of the second row."
"""

import tkinter as tk

window = tk.Tk()

for r in range(11):
    for c in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )

        frame.grid(row=r, column=c)
        label = tk.Label(master=frame, text=f'Row {r}\nColumn {c}')
        label.pack()

window.mainloop()