from tkinter import *
import sys
import os

if os.environ.get('DISPAY','') == '':
    print("no display found. Using: 0.0")
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Tk()

window.title("Hello World")

lbl = Label(window, text="Type something in text box ->")
lbl.grid(column=0, row=0)

window.geometry('1400x800') #works great for 7" touch screen

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

toggle = False

def clicked():
    global toggle
    if  toggle == False:
        lbl.configure(text=txt.get())
        toggle = True
    else: 
        lbl.configure(text="")
        toggle = False

btn = Button(window, text="click me" , command=clicked)
btn.grid(column=2, row=0)


window.mainloop()

