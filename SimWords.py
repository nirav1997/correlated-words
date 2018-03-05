# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:09:34 2017

@author: Nirav

"""

import sys
import pandas as pd

from sort import Sort
sort = Sort()
try:
    from Tkinter import *
    import tkinter
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import SimWords_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    SimWords_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = root
    
    SimWords_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None



class New_Toplevel_1:
    
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Yu Gothic UI Semibold} -size 14 -weight "  \
            "bold -slant roman -underline 0 -overstrike 0"

        top.geometry("600x479+383+78")
        top.title("Similiar Words")
        top.configure(background="#000000")


        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.26, relwidth=0.96)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#1b1612")
        self.Frame1.configure(width=575)
        
        self.Button1 = Button(self.Frame1,command=self.printsimwords)
        self.Button1.place(relx=0.6, rely=0.32, height=42, width=220)
        self.Button1.configure(activebackground="#c2efd9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0f0020")
        self.Button1.configure(disabledforeground="#ff4699")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search Correlated Words''')
        
        self.searchWord = StringVar()
        self.Entry1 = Entry(self.Frame1,textvariable=self.searchWord)
        self.Entry1.place(relx=0.02, rely=0.32, relheight=0.32, relwidth=0.56)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=324)

        self.simWords = StringVar()
        #self.simWords.set('Similiar Words\n')
        self.label = Label(top, textvariable= self.simWords)
        self.label.configure(background="#5c5c5c")
        self.label.configure(foreground="#000000")
        self.label.configure(font=font10)
        self.label.place(relx=0.02, rely=0.31, relheight=0.64, relwidth=0.96)
        

    def printsimwords(self):
        #print(self.searchWord.get())
        index = self.searchWord.get()
        l='hello'
        self.simWords.set(l)
        l = sort.maxWay("correlated.csv",index)
        self.simWords.set(l) 




if __name__ == '__main__':
    vp_start_gui()



