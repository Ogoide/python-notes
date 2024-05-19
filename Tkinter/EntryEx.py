import tkinter as tk

window = tk.Tk()

ent_name = tk.Entry()
ent_name.insert(0, 'What is your name?')
ent_name.pack()
window.mainloop()