# import all functions from the tkinter
import os
import sys
import tkinter.font as tkfont
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr( sys, '_MEIPASS', os.path.dirname( os.path.abspath( __file__ ) ) )
    return os.path.join( base_path, relative_path )

print(resource_path('data\\pouet'))