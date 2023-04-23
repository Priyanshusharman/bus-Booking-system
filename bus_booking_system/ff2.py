from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
c1=Label(root,image=bus)
c1.grid(padx=(w//3),columnspan=200)
c2=Label(root,text="Online Bus Booking System",bg="lightblue",fg="red",font='Arial 28 bold',borderwidth=2,relief=GROOVE)
c2.grid(padx=(w//3),columnspan=200)
c3=Label(root,text="Check Your Booking",bg="lightgreen",fg="green",font="Arial 20 bold",borderwidth=2,relief=GROOVE)
c3.grid(padx=(w//3),pady=15,columnspan=200)
c4=Label(root,text="Enter Your Mobile No:",font="Arial 15 bold")
c4.grid(row=4,column=95)
mobile=Entry(root)
mobile.grid(row=4,column=96)

def show():
    a=0
    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    try:
        cur.execute("select * from BookingHistory where refno="+mobile.get()+"")
        tik=cur.fetchall()
        name=str(tik[0][1])
    except sqlite3.OperationalError:
        import tkinter.messagebox as ms
        ms.showinfo("Invalid","Enter currect phone number")
    except IndexError :
        a=-1
        import tkinter.messagebox as ms
        check1=ms.askyesnocancel("Ticket do't found","You want to book New Ticket")
        if(check1=='Yes'):
            c1.destroy()
            c2.destroy()
            c3.destroy()
            c4.destroy()
            c6.destroy()
            import ftry
    if(a==0):
        c1.destroy()
        c2.destroy()
        c3.destroy()
        c4.destroy()
        c6.destroy()
        

        f1=Frame(root).grid()
        Label(f1,image=bus).grid(padx=w//3,pady=30,columnspan=20)
        Label(f1,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 28 bold').grid(padx=w//3,pady=30,columnspan=20)
        Label(f1,text='Bus Ticket',font='Arial 18 bold').grid(padx=w//3,columnspan=20)
        
        
        
        name=str(tik[0][1])
        seat=str(tik[0][8])
        refno=str(tik[0][0])
        age=str(tik[0][9])
        ton=str(tik[0][4])
        bon=str(tik[0][5])

        gender=str(tik[0][2])
        phone=str(tik[0][0])
        busdetail="kamal"
        boarder=str(tik[0][6])
        fare=1000
        Rs=str(fare*int(seat))
        f2=Frame(root,borderwidth=2,relief=GROOVE)
        f2.grid(padx=w//3,row=8)
        Label(f2,text='Passengers : '+name,font='Arial 16 bold').grid(row=9,column=0)
        Label(f2,text='No of seats : '+seat,font='Arial 16 bold').grid(row=10,column=0)
        Label(f2,text='Booking Ref : '+refno,font='Arial 16 bold').grid(row=11,column=0)
        Label(f2,text='Travel On : '+ton,font='Arial 16 bold').grid(row=12,column=0)
        Label(f2,text='Age : '+age,font='Arial 16 bold').grid(row=13,column=0)

        Label(f2,text='Gender : '+gender,font='Arial 16 bold').grid(row=9,column=1)
        Label(f2,text='Phone : '+phone,font='Arial 16 bold').grid(row=10,column=1)
        Label(f2,text='Bus Detail : '+busdetail,font='Arial 16 bold').grid(row=11,column=1)
        Label(f2,text='Booked on : '+bon,font='Arial 16 bold').grid(row=12,column=1)
        Label(f2,text='Boarding : '+boarder,font='Arial 16 bold').grid(row=13,column=1)
        Label(f2,text='* Total amount Rs '+Rs+'/- to be paid at time of boarding the Bus',font='Arial 6 bold').grid(row=14,column=0)
c6=Button(root,text="Check Booking",command=show)
c6.grid(row=4,column=97)
root.mainloop()
