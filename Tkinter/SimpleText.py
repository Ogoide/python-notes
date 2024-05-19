import tkinter as tk

window = tk.Tk()
text = tk.Text()
text.pack()
# entry methods still work, but delete() and insert() methods' arguments need a line argument ('line_start.char_start')
window.mainloop()