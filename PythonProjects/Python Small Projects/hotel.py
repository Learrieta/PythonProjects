import tkinter.messagebox
from tkinter import  *
import random as rd
import datetime 
import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="Avamery2021!")
cur=con.cursor()
cur = con.cursor(buffered=True) 
cur.execute("create database if not exists hello")

cur.execute("use hello")

cur.execute("create table if not exists apt"
            "("
            "idno varchar(12) primary key,"
            "name char(20),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")



#  Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
        
    cur.execute('insert into apt values(%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,))
    con.commit()
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

#  For registration 
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
    label.pack()
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    l1=Label(root1,text="PATIENT ID")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=100,y=130)
    l2=Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=100,y=170)
    l3=Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=100,y=210)
    l4=Label(root1,text="GENDER M\F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=100,y=250)
    l5=Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=100,y=290)
    l6=Label(root1,text="BLOOD GROUP")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=100,y=330)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=150,y=370)
    
    root.resizable(False,False)
    root1.mainloop()

#  Message for appointment
def apo_details():
     global x2
     p1=x2.get()    
     if int(p1)==1:
         i=("Dr. Varun \nRoom no:- 201")
         j=("Dr. Hrithik \nRoom no:- 202")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
     elif int(p1)==2:
         i=("Dr. Sidharth \nRoom no. 207")
         j=("Dr. Abhishek \nRoom no. 208")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=5),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
     elif int(p1)==3:
         i=("Dr. Salman \nRoom no. 203")
         j=("Dr. Shahrukh \nRoom no. 204")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

     elif int(p1)==4:
         i=("Dr. Ajay, \nRoom no. 209")
         j=("Dr. Ranveer \nRoom no. 200")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=6),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

     elif int(p1)==5:
         i=("Dr. Akshay \nRoom no. 205")
         j=("Dr. Amir \nRoom no. 206")
         q=(i,j)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=4),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   

     elif int(p1)==6:
         i=("Dr. Irfan \nRoom no. 001")
         j=("Dr. John \nRoom no. 002")
         k=("Dr. Sanjay \nRoom no. 003")
         l=("Dr. Shahid \nRoom no. 004")
         q=(i,j,k,l)
         h=rd.choice(q) 
         u=(23,34,12,67,53,72)
         o=rd.choice(u)        
         det=("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=1),'\nAppointmnet no:-',o)
         tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
 
     else:
          tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')

#  For appointment
def get_apoint():
    global x1,x2
    p1=x1.get()  
    cur.execute('select * from apt where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3=Tk()
        label=Label(root3,text="APPOINTMENT",font='arial 25 bold')
        label.pack()
        frame=Frame(root3,height=500,width=300)
        frame.pack()
        if i[3]=='M' or i[3]=='m':
                x="Mr."
                name2=Label(root3,text=i[1])
                name2.place(x=140,y=80)
        else:
                x="Mrs\Ms."
                name2=Label(root3,text=i[1])
                name2.place(x=170,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME')
            name.place(x=50,y=80)
            name1=Label(root3,text=x)
            name1.place(x=120,y=80)
            age=Label(root3,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2])
            age1.place(x=100,y=100)
            phone=Label(root3,text='PHONE:-')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[4])
            phone1.place(x=100,y=120)
            bg=Label(root3,text='BLOOD GROUP:-')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[5])
            bg1.place(x=150,y=140)


        L=Label(root3,text='DEPARTMENTS')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.Cardiologist ")
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.Rheumatologist')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Psychitrist')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Neurologist')
        L4.place(x=50,y=310)
        L5=Label(root3,text='5.Otolaryngonologist')
        L5.place(x=50,y=330)
        L6=Label(root3,text='6.MI Room')
        L6.place(x=50,y=350)
        L7=Label(root3,text='Enter')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=150,y=370)        
        B1=Button(root3,text='Submit',command=apo_details)
        B1.place(x=120,y=440)   
        root3.resizable(False,False)
        root3.mainloop()

#  For Adhaar no input
def apoint():
    global x1
    root2=Tk()
    label=Label(root2,text="APPOINTMENT",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=200,width=200)
    frame.pack()
    l1=Label(root2,text="ADHAAR NO.")
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2)
    x1.place(x=100,y=130)
    b1=Button(root2,text='Submit',command=get_apoint)
    b1.place(x=100,y=160)
    root2.resizable(False,False)
    root2.mainloop()
    
