import tkinter as tk

window = tk.Tk()

message = tk.Label(
    text='Hello Tkinter',
    bg='dark blue',
    fg='cyan',
    height=3,
    width=10)

button = tk.Button(
    text='Click Me!',
    width=10,
    height=2,
    bg='cyan',
    fg='dark blue')

message.pack()
button.pack()
window.mainloop()