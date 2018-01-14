
import tkinter as tk

from tkinter import simpledialog

application_window = tk.Tk()

answer = simpledialog.askstring('input', 'what is your first name?', parent= application_window)

if answer is not None:
    print('Your first name is ', answer)
else:
    print('you dont have a first name')

answer = simpledialog.askinteger('input', 'what is your age?', parent = application_window, minvalue=0, maxvalue=100)

if answer is not None:
    print('Your age is ', answer)
else:
    print('you dont have an age?')

answer = simpledialog.askfloat('input', 'what is your salary?', parent=application_window, minvalue=0.0, maxvalue=1000000)

if answer is not None:
    print ("Your salary is ", answer)
else:
    print("You don't have a salary?")


