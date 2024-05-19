import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
label_a = tk.Label(text='I\'m in frame A.', master=frame_a)
label_b = tk.Label(text='I\'m in frame B.', master=frame_b)
# The order the frames are packed is the order the widgets will appear by default.
frame_a.pack()
frame_b.pack()
# Since labels are assigned to frames, they will be moved with their master
label_a.pack()
label_b.pack()
window.mainloop()
