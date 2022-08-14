from tkinter import *

def calc(age, rhr, lhr, hhr, gen):
    if gen==1:
        maxhr=206.9-(0.67*age)
        H=maxhr-rhr
        mn=(H*(lhr/100))+rhr
        mx=(H*(hhr/100))+rhr
        message='Pulse rate zone is between' + mn + 'and' + mx
        fl=Label(r, text=message)
        fl.pack()
    elif gen==2:
        maxhr=206.9-(0.88*age)
        H=maxhr-rhr
        mn=(H*(lhr/100))+rhr
        mx=(H*(hhr/100))+rhr
        message='Pulse rate zone is between' + mn + 'and' + mx
        fl2=Label(r, text=message)
        fl2.pack()

r=Tk()
l=Label(r, text='Hello! Enter following details to check your pulse rate:')
l.pack()

ln=Label(r, text='Age')
ln.place(x=540,y=20)
ln2=Label(r, text='Resting heart rate')
ln2.place(x=470,y=35)
ln3=Label(r, text='Low end heart rate')
ln3.place(x=460,y=55)
ln4=Label(r, text='High end heart rate zone')
ln4.place(x=470,y=75)
ln5=Label(r, text='Gender: 1-female; 2-male')
ln5.place(x=420,y=95)


e1=Entry(r)
e2=Entry(r)
e3=Entry(r)
e4=Entry(r)
e5=Entry(r)


e1.pack()
e2.pack()
e3.pack()
e4.pack()
e5.pack()

def getinput():
    age = e1.get()
    rhr = e2.get()
    lhr = e3.get()
    hhr = e4.get()
    gen = e5.get()
    calc(age, rhr, lhr, hhr, gen)

mb=Button(r, text="submit",command = getinput())
mb.pack()

r.mainloop()











