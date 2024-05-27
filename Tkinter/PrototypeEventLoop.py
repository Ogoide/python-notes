"""
.bind() is used to bind (aha) an event handler to the mainloop, thus allowing them to be usable
"""

import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    # Print characters associated with keypress event
    print(event.char)

# Bind keypress event to hadle_keypress
window.bind('<Key>', handle_keypress)

window.mainloop()