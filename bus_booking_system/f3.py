from tkinter import *
root=Tk()
(h,w)=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
home=PhotoImage(file='.\\home.png')
Label(root,image=bus).grid(row=0,padx=w//3,pady=30,columnspan=200)
Label(root,text='Online Bus Booking System',bg='lightblue',fg='red',font='Arial 28 bold',borderwidth=2,relief=GROOVE).grid(row=1,padx=w//3,pady=15,columnspan=100)
Label(root,text='Enter Journey Details',bg='lightgreen',fg='green',font='Arial 18 bold',borderwidth=2,relief=GROOVE).grid(row=2,padx=w//3,columnspan=100)
Label(root,text='TO',font='Arial 14 bold').grid(row=3,column=41)
To=Entry(root)
To.grid(row=3,column=42,padx=30)
Label(root,text='From',font='Arial 14 bold').grid(row=3,column=43)
From=Entry(root)
From.grid(row=3,column=44)
Label(root,text='Journey date',font='Arial 14 bold').grid(row=3,column=45)
Date=Entry(root)
Date.grid(row=3,column=46)

def show_bus():

    import sqlite3
    con=sqlite3.connect("Bus_Booking")
    cur=con.cursor()
    a=0
    try:
        cur.execute("select t.RouteId from route as t,route as f where t.RouteId=f.RouteId and t.sname = '"+To.get()+"' and f.sname ='"+From.get()+"'and t.std > f.std")
        result1=cur.fetchall()
        result1[0][0]
        #cur.execute(" select distinct(busId),cname,type,SeatAvil,capacity,fare from bus,route,operator,run where opeId=opId and  busId=Id and route.RouteId= bus.RouteId and route.RouteId ="+str(result1[0][0])+"")
    except sqlite3.OperationalError:
        a=-1
        import tkinter.messagebox as ms
        ok=ms.showinfo("Invalid","Please enter correct value")
 
    except NameError:
        a=-1
        import tkinter.messagebox as ms
        ok=ms.showerror("reparted value","Entery already exit")
      
    except AttributeError:
        a=-1
        import tkinter.messagebox as ms
        ok=ms.showinfo("Invalid","Enter value")
       
    except sqlite3.IntegrityError:
        a=-1
        import tkinter.messagebox as ms
        okms.showinfo("reparted value","Entery already exit")
        
    except IndexError:
        a=-1
        import tkinter.messagebox as ms
        ok=ms.showinfo("Sorry","No Bus Found")
        
    j=-1
    if(a==0):
        Label(root,text='Select Bus',font='Arial 14 bold',fg='green').grid(row=5,column=41)
        Label(root,text='Operator',font='Arial 14 bold',fg='green').grid(row=5,column=42)
        Label(root,text='Bus Type',font='Arial 14 bold',fg='green').grid(row=5,column=43)
        Label(root,text='Available/Capacity',font='Arial 14 bold',fg='green').grid(row=5,column=44)
        Label(root,text='Fare',font='Arial 14 bold',fg='green').grid(row=5,column=45)

        for i in result1:
            j=j+1
            cur.execute(" select distinct(busId),cname,type,SeatAvil,capacity,fare, RDate from bus,route,operator,run where opeId=opId and  busId=Id and route.RouteId= bus.RouteId and route.RouteId ="+str(result1[j][0])+"")
            result2=cur.fetchall()
            bus_select= IntVar()
            r1=Radiobutton(root,text='Bus'+str(j+1),font='Arial 12 bold',variable=bus_select,value=1+j)
            r1.grid(row=6+j,column=41,pady=10)
            #Label(root,text='Select Bus',font='Arial 14 bold',fg='green').grid(row=6+i,column=41)
            Label(root,text=str(result2[j][1]),font='Arial 14 bold',fg='green').grid(row=6+j,column=42)
            Label(root,text=str(result2[j][2]),font='Arial 14 bold',fg='green').grid(row=6+j,column=43)
            Label(root,text=str(result2[j][3])+"/"+str(result2[0][4]),font='Arial 14 bold',fg='green').grid(row=6+j,column=44)
            Label(root,text=str(result2[j][5]),font='Arial 14 bold',fg='green').grid(row=6+j,column=45)
              
            def proceed_to_book():
                Label(root,text='Fill Passenger Details to book the Bus Ticket',bg='light sky blue',fg='red2',font='Arial 24 bold',borderwidth=2,relief=GROOVE).grid(padx=w//4,pady=15,row=9,columnspan=100)
                Name=Entry(root)
                Name.grid(row=10,column=41)
                Label(root,text='Name',font='Arial 14 bold').grid(row=10,column=40,pady=40)
                Label(root,text='Gender',font='Arial 14 bold').grid(row=10,column=42)
                gender_a=StringVar()
                gender_a.set('Gender')
                op=['Male','Female','Other']
                menu=OptionMenu(root,gender_a,*op).grid(row=10,column=43)
                No_of_seats=Entry(root)
                No_of_seats.grid(row=10,column=45)
                Label(root,text='No of seats',font='Arial 14 bold').grid(row=10,column=44)
                Mobile=Entry(root)
                Mobile.grid(row=10,column=47)
                Label(root,text='Mobile No',font='Arial 14 bold').grid(row=10,column=46)
                Age=Entry(root)
                Age.grid(row=10,column=49)
                Label(root,text='Age',font='Arial 14 bold').grid(row=10,column=48)
                def ticket():
                    if(int(No_of_seats.get())  <=  int(result2[0][3])):
                        cur.execute("insert into BookingHistory values("+Mobile.get()+",'"+Name.get()+"','"+gender_a.get()+"',"+str(result2[bus_select.get()][0])+",'"+"2022/11/29"+"','"+str(result2[bus_select.get()][5])+"','"+To.get()+"','"+From.get()+"',"+No_of_seats.get()+","+Age.get()+")")
                        con.commit()
                        import tkinter.messagebox as ms
                        ms.showinfo("successful transaction","Thank you for use service")          
                        
                        


                    else:
                        import tkinter.messagebox as ms
                        ms.showerror("Error","Try to Book more then Available Seat")
                Button(root,text='Book Seat',font='Arial 14 bold',bg='green3',command=ticket).grid(row=10,column=50,pady=10)


                
            Button(root,text='Proceed to Book',font='Arial 14 bold',bg='green3',command=proceed_to_book).grid(row=8,column=47,pady=10)      
 
    
      


Button(root,text='Show Bus',bg='green',font='Arial 14 bold',command=show_bus).grid(row=3,column=47)
def Home():
    root.destroy()
    import f2
Button(root,image=home,command=Home).grid(row=3,column=48)

root.mainloop()
