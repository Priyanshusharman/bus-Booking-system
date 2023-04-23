from tkinter import *
import tkinter.messagebox as message
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
selectType=StringVar()
selectType.set("Select Bus")
bus=PhotoImage(file='.\\Bus_for_project.png')
home=PhotoImage(file='.\\home.png')


Label(root,image=bus).grid(padx=(w//3),columnspan=200)
Label(root,text="Online Bus Booking System",bg="lightblue",fg="red",font='Arial 28 bold',borderwidth=2,relief=GROOVE).grid(padx=(w//3),columnspan=200)
Label(root,text="Add Bus Delails",fg="green",font="Arial 20 bold",borderwidth=2,relief=GROOVE).grid(padx=(w//3),pady=15,columnspan=200)
Label(root,text="Bus ID",font="Arial 14 bold").grid(padx=10,row=3,column=24)

BusID=Entry(root)
BusID.grid(row=3,column=26)
Label(root,text="Bus Type",font="Arial 14 bold").grid(row=3,column=28)
option=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2X1","Non-AC Sleeper 2X1"]
menu=OptionMenu(root,selectType,*option)
menu.grid(row=3,column=30)


Label(root,text="Capacity",font="Arial 14 bold").grid(row=3,column=32)
Capacity=Entry(root)
Capacity.grid(row=3,column=34)
Label(root,text="Fare Rs",font="Arial 14 bold").grid(row=3,column=35)
FareRs=Entry(root)
FareRs.grid(row=3,column=36)
Label(root,text="Operator ID",font="Arial 14 bold").grid(row=3,column=38)
OperatorID=Entry(root)
OperatorID.grid(row=3,column=40)
Label(root,text="Route ID",font="Arial 14 bold").grid(row=3,column=42)
RouteID=Entry(root)
RouteID.grid(row=3,column=44)

def addbus():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("insert into Bus values("+BusID.get()+",'"+selectType.get()+"',"+Capacity.get()+","+OperatorID.get()+","+RouteID.get()+","+FareRs.get()+")")
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
        ms.showinfo("Successful","Add a Bus")
    #cur.execute("select * from Bus where busId="+BusID.get()+"")
    #result=cur.fetchall()
def editbus():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("delete from bus where routeId="+BusID.get()+"")
        cur.execute("insert into Bus values("+BusID.get()+",'"+selectType.get()+"',"+Capacity.get()+","+OperatorID.get()+","+RouteID.get()+","+FareRs.get()+")")
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
        ms.showinfo("Successful","Edited")
    #cur.execute("select * from bus where routeId="+BusID.get()+"")
    #result=cur.fetchall()

Button(root,text="Add Bus",bg="lightgreen",font="Arial 14 bold",command=addbus).grid(pady=25,row=4,column=34)
Button(root,text="Edit Bus",bg="lightgreen",font="Arial 14 bold",command=editbus).grid(pady=25,row=4,column=35)
def Home():
    root.destroy()
    import f2
Button(root,image=home,command=Home).grid(pady=25,row=4,column=37)

 
root.mainloop()
