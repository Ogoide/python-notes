import tkinter as tk

window = tk.Tk()
frame = tk.Frame()
label = tk.Label(master=frame, text='Text')
frame.pack(); label.pack()

window.mainloop()