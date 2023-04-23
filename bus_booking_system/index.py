from tkinter import *
import tkinter.messagebox as ma
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
#ma.showinfo("hello")
f1=Frame(root).pack()
bus=PhotoImage(file='.\\Bus_for_project.png')
h1=Label(f1,image=bus)
h1.pack(pady=35)
h2=Label(f1,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 28 bold',borderwidth=3,relief=GROOVE)
h2.pack(pady=30)
h3=Label(f1,text='Name : Priyanshu',fg='blue',font='Arial 14 bold')
h3.pack(pady=15)
h4=Label(f1,text='er: abcd',fg='blue',font='Arial 14 bold')
h4.pack(pady=15)
h5=Label(f1,text='Mobile : mobile',fg='blue',font='Arial 14 bold')
h5.pack(pady=15)
h6=Label(f1,text='Submitted to : ',bg='lightblue',fg='red',font='Arial 25 bold',borderwidth=2,relief=GROOVE)
h6.pack()
h7=Label(f1,text='Project Based Learning',fg='red',font='Arial 12 bold')
h7.pack()

def closer():
    root.destroy()
    
    import f2


root.after(1000,closer)
    
root.mainloop()

