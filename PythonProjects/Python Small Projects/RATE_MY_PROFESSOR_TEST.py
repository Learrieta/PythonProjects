import tkinter.messagebox
from tkinter import  *
import tkinter as tk
import random as rd
import datetime 
import os
from secrets import choice
from turtle import width
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Avamery2021!",
    database = "rateprofessor"
)
mycursor = db.cursor()


#Option Number one will search the professor of the user's choice
def searchProfessor():
    root1 = Tk()
    label=Label(root1,text="Select the search criteria: ",font='arial 25 bold')
    fn=Button(root1,text="Search Name ",font="arial 20 bold",bg='cyan',command= search_n)
    ln=Button(root1,text="Search Last Name",font="arial 20 bold",bg='cyan',command=search_ln)
    all=Button(root1,text="List of Teachers",font="arial 20 bold",bg='cyan',command=search_all)
    label.pack()
    fn.pack(side=LEFT,padx=100)
    ln.pack(side=LEFT,padx=100)
    all.pack(side=LEFT,padx=100)
    frame=Frame(root1,height=400,width=100)
    frame.pack()
    root.resizable(False,False)
    root1.mainloop()
#Function that search by name
def search_n(): 
    global e1
    root2=Tk()
    label=Label(root2,text="Search Name: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=200,width=200)
    frame.pack()
    l1=Label(root2,text="Professor Name: ")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root2)
    e1.place(x=100,y=130)
    b1=Button(root2,text="SUBMIT",command=result_n)
    b1.place(x=90,y=180)
    root2.mainloop()
def result_n():
    global e1
    root3=Tk()
    label=Label(root3,text="Teacher: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root3,height=120,width=100)
    frame.pack()
    entry= e1.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_name, course_name,course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where faculty_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    details = Label(root3,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root3,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root3,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))

    root3.mainloop()
