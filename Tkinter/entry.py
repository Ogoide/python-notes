import tkinter as tk

window = tk.Tk()
message = tk.Label(text='Enter text:')
# Entry crreates a single-line textbox
entry = tk.Entry()
message.pack()
entry.pack()

# entry.get() retrieves text, entry.insert() inserts text into the window and text.delete() removes text from window

window.mainloop()
