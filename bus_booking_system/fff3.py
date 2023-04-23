from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
home=PhotoImage(file='.\\home.png')
def close():
    root.destroy()
def newbus():
    close()
    import fff3_2
def operator():
     close()
     import fff_1
def rought():
    close()
    import fff_3
def run():
    close()
    import fff_4    
Label(root,image=bus).grid(row=0,padx=(w//3),columnspan=20)
Label(root,text="Online Bus Booking System",bg="lightblue",fg="red",font='Arial 28 bold',borderwidth=2,relief=GROOVE).grid(row=1,padx=(w//3),pady=8,columnspan=20)

Label(root,text="Add New Details to DataBase",fg="green",font="Arial 16 bold",borderwidth=2,relief=GROOVE).grid(row=2,padx=(w//3),pady=15,columnspan=20)

new_operator=Button(root,text="New Operator",bg='lightgreen',font='Arial 16 bold',command=operator)

new_bus=Button(root,text="New Bus",bg='orange red',font='Arial 16 bold',command=newbus)

new_rought=Button(root,text="New Route",bg='lightblue',font='Arial 16 bold',command=rought)

new_Run=Button(root,text="New Run",bg='lightpink3',font='Arial 16 bold',command=run)




new_operator.grid(row=4,column=8,pady=10)
new_bus.grid(row=4,column=9,pady=10)
new_rought.grid(row=4,column=10,pady=10)
new_Run.grid(row=4,column=11,pady=10)
def Home():
    root.destroy()
    import f2
Button(root,image=home,command=Home).grid(row=5,column=11,pady=10)
root.mainloop()