#Function that search by last name
def search_ln():
    global e2
    root4=Tk()
    label=Label(root4,text="Search Last Name: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root4,height=200,width=200)
    frame.pack()
    l1=Label(root4,text="Professor Name: ")
    l1.place(x=10,y=130)
    e2=tkinter.Entry(root4)
    e2.place(x=100,y=130)
    b1=Button(root4,text="SUBMIT",command=results_ln)
    b1.place(x=90,y=180)
    root4.mainloop()
def results_ln():
    global e2
    root4=Tk()
    label=Label(root4,text="Teacher: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root4,height=120,width=100)
    frame.pack()
    entry= e2.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_lastname,faculty_name, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where faculty_lastname =%s", (entry_0,))
    mydata = mycursor.fetchall()
    details = Label(root4,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root4,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root4,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))

    root4.mainloop()
#Function that prints all the courses and teachers available with their reviews
def search_all():
    root5=Tk()
    label=Label(root5,text="Teacher: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root5,height=120,width=100)
    frame.pack()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    details = Label(root5,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root5,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root5,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))

    root5.mainloop()

def searchCourse():
    root6 = Tk()
    label=Label(root6,text="Select the search criteria: ",font='arial 25 bold')
    fn=Button(root6,text="Search by Course Name ",font="arial 20 bold",bg='cyan',command= course_name)
    all=Button(root6,text="List of Courses",font="arial 20 bold",bg='cyan',command=all_courses)
    label.pack()
    fn.pack(side=LEFT,padx=100)
    all.pack(side=LEFT,padx=100)
    frame=Frame(root6,height=400,width=100)
    frame.pack()
    root.resizable(False,False)
    root6.mainloop()

def course_name(): 
    global e3
    root7=Tk()
    label=Label(root7,text="Search course: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="Course Name: ")
    l1.place(x=10,y=130)
    e3=tkinter.Entry(root7)
    e3.place(x=100,y=130)
    b1=Button(root7,text="SUBMIT",command=result_course_name)
    b1.place(x=90,y=180)
    root7.mainloop()
def result_course_name():
    global e3
    root8=Tk()
    label=Label(root8,text="Teacher: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root8,height=120,width=100)
    frame.pack()
    entry= e3.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where course_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    details = Label(root8,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root8,text="Course, Course Code, Credit, Name and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root8,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))
   
def  all_courses():
    root9=Tk()
    label=Label(root9,text="Courses: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root9,height=120,width=100)
    frame.pack()
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    details = Label(root9,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root9,text="Course, Course Code, Credit, Name and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root9,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))

def writeReview():
    root10 = Tk()
    label=Label(root10,text="Pick an Option!",font='arial 25 bold')
    luis=Button(root10,text="Luis Hidalgo",font="arial 20 bold",bg='cyan',command= choice_luis)
    german=Button(root10,text="German Garcia",font="arial 20 bold",bg='cyan',command= choice_german)
    jerry=Button(root10,text="Jerry Edmonds",font="arial 20 bold",bg='cyan',command=choice_jerry)
    frank=Button(root10,text="Frank Lozano",font="arial 20 bold",bg='cyan',command=choice_frank)
    add_new=Button(root10,text="Add a new Teacher",font="arial 20 bold",bg='cyan',command= write_new)
    label.pack()
    luis.pack(side=LEFT,padx=(70,10))
    german.pack(side=LEFT,padx=10)
    jerry.pack(side=LEFT,padx=10)
    frank.pack(side=LEFT,padx=10)
    add_new.pack(side=LEFT,padx=10)
    frame=Frame(root10,height=400,width=100)
    frame.pack()
    root.resizable(False,False)
    root10.mainloop()
    
def choice_luis():
    global e4
    root11=tk.Tk()
    label=Label(root11,text="Write review for Luis ",font='arial 25 bold')
    label.pack(padx = (20,0))
    frame=Frame(root11,height=200,width=200)
    frame.pack()
    e4=tk.Text(root11, height = 7, width = 42)
    e4.place(x=10,y=50)
    b1=Button(root11,text="SUBMIT",command=choice_luis_review)
    b1.place(x=150,y=190)
    root11.mainloop()
def choice_luis_review():
    global e4
    root12=Tk()
    label=Label(root12,text="Reviews: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root12,height=120,width=100)
    frame.pack()
    entry= e4.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,1)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    details = Label(root12,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root12,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root12,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))
    root12.mainloop()

def choice_german():
    global e5
    root13=tk.Tk()
    label=Label(root13,text="Write review for German ",font='arial 25 bold')
    label.pack(padx = (20,0))
    frame=Frame(root13,height=200,width=200)
    frame.pack()
    e5=tk.Text(root13, height = 7, width = 42)
    e5.place(x=10,y=50)
    b1=Button(root13,text="SUBMIT",command=choice_german_review)
    b1.place(x=150,y=190)
    root13.mainloop()
def choice_german_review():
    global e5
    root14=Tk()
    label=Label(root14,text="Reviews: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root14,height=120,width=100)
    frame.pack()
    entry= e5.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,2)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    details = Label(root14,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root14,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root14,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))
    root14.mainloop()

def choice_jerry():
    global e6
    root15=tk.Tk()
    label=Label(root15,text="Write review for Jerry ",font='arial 25 bold')
    label.pack(padx = (20,0))
    frame=Frame(root15,height=200,width=200)
    frame.pack()
    e6=tk.Text(root15, height = 7, width = 42)
    e6.place(x=10,y=50)
    b1=Button(root15,text="SUBMIT",command=choice_jerry_review)
    b1.place(x=150,y=190)
    root15.mainloop()
def choice_jerry_review():
    global e6
    root16=Tk()
    label=Label(root16,text="Reviews: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root16,height=120,width=100)
    frame.pack()
    entry= e6.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,3)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    details = Label(root16,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root16,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root16,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))
    root16.mainloop()

def choice_frank():
    global e7
    root17=tk.Tk()
    label=Label(root17,text="Write review for Frank ",font='arial 25 bold')
    label.pack(padx = (20,0))
    frame=Frame(root17,height=200,width=200)
    frame.pack()
    e7=tk.Text(root17, height = 7, width = 42)
    e7.place(x=10,y=50)
    b1=Button(root17,text="SUBMIT",command=choice_frank_review)
    b1.place(x=150,y=190)
    root17.mainloop()

def choice_frank_review():
    global e7
    root18=Tk()
    label=Label(root18,text="Reviews: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root18,height=120,width=100)
    frame.pack()
    entry= e7.get("1.0",'end-1c')
    entry_0 = str(entry)
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(entry_0,))
    db.commit()
    last_digit = mycursor.lastrowid
    mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,4)", (last_digit,))
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
    mydata = mycursor.fetchall()
    details = Label(root18,text="The content details are as follows : ", font = 'arial 15')
    details.pack()
    details.place(x=30, y = 50)
    details2=Label(root18,text="Name , Course, Course Code, Credit and Reviews ",font = 'arial 15')
    details2.pack()
    details2.place(x=30, y=80 )
    for rows in mydata:
        answer = Label(root18,text = str(rows, ), font = 'arial 15')
        answer.pack(pady=(0, 30))
    root18.mainloop()

def write_new():
    f = []
    c = []
    r = []
    print("Please enter the following: ")
    print()
    name = input("First name: ")
    f.append(name)
    lname = input("Last Name: ")
    f.append(lname)
    cont_faculty = (f)
    sql_faculty = "INSERT INTO faculty (faculty_name, faculty_lastname) VALUES (%s,%s)"
    mycursor.execute(sql_faculty,cont_faculty)
    db.commit()
    last_digit = mycursor.lastrowid
    c_name = input("Course Name: ")
    c.append(c_name)
    c_number = int(input("Course Number: "))
    c.append(c_number)
    c_credits = int(input("Enter number of Credits: "))
    c.append(c_credits)
    c.append(last_digit)
    cont_course = (c)
    sql_course = "INSERT INTO course (course_name, course_number, credits, faculty_id) VALUES (%s,%s,%s,%s)"
    mycursor.execute(sql_course,cont_course)
    db.commit()
    lh = input("Write a review (max 400 characters): ")
    mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(lh,))
    db.commit()
    last_digit_r = mycursor.lastrowid
    r.append(last_digit_r)
    r.append(last_digit)
    cont_r = (r)
    sql_r = "INSERT INTO reviews_has_faculty VALUES (%s,%s)"
    mycursor.execute(sql_r, cont_r)
    db.commit()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit_r,))
    mydata = mycursor.fetchall()
    print("The content details are as follows : ")
    print(" Name , Course, Course Code, Credit  and Reviews ")
    for row in mydata:
        print(row)

root=Tk()
label=Label(root,text="Welcome to Rate my Professor of BYU-I",font="arial 40 bold",bg='blue')
b1=Button(text="Search Professor",font="arial 20 bold",bg='cyan',command=searchProfessor)
b2=Button(root,text="Search Course",font="arial 20 bold",bg='cyan',command=searchCourse)
b3=Button(root,text="Write a Review",font="arial 20 bold",bg='cyan',command=writeReview)
label.pack()
b1.pack(side=LEFT,padx=100)
b2.pack(side=LEFT,padx=100)
b3.pack(side=LEFT,padx=100)
frame=Frame(root,height=400,width=100)
frame.pack()
root.mainloop()
    