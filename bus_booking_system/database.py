import sqlite3
con=sqlite3.connect("Bus_Booking")
cur=con.cursor()
#cur.execute('create table operator(opeId int,cname varchar(30),address varchar(50),email varchar(50),phone int(10),primary key(opeid))')
#cur.execute('create table route(RouteId int,std int,sname varchar(30),primary key(RouteId,std))')
#cur.execute('create table Bus(Id int,type varchar(20),capacity int,opId int,RouteId int,fare int,primary key(Id),foreign key(RouteId) references route(RouteId))')
#cur.execute('create table run(busId int,RDate date,SeatAvil int,primary key(busId),foreign key(BusId) references bus(Id))')

#cur.execute('create table BookingHistory(refno int(),Custname varchar(30),sex varchar(10),busId int,dateOfBooking date,dateOfjourney date,Sfrom varchar(15),Sto varchar(15)totalSeat int,age int,primary key(refno))')

##cur.execute('insert into route values(1 ,1, "Guna"),(1 ,2, "Biaora"),(1 ,3, "Shajapur"),(1 ,4, "Dewas"),(1 ,5, "Indore"),(2 ,1, "Katihar"),(2 ,2, "Korha"),(2 ,3, "Kursela"),(2 ,4, "Naugchhia"),(2 ,5, "Bhaghalpur"),(3 ,1, "Guna"),(3 ,2, "Vijaypur"),(3 ,3, "Kurawar"),(3 ,4, "Shyampur"),(3 ,5, "Bhopal")')

#cur.execute('select * from route')

#cur.execute('insert into operator values(1,"kamala","uper wali pahari,guna","kmala@gmail.com",9900990044)')

#cur.execute('select * from operator')

#cur.execute('insert into Bus values(1,"AC 2X2",30,1,1,1000)')

#cur.execute('insert into run values(1,"30/11/2002",29)')
#cur.execute('alter table BookingHistory modify column sex varchar(10)')
#cur.execute('insert into BookingHistory values(8406053625,"Priyanshu","M",1,"2025/11/25","2022/11/30","guna","bhopal")')
#con.commit()

#cur.execute("insert into route("+route.get()+","+std.get()+",'"+sname.get()+"')")
#cur.execute("insert into route values("+"7"+","+"5"+",'"+"jamalpur"+"')")
#cur.execute("insert into BookingHistory values("+Mobile.get()+",'"+Name.get()+"')")
cur.execute("insert into BookingHistory values("+Mobile.get()+",'"+Name.get()+"','"+gender_a.get()+"',"+str(result2[bus_select.get()][0])+",'"+"2022/11/29"+"','"+result2[bus_select.get()][5]+"','"+To.get()+"','"+From.get()+"')")
cur.execute("select * from Bus ")
result=cur.fetchall()
for i in result:
    print(i)
