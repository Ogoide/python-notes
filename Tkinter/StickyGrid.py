"""
By default, widgets are centered in their grid
The sticky parameter can pin widgets to top ('n'), left ('w'), bottom ('s') our right ('e'), as in the cardinal points
These can also be combined
"""

import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky='se')

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky='n')

window.mainloop()
