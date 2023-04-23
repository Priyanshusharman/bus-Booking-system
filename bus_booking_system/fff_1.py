from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')

home=PhotoImage(file='.\\home.png')
f2=Frame(root).grid(row=0)
e1=Label(f2,image=bus)
e1.grid(row=0,padx=w//3,pady=15,columnspan=200)

e2=Label(f2,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE)
e2.grid(row=1,padx=w//3,pady=15,columnspan=200)

e3=Label(f2,text='Add Bus Operator Details',bg='white',fg='green2',font='Arial 20 bold',borderwidth=2,relief=GROOVE)
e3.grid(row=2,padx=w//3,pady=15,columnspan=200)

Operator=Entry(f2)
Operator.grid(row=3,column=76)

e5=Label(f2,text='Operator Id',font='Arial 14')
e5.grid(row=3,column=75)

Name=Entry(f2)
Name.grid(row=3,column=78)

e7=Label(f2,text='Name',font='Arial 14')
e7.grid(row=3,column=77)

Address=Entry(f2)
Address.grid(row=3,column=80)

e9=Label(f2,text='Address',font='Arial 14')
e9.grid(row=3,column=79)

Phone=Entry(f2)
Phone.grid(row=3,column=82)

e11=Label(f2,text='Phone',font='Arial 14')
e11.grid(row=3,column=81)

Email=Entry(f2)
Email.grid(row=3,column=84)

e13=Label(f2,text='Email',font='Arial 14')
e13.grid(row=3,column=83)
def add():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("insert into operator values("+Operator.get()+",'"+Name.get()+"','"+Address.get()+"','"+Email.get()+"',"+Phone.get()+")")
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
    cur.execute("select * from operator where opeId="+Operator.get()+"")
    result=cur.fetchall()
    ft=Frame(root).grid(row=4)
    Label(ft,text="operator Id : "+str(result[0][0])+"  name ="+result[0][1]+"  Address ="+str(result[0][2])+"  Email ="+str(result[0][3])+" phone no ="+str(result[0][4])).grid(row=4)

def edit():
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("delete from operator where opeId="+Operator.get()+"")
        con.commit()
        cur.execute("insert into operator values("+Operator.get()+",'"+Name.get()+"','"+Address.get()+"','"+Email.get()+"',"+Phone.get()+")")
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
        ms.showinfo("reparted value","Entery already exit")
        a=-1
    if(a==0):
        con.commit()
        import tkinter.messagebox as ms
        ms.showinfo("Successful","Editing done")    
    cur.execute("select * from operator where opeId="+Operator.get()+"")
    result=cur.fetchall()
    ft=Frame(root).grid(row=4,column=75)
    Label(ft,text="operator Id : "+str(result[0][0])+"  name ="+result[0][1]+"  Address ="+str(result[0][2])+"  Email ="+str(result[0][3])+" phone no ="+str(result[0][4])).grid(row=4,column=75)
    import tkinter.messagebox as ms
    ms.showinfo("Successful","Editing done")
e14=Button(f2,text='Add',font='Arial 14',bg='green2',command=add)
e14.grid(row=3,column=99)

e15=Button(f2,text='Edit',font='Arial 14',bg='green2',command=edit)
e15.grid(row=3,column=109)
def Home():
    root.destroy()
    import f2
e16=Button(root,image=home,bg='green2',command=Home)
e16.grid(row=6,column=84,pady=100)

root.mainloop()
