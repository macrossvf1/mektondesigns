from tkinter import *
from tkinter.ttk import *
from time import strftime

# Configure main window.
root = Tk()
root.title("Mekton Builder")
root.geometry('600x400')

# Main menu bar
menubar = Menu(root)

# Adding file menu
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label ='New Mekton', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='About', command = None)
# 
root.config(menu = menubar)
root.mainloop()
