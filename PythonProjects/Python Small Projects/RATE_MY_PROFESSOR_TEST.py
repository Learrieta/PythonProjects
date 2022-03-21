import tkinter.messagebox
from tkinter import  *
import random as rd
import datetime 
import os
from secrets import choice
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Avamery2021!",
    database = "rateprofessor"
)
mycursor = db.cursor()



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

def search_n(): 
    global entry_0
    root2=Tk()
    label=Label(root2,text="Search Name: ",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=500,width=200)
    frame.pack()
    l1=Label(root2,text="Professor Name: ")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root2)
    entry= e1.get()
    entry_0 = str(entry)
    e1.place(x=100,y=130)
    b1=Button(root2,text="SUBMIT",command=result)
    b1.place(x=150,y=370)
    root2.mainloop()
def result():
    global entry_0
    mycursor.execute("SELECT faculty_name, course_name,course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where faculty_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    print("The content details are as follows : ")
    print(" Name , Course, Course Code, Credit and Reviews ")
    for rows in mydata:
        print(rows)

    

def search_ln():
    l = input("Enter the professor's last name: ")
    mycursor.execute("SELECT faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where faculty_lastname =%s", (l,))
    mydata = mycursor.fetchall()
    print("The content details are as follows : ")
    print(" Last Name , Course, Course Code, Credit  and  Reviews ")
    for rows in mydata:
        print(rows)

def search_all():
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    print("The content details are as follows : ")
    print(" Name, Last Name , Course,Course Code, Credit  Reviews ")
    for rows in mydata:
        print(rows)
    


def searchCourse():
    print("Select the search criteria:")
    print()
    print("1: Search by name ")
    print()
    print("2: Show All  ")
    print()
    
    choice = int(input("Enter choice: "))
    print()

    if choice == 1 : 
        f = input("Enter the course name: ")
        mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where course_name =%s", (f,))
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print("Course, Course Code, Credit , Faculty Name and  Reviews ")
        for rows in mydata:
            print(rows)
    elif choice == 2:
        mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print("Course, Course Code, Credit, Faculty Name and  Reviews ")
        for rows in mydata:
            print(rows)

def writeReview():
    print("Which professor would you like to write a review for?")
    print()
    print("1: Luis Hidalgo ")
    print("2: German Garcia  ")
    print("3: Jerry Edmonds ")
    print("4 : Frank Lozano")
    print("5: Add a new professor")
    print()
    choice = input("Enter choice: ")
    print()
    if choice == 1:
        lh = input("Write a review (max 400 characters): ")
        mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(lh,))
        db.commit()
        last_digit = mycursor.lastrowid
        mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,1)", (last_digit,))
        db.commit()
        mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print(" Name , Course, Course Code, Credit  and Reviews ")
        for row in mydata:
            print(row)
    if choice == 2:
        lh = input("Write a review (max 400 characters): ")
        mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(lh,))
        db.commit()
        last_digit = mycursor.lastrowid
        mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,2)", (last_digit,))
        db.commit()
        mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print(" Name , Course, Course Code, Credit  and Reviews ")
        for row in mydata:
            print(row)
    if choice == 3:
        lh = input("Write a review (max 400 characters): ")
        mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(lh,))
        db.commit()
        last_digit = mycursor.lastrowid
        mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,3)", (last_digit,))
        db.commit()
        mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print(" Name , Course, Course Code, Credit  and Reviews ")
        for row in mydata:
            print(row)
    if choice == 4:
        lh = input("Write a review (max 400 characters): ")
        mycursor.execute("INSERT INTO reviews (reviews) VALUES(%s)",(lh,))
        db.commit()
        last_digit = mycursor.lastrowid
        mycursor.execute("INSERT INTO reviews_has_faculty VALUES (%s,4)", (last_digit,))
        db.commit()
        mycursor.execute("SELECT faculty_name, faculty_lastname, course_name,course_number, credits,  reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where r.reviews_id = %s ", (last_digit,))
        mydata = mycursor.fetchall()
        print("The content details are as follows : ")
        print(" Name , Course, Course Code, Credit  and Reviews ")
        for row in mydata:
            print(row)
    if choice == 5:
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
b1=Button(text="Search Teacher",font="arial 20 bold",bg='cyan',command=searchProfessor)
label.pack()
b1.pack(side=LEFT,padx=10)
frame=Frame(root,height=500,width=100)
frame.pack()
root.mainloop()
    