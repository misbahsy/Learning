
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

my_label = ttk.Label(window, text = "Hello, World!")
my_label.grid(row=1, column=1)

def process_event(event):
  print("The process_event function was called.")

quit_button = ttk.Button(window, text="Quit")
quit_button.grid(row=2, column=1)
quit_button.bind('<Enter>', process_event)
quit_button['command'] = window.destroy



window.mainloop()



