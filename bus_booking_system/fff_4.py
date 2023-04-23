from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')

home=PhotoImage(file='.\\home.png')

Label(root,image=bus).grid(padx=w//3,pady=15,columnspan=200)
Label(root,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE).grid(padx=w//3,pady=15,columnspan=200)

Label(root,text='Add Bus Running Details',bg='white',fg='green2',font='Arial 20 bold',borderwidth=2,relief=GROOVE).grid(padx=w//3,columnspan=200)

Bus=Entry(root)
Bus.grid(row=3,column=56)

Label(root,text='Bus ID',font='Arial 14').grid(row=3,column=55)

date=Entry(root)
date.grid(row=3,column=58)

Label(root,text='Running Date',font='Arial 14').grid(row=3,column=57,pady=30)

seat=Entry(root)
seat.grid(row=3,column=60)

Label(root,text='Seat Available',font='Arial 14').grid(row=3,column=59)
def add():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("insert into run values("+Bus.get()+",'"+date.get()+"',"+seat.get()+")")
    except sqlite3.OperationalError:
        import tkinter.messagebox as ms
        ms.showinfo("Invalid","Please enter correct value")
        a=-1
    except NameError:
        import tkinter.messagebox as ms
        ms.showinfo("reparted value","Entery already exit")
        a=-1
    except sqlite3.IntegrityError:
        import tkinter.messagebox as ms
        ms.showinfo("reparted value","Entery already exit")
        a=-1
    if(a==0):
        con.commit()
        import tkinter.messagebox as ms
        ms.showinfo("Successful","Added")
    cur.execute("select * from operator where busId="+Bus.get()+"")
    result=cur.fetchall()
def delete():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("delete from run where routeId="+Bus.get()+"")

    except sqlite3.OperationalError:
        import tkinter.messagebox as ms
        ms.showinfo("Invalid","Please enter correct value")
        a=-1
    except NameError:
        import tkinter.messagebox as ms
        ms.showinfo("unidentify","Error")
        a=-1
    except sqlite3.IntegrityError:
        import tkinter.messagebox as ms
        ms.showinfo("reparted value","Entery don't exit")
        a=-1
    if(a==0):
        con.commit()
        import tkinter.messagebox as ms
        ms.showinfo("Successful","Deleted")
    cur.execute("select * from operator where opeId="+Operator.get()+"")
    result=cur.fetchall()
    ft=Frame(root).grid(row=4,column=75)
    Label(ft,text="operator Id : "+str(result[0][0])+"  name ="+result[0][1]+"  Address ="+str(result[0][2])+"  Email ="+str(result[0][3])+" phone no ="+str(result[0][4])).grid(row=4,column=75)

Button(root,text='Add Bus',font='Arial 14',bg='green2',command=add).grid(row=3,column=61)

Button(root,text='Delete Bus',font='Arial 14',bg='green2',command=delete).grid(row=3,column=62)
def Home():
    root.destroy()
    import f2 

Button(root,image=home,bg='green2',command=Home).grid(row=9,column=61,pady=20)




root.mainloop()
