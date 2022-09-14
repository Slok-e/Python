from tkinter import *

#Create a Window
win = Tk()
win.title('practice_Tk')
win.geometry('350x350')
win.configure(background='black')

#Create a label 1 and add to window
win = Label(win, text='Hello, welcome to my practice python GUI!',
       bg='black', fg='white', font='timesnewroman 12')
win.pack()


#Create Frame widget
from tkinter import *


root = Tk()
root.geometry('350x350')
frame1 = Frame(root, highlightbackground='green', highlightcolor='green',
               highlightthickness=1, width=200, height=75, bd=2)
frame1.pack()
frame1.pack_propagate(False)
Entry(frame1).pack()




