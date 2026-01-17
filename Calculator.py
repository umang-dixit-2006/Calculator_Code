from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.geometry('500x500')

#entry
e = ttk.Entry(window, width=34)
e.pack()
e.place(x=10, y=0)

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result)+str(num))
    
def clear():
    e.delete(0, END)
    
#Number Buttons
b = ttk.Button(window, text= '1', width=10, command=lambda:click(1))
b.place(x=10, y= 25)

b = ttk.Button(window, text= '2', width=10, command=lambda:click(2))
b.place(x=80, y= 25)

b = ttk.Button(window, text= '3', width=10, command=lambda:click(3))
b.place(x=150, y= 25)

b = ttk.Button(window, text= '4', width=10, command=lambda:click(4))
b.place(x=10, y= 50)

b = ttk.Button(window, text= '5', width=10, command=lambda:click(5))
b.place(x=80, y= 50)

b = ttk.Button(window, text= '6', width=10, command=lambda:click(6))
b.place(x=150, y= 50)

b = ttk.Button(window, text= '7', width=10, command=lambda:click(7))
b.place(x=10, y= 75)

b = ttk.Button(window, text= '8', width=10, command=lambda:click(8))
b.place(x=80, y= 75)

b = ttk.Button(window, text= '9', width=10, command=lambda:click(9))
b.place(x=150, y= 75)

b = ttk.Button(window, text= '0', width=10, command=lambda:click(0))
b.place(x=80, y= 100)

#Operations
def add():
    n1 = e.get()
    global i
    i = int(n1)
    global math
    math = 'addition'
    e.delete(0, END)
    pass

def sub():
    n1 = e.get()
    global i
    i = int(n1)
    global math
    math = 'subtraction'
    e.delete(0, END)
    pass

def div():
    n1 = e.get()
    global i
    i = int(n1)
    global math
    math = 'division'
    e.delete(0, END)
    pass

def mul():
    n1 = e.get()
    global i
    i = int(n1)
    global math
    math = 'multiplication'
    e.delete(0, END)
    pass

def mod():
    n1 = e.get()
    global i
    i = int(n1)
    global math
    math = 'modulus'
    e.delete(0, END)
    pass

def equals():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i+int(n2))
    elif math == 'subtraction':
        e.insert(0, i - int(n2))
    elif math == 'division':
        e.insert(0, i / int(n2))
    elif math == 'multiplication':
        e.insert(0, i*int(n2))
    elif math == 'modulus':
        e.insert(0, i%int(n2))
    pass

def delete():
    e.delete(1)

#Operator buttons
b = ttk.Button(window, text= '+', width=10, command=add)
b.place(x=10, y= 100)

b = ttk.Button(window, text= '-', width=10, command=sub)
b.place(x=150, y= 100)

b = ttk.Button(window, text= '/', width=10, command=div)
b.place(x=10, y= 125)

b = ttk.Button(window, text= '×', width=10, command=mul)
b.place(x=80, y= 125)

b = ttk.Button(window, text= '%', width=10, command=mod)
b.place(x=150, y= 125)

b = ttk.Button(window, text= 'del', width=10, command=delete)
b.place(x=10, y= 150)

b = ttk.Button(window, text= 'clear', width=10, command=clear)
b.place(x=80, y= 150)

b = ttk.Button(window, text= '=', width=10, command=equals)
b.place(x=150, y= 150)

window.mainloop()
