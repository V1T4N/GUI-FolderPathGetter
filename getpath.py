# -*- coding: utf-8 -*-
import os, tkinter, tkinter.filedialog, tkinter.messagebox

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('SleepSign automater','Select save folder')

dir = tkinter.filedialog.askdirectory(initialdir = iDir)

print(dir)

path_w = 'path.txt'


with open(path_w, mode='w') as f:
    f.write(dir)
