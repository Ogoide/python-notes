import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

# Create label widget
message = ttk.Label(
    # Display text message
    text='Tkinter rocks!',
    # Change text color
    foreground='white',
    # Change widget background color
    background='dark blue',
    # Controlling height and width
    # Padding adds space to insides of the widget
    padding=50
    )

message.pack()
window.mainloop()
