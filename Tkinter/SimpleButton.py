import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

# Creating a button widget
button = ttk.Button(text='Click Me!')
button.grid(row=1, column=1, ipady=100, ipadx=100)

button.pack()
window.mainloop()
