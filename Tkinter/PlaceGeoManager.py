'''
The place geometry manager is used to precisely specify the widgets' placement on the window.
It takes x and y coordinates as arguments, measured in pixels from the top-left corner.
'''

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=150, height=150)
frame1.pack(fill=tk.BOTH, expand=True)
label1 = tk.Label(master=frame1, text='I\'m at (0,0)', bg='cyan')
label1.place(x=0, y=0)
label2 = tk.Label(master=frame1, background='blue', foreground='white', text='I\' at (75,75)')
label2.place(x=75, y=75)

window.mainloop()