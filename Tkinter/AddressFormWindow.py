import tkinter as tk

labels = ['First Name:', 'Last Name:', 'Address Line 1:', 'Address Line 2:', 'City:', 'State/Province:', 'Postal Code:', 'Country:']
buttons = ['CLear', 'Submit']

window = tk.Tk()
window.title('Address Form')

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3, padx=5)
frame.columnconfigure([0, 1], minsize=20)
frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=20)

for i in range(8):
    for j in range(2):
        if j == 0:
            label = tk.Label(master=frame, text=labels[i])
            label.grid(row=i, column=j, sticky='e')
        else:
            entry = tk.Entry(master=frame, width=50)
            entry.grid(row=i, column=j)

frame.pack()

# Clear and Submit
frame2 = tk.Frame(master=window)
frame2.columnconfigure([0], minsize=2)
frame2.rowconfigure([0, 1], minsize=2)


for k in range(2):
    button = tk.Button(master=frame2, text=buttons[k], width=10)
    button.grid(row=0, column=k, sticky='e', padx=5)

frame2.pack(side=tk.RIGHT, padx=5, pady=5)

window.mainloop()