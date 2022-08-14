wid#import tkinter 
from tkinter import *  #import all functions

'''
def onclick():
	l=Label(root, text='welcome to nightvale')
	l.grid(row=20, column=20)

root=Tk()
root.geometry('1000x1000')
lab=Label(root, text='BOTTOM TEXT')
lab.grid(row=0, column=0)

root.mainloop()
bu=Button(root, text='helllllll', command=onclick, bg='black', fg='purple')
bu.grid(row=1,column=10)
'''
root=Tk()
root.geometry('1000x1000')

lb=Label(root, text='enter text')
lb.pack()
e=Entry(root, width=20, bg='blue', fg='white')
e.pack()
e.insert(14, 'enter your name')
def click():	message='hello ' + e.get() #for text entered in entry
	lb2=Label(root, text=message)
	lb2.pack()

butt=Button(root, text='click', command=click, bg='red', fg='white')
butt.pack()

root.mainloop()
