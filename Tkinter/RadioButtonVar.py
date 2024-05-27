import tkinter as tk
from tkinter import ttk

def on_radio_select():
    selected_var = radio_var.get()
    print(selected_var)

window = tk.Tk()
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

radio_var =tk.StringVar()
options = ['Celsius to Farenheit', 'Farenheit to Celsius']
for i, option in enumerate(options):
    rb = ttk.Radiobutton(master=window, text=option, value=option, variable=radio_var, command=on_radio_select)
    rb.grid(row=i, column=0, sticky='nsew')

window.mainloop()