#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: simple_clock.py
"""
Example of how a Python programs can use libraries, such as tkinter, to create simple programs.
"""
# Module implementation
# import and retrieve system time
from tkinter import *
from tkinter.ttk import *

from time import strftime

# Display time function on label.
root = Tk()
root.title('Demo_Clock')


def time():
    """
        time function with variable configuration for the time and date, accounted for as a string.
            Vars:
                string: Set to the format of month, day, year, then below, hour, minute, second, and 12-hour time.
            Note:
                The code written after are tkinter modules which can be used to create basic graphics.
    """
    string = strftime('%b %d, %Y \n %H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling of the clock.
lbl = Label(root, font=('times new roman', 40, 'bold'),
            background='red',
            foreground='white')

# Center the clock.
lbl.pack(anchor='center')

# Run the time function.
time()

# Run the main loop from the tkinter library.
mainloop()
