import tkinter as tk
from tkinter import ttk

class Manager:
    def __init__(self):
        self.error = False
        self.error_message = ''
        self.convert_option = ''
        self.output_value = ''
        self.error_window = None

    def get_radio_option(self):
        self.convert_option = option_var.get()
        if self.convert_option == "Farenheit to Celsius":
            lbl_tempinfo['text'] = 'ºF'
        elif self.convert_option == "Celsius to Farenheit":
            lbl_tempinfo['text'] = 'ºC'



    def conversion(self):
        input_value = ent_input.get()
        self.error = False
        self.error_message = ''

        if not self.error:
            if self.convert_option == "Farenheit to Celsius":
                try:
                    temp = float(input_value)
                    c = (5 / 9) * (temp - 32)
                    self.output_value = f'{c:.2f}ºC'
                except:
                    self.error = True
            elif self.convert_option == "Celsius to Farenheit":
                try:
                    temp = float(input_value)
                    f = ((9 / 5) * temp) + 32
                    self.output_value = f'{f:.2f}ºF'
                except:
                    self.error = True
            else:
                self.error = True
                self.error_message = 'Please select the conversion mode!'

        if self.error:
            if not input_value.isnumeric() and self.error_message == '':
                self.error_message = 'Insert a numerical value and only a numerical value to convert.'

            self.error_window = tk.Tk()
            error_window = self.error_window
            error_window.title('ERROR')
            error_window.resizable(False, False)
            error_window.rowconfigure([0, 1], minsize=20)
            error_window.columnconfigure(0, minsize=50)

            lbl_errordisplay = ttk.Label(master=error_window, text=m.error_message, padding=5)
            lbl_errordisplay.grid(row=0, column=0, sticky='nsew')

            btn_close = ttk.Button(master=error_window, text='Close', command=self.quit, padding=1)
            btn_close.grid(row=1, column=0)

            error_window.mainloop()

        lbl_output['text'] = self.output_value

    def quit(self):
        self.error_window.destroy()


m = Manager()

main = tk.Tk()
main.title('F/C Converter')
main.resizable(False, False)

frm_main = ttk.Frame(master=main)
frm_main.rowconfigure(0, minsize=10)
frm_main.columnconfigure([0, 1, 2, 3], minsize=20)

ent_input = ttk.Entry(master=frm_main)
ent_input.grid(row=0, column=0, padx=5)

lbl_tempinfo = ttk.Label(master=frm_main, text='N/A', width=5)
lbl_tempinfo.grid(row=0, column=1, sticky='w')

btn_convert = ttk.Button(master=frm_main, text='-->', width=5, command=m.conversion)
btn_convert.grid(row=0, column=2)

lbl_output = ttk.Label(master=frm_main, text='', borderwidth=1, relief=tk.SUNKEN, width=10, padding=2)
lbl_output.grid(row=0, column=3)

frm_options = ttk.Frame(master=main)
frm_options.rowconfigure(0, minsize=10, weight=1)
frm_options.columnconfigure([0, 1], minsize=50, weight=1)

option_var = tk.StringVar()
options = ['Celsius to Farenheit', 'Farenheit to Celsius']
for i, option in enumerate(options):
    rbt_option = ttk.Radiobutton(master=frm_options, text=option, value=option, variable=option_var, command=m.get_radio_option)
    rbt_option.grid(row=0, column=i, sticky='nsew')


frm_main.pack()
frm_options.pack()

main.mainloop()