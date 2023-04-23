from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def close():
    root.destroy()
def booking():
    close()
    import f3
def check():
     close()
     import ff2
def add_bus():
    close()
    import fff3

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(padx=w//3,pady=30,columnspan=20)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 28 bold',borderwidth=3,relief=GROOVE).grid(padx=w//3,pady=30,columnspan=20)

Button(root,text='Seat Booking',bg='lightgreen',font='Arial 14 bold',borderwidth=3,relief=GROOVE,command=booking).grid(row=3,column=6,)

Button(root,text='Check Booked Seat',bg='green',font='Arial 14 bold',borderwidth=3,relief=GROOVE,command=check).grid(row=3,column=9)

Button(root,text='Add bus',bg='green',font='Arial 14 bold',borderwidth=3,relief=GROOVE,command=add_bus).grid(row=3,column=12)

Label(root,text='For Admin Only',fg='red',font='Arial 8 bold').grid(row=4,column=12)


root.mainloop()