#  List of doctors
def lst_doc():
    root4=Tk()
    
    l=["Dr. Varun","Dr. Hrithik","Dr. Salman","Dr. Shahrukh","Dr. Akshay","Dr. Amir","Dr. Sidharth","Dr. Abhishek","Dr. Ajay","Dr. Ranveer",'Dr. Irfan','Dr. John','Dr. Sanjay','Dr. Shahid']
    m=["Cardiologist","Cardiologist","Psychitrist","Psychitrist","Otolaryngonologist","Otolaryngonologist","Rheumatologist","Rheumatologist","Neurologist","Neurologist",'MI room','MI room','MI room','MI room']
    n=[201,202,203,204,205,206,207,208,209,200,401,402,403,404]

    frame=Frame(root4,height=500,width=500)
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF DOCTORS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(root4,text=i)
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT')
    l2.place(x=140,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(root4,text=i)
       l3.place(x=140,y=count1)

    l4=Label(root4,text='ROOM NO')
    l4.place(x=260,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(root4,text=i)
       l5.place(x=260,y=count2)
    root.resizable(False,False)
    root4.mainloop()

def ser_avail():
    root5=Tk()
    frame=Frame(root5,height=500,width=500)
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    f=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root5,text=i)
       l3.place(x=20,y=count1)
    l2=Label(root5,text='ROOM NO.')
    l2.place(x=140,y=10)
    g=[101,102,103,104,105,301,302,303,304]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root5,text=i)
       l4.place(x=140,y=count2)
    l5=Label(root5,text='To avail any of these please contact on our no.:- 9211420420')
    l5.place(x=20,y=240)
    root5.resizable(False,False)
    root5.mainloop()

def mod_sub():
    global x3
    root7=Tk()
    label=Label(root7,text="MODIFICATION",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="ADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=100,y=130)
    b1=Button(root7,text='Submit',command=modify)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()
     



def modify():
    global x3,x4
    p1=x3.get()
    cur.execute('select * from apt where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else: 
      root6=Tk()
      frame=Frame(root6,height=500,width=500)
      frame.pack()
      l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
      l1.place(x=75,y=10)
      l2=Label(root6,text='WHAT YOU WANT TO CHANGE')
      l2.place(x=50,y=200)
      l3=Label(root6,text='1.NAME')
      l3.place(x=50,y=220)
      l4=Label(root6,text='2.AGE')
      l4.place(x=50,y=240)
      l5=Label(root6,text='3.GENDER')
      l5.place(x=50,y=260)
      l6=Label(root6,text='4.PHONE')
      l6.place(x=50,y=280)
      l7=Label(root6,text='5.BLOOD GROUP')
      l7.place(x=50,y=300)
      x2=Label(root6,text='Enter')
      x2.place(x=50,y=330)
      x4=tkinter.Entry(root6)
      x4.place(x=100,y=330)
      for i in dat:
            name=Label(root6,text='NAME:-')
            name.place(x=50,y=80)
            name1=Label(root6,text=i[1])
            name1.place(x=150,y=80)
            age=Label(root6,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root6,text=i[2])
            age1.place(x=150,y=100)
            gen=Label(root6,text='GENDER:-')
            gen.place(x=50,y=120)
            gen1=Label(root6,text=i[3])
            gen1.place(x=150,y=120)
            pho=Label(root6,text='PHONE:-')
            pho.place(x=50,y=140)
            pho1=Label(root6,text=i[4])
            pho1.place(x=150,y=140)
            bg=Label(root6,text='BLOOD GROUP:-')
            bg.place(x=50,y=160)
            bg1=Label(root6,text=i[4])
            bg1.place(x=150,y=160)
      b=Button(root6,text='Submit')
      b.place(x=50,y=400)
      L1=Label(root6,text='OLD DETAILS')
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL')
      L2.place(x=50,y=360)
      x5=tkinter.Entry(root6)
      x5.place(x=160,y=360)

      root6.resizable(False,False)
      root6.mainloop()
    
    
root=Tk()
label=Label(root,text="CITY HOSPITAL",font="arial 40 bold",bg='blue')
b1=Button(text="Registration",font="arial 20 bold",bg='cyan',command=register)
b2=Button(text="Appointment",font="arial 20 bold",bg='cyan',command=apoint)
b3=Button(text="List of Doctors",font="arial 20 bold",bg='cyan',command=lst_doc)
b4=Button(text="Services available",font='arial 20 bold',bg='cyan',command=ser_avail)
b5=Button(text="Modify data",font='arial 20 bold',bg='cyan',command=mod_sub)
b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,bg='yellow')
label.pack()
b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)
b4.pack(side=LEFT,padx=10)
b5.pack(side=LEFT,padx=10)
b6.pack(side=LEFT,padx=10)
frame=Frame(root,height=500,width=100)
frame.pack()
root.resizable(False,False)
root.mainloop()