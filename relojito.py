from cProfile import label
from cgitb import text
from distutils.command.config import config
import os, itertools
from tkinter import *
import tkinter
from tkinter.ttk import *
from time import strftime
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )


#   _winapi.WriteFile()

relojito = Tk()

relojito.title('Relojito crv')

relojito.config(width = 1020, height = 720)

txt = tkinter.Label(relojito, text = "JI JI JI JA, Vales verga maldito",
font = ('Arial', 60), background = 'orange', foreground = 'black')
txt.pack()
nv = 50
def joda():
    for _ in itertools.repeat(None, nv): os.system("notepad.exe")

joda()

relojito.mainloop()

