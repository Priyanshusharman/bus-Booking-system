from tkinter import *
import tkinter.messagebox as ma
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\Bus_for_project.png')

home=PhotoImage(file='.\\home.png')
def tab2():
    root.destroy()

    tab()



    b1=Label(root,image=img)
    b1.grid(padx=w//3,pady=15,row=0,columnspan=200)

    b2=Label(root,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE)
    b2.grid(padx=w//3,pady=15,row=1,columnspan=200)

    b3=Label(root,text='Enter Journey Details',bg='lightgreen',fg='green',font='Arial 18 bold',borderwidth=2,relief=GROOVE)
    b3.grid(padx=w//3,pady=15,row=2,columnspan=200)

    From=Entry(root)
    From.grid(row=3,column=96)

    b4=Label(root,text='From',font='Arial 14 bold')
    b4.grid(row=3,column=95)

    To=Entry(root)
    To.grid(row=3,column=98)

    b5=Label(root,text='To',font='Arial 14 bold')
    b5.grid(row=3,column=97)

    date=Entry(root)
    date.grid(row=3,column=100)

    b5=Label(root,text='Journey date',font='Arial 14 bold')
    b5.grid(row=3,column=99)
            
    b6=Button(root,text='Show Bus',font='Arial 14 bold',bg='green2')
    b6.grid(row=3,column=101)

    b7=Button(root,image=home,command=tab2,bg='green2')
    b7.grid(row=3,column=102)
def tab():


    def tab1():
        root.destroy()
        def tab2():
            root.destroy()
            tab()



        b1=Label(root,image=img)
        b1.grid(padx=w//3,pady=15,row=0,columnspan=200)

        b2=Label(root,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE)
        b2.grid(padx=w//3,pady=15,row=1,columnspan=200)

        b3=Label(root,text='Enter Journey Details',bg='lightgreen',fg='green',font='Arial 18 bold',borderwidth=2,relief=GROOVE)
        b3.grid(padx=w//3,pady=15,row=2,columnspan=200)

        From=Entry(root)
        From.grid(row=3,column=96)

        b4=Label(root,text='From',font='Arial 14 bold')
        b4.grid(row=3,column=95)

        To=Entry(root)
        To.grid(row=3,column=98)

        b5=Label(root,text='To',font='Arial 14 bold')
        b5.grid(row=3,column=97)

        date=Entry(root)
        date.grid(row=3,column=100)

        b5=Label(root,text='Journey date',font='Arial 14 bold')
        b5.grid(row=3,column=99)
            
        b6=Button(root,text='Show Bus',font='Arial 14 bold',bg='green2')
        b6.grid(row=3,column=101)

        b7=Button(root,image=home,command=tab2,bg='green2')
        b7.grid(row=3,column=102)
    def tab3():
        root.destroy()
        def alert():
            import tkinter.messagebox as ma
            alet=ma.askyesnocancel("Ticket not found","you want to book Ticket")
            if(alet == "Yes"):
                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                tab2()
        c1=Label(root,image=img)
        c1.grid(row=0,padx=w//3,pady=15,columnspan=200)

        c2=Label(root,text='Online Bus Booking System',bg='light sky blue',fg='red2',font='Arial 26 bold',borderwidth=2,relief=GROOVE)
        c2.grid(row=1,padx=w//3,pady=15,columnspan=200)

        c3=Label(root,text='Check Your Booking',fg='green',bg='lightgreen',font='Arial 20 bold',borderwidth=2,relief=GROOVE)
        c3.grid(row=2,padx=w//3,pady=15,columnspan=200)

        c4=Mobile=Entry(root)
        c4.grid(row=3,column=96)

        c5=Label(root,text='Enter Your Mobile No:',font='Arial 14 bold')
        c5.grid(row=3,column=95)

        c6=Button(root,text='Check Booking',command=alert,font='Arial 14 bold')
        c6.grid(row=3,column=97)    
  
    a1=Label(root,image=img)
    a1.grid(padx=w//3,pady=10,row=0,columnspan=20)

    a2=Label(root,text = "ONLINE BUS BOOKING SYSTEM",font='arial 28 bold',bg ='light sky blue',fg='red2',borderwidth=2,relief=GROOVE)
    a2.grid(padx=w//3,pady=50,row=1,columnspan=20)    
    a3=Button(root,text ='Seat Booking',command=tab1,font='arial 20 bold',fg='black',bg='green2',borderwidth=2,relief=GROOVE)
    a3.grid(row=3,column=6)

    a4=Button(root,text ='Check Booked Seat',command=tab3,font='arial 20 bold',fg='black',bg='green3')
    a4.grid(row=3,column=10)

    a5=Button(root,text ='Add Bus Details',font='arial 20 bold',fg='black',bg='green4')
    a5.grid(row=3,column=14,pady=10)

    a6=Label(root,text ='For Admin Only',font='arial 16 bold',fg='red2')
    a6.grid(row=4,column=14)




tab()

root.mainloop()
