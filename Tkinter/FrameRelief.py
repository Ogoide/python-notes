import tkinter as tk

border_effects = {
    # Different borders for frames
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

# Creates one widget per relief option (border type), displaying said relief's name
for relief_name, relief in border_effects.items():
    # As default borderwidth is 0, for relief effects to be seen, it is needed to up that value
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()