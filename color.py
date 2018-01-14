import tkinter as tk
from tkinter import colorchooser

application_window = tk.Tk()

rgb_color, web_color = colorchooser.askcolor(parent=application_window, initialcolor=(255, 0, 0))



