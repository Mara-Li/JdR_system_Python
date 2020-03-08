from tkinter import *

def someotherfunction(e=None):
    print('It works !')

root = Tk()
root.bind('<Control-n>', someotherfunction)
root.mainloop()