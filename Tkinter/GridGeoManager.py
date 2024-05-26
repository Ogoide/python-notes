"""
from RealPython: 
".grid() works by splitting a window or Frame into rows and columns. You specify the location of 
a widget by calling .grid() and passing the row and column indices to the row and column keyword arguments, 
respectively. Both row and column indices start at 0, so a row index of 1 and a column index of 2 tells .grid() to 
place a widget in the third column of the second row."
"""

import tkinter as tk

window = tk.Tk()

for r in range(5):
    """
    Configuration of rows and columns to add responsive window resizing behaviour:
    
    Index: The index of the grid column or row that you want to configure or a list of indices to configure multiple rows or columns at the same time
    Weight: A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows
    Minimum Size: A keyword argument called minsize that sets the minimum size of the row height or column width in pixels

    """
    window.columnconfigure(index=r, weight=2, minsize=50)
    window.rowconfigure(index=r, weight=2, minsize=50)

    for c in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )

        # Padding adds extra spaces in between widgets
        frame.grid(row=r, column=c, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Row {r}\nColumn {c}')
        label.pack(padx=5, pady=5)

window.mainloop()