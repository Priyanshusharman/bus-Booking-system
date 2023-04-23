from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')

home=PhotoImage(file='.\\home.png')

s1=Label(root,image=bus).grid(padx=w//3,pady=15,columnspan=200)

s2=Label(root,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE).grid(padx=w//3,pady=15,columnspan=200)

s3=Label(root,text='Add Bus Route Details',bg='white',fg='green2',font='Arial 20 bold',borderwidth=2,relief=GROOVE).grid(padx=w//3,pady=15,columnspan=200)

route=Entry(root)
route.grid(row=3,column=56)

s4=Label(root,text='Route ID',font='Arial 14').grid(row=3,column=55)

station=Entry(root)
station.grid(row=3,column=58)

s5=Label(root,text='Station Name',font='Arial 14').grid(row=3,column=57,pady=30)

std=Entry(root)
std.grid(row=3,column=60)

s6=Label(root,text='Station ID',font='Arial 14').grid(row=3,column=59)

def addroute():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("insert into route values("+route.get()+","+std.get()+",'"+station.get()+"')")
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
    cur.execute("select * from route where RouteId="+route.get()+" and std="+std.get()+"")
    result=cur.fetchall()
    ft=Frame(root).grid(row=4)
    Label(ft,text="Route Id : "+str(result[0][0])+"station name ="+result[0][2]+"Staion ID ="+str(result[0][1])).grid(row=4)
def routedelete():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("delete from route where RouteId="+route.get()+" and std="+std.get()+"")
    except sqlite3.OperationalError:
        import tkinter.messagebox as ms
        ms.showinfo("Invalid","Please enter correct value")
        a=-1
    if(a==0):
        con.commit()
    ft=Frame(root).grid(row=4)
    Label(ft,text="Delete Route: "+str(route.get())+"station name ="+station.get()+"Staion ID ="+str(std.get())).grid(row=4)

s7=Button(root,text='Add Route',font='Arial 14',bg='green2',command=addroute).grid(row=3,column=63)

s8=Button(root,text='Delete Route',font='Arial 14',bg='green2',fg='red',command=routedelete).grid(row=3,column=70)
def Home():
    root.destroy()
    import f2
Button(root,image=home,bg='green2',command=Home).grid(row=9,column=61,pady=55)

root.mainloop()
