from msilib.schema import ListBox
from textwrap import fill
import tkinter.messagebox
from tkinter import  *
import tkinter as tk
import random as rd
import os
from secrets import choice
from turtle import width
import mysql.connector
from PIL import ImageTk, Image

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
    root1.geometry("800x700")
    root1.resizable(False, False)
    image_2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\PCT.png', master = root1)
    background1 = Label(root1, image = image_2, bd = 0)
    background1.place(x = 0, y = 0)
    img4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sn.png', master = root1)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\snl.png', master = root1)
    img6 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\lop.png', master = root1)
    fn=Button(root1,image = img4,command= search_n, bd = 0)
    ln=Button(root1,image = img5, command=search_ln, bd = 0)
    all=Button(root1,image = img6,command=search_all, bd = 0)
    fn.pack(side=LEFT,padx=(50,25), pady = (200,0))
    ln.pack(side=LEFT,padx=25, pady = (200,0))
    all.pack(side=LEFT,padx=25, pady = (200,0))
    frame=Frame(root1)
    frame.pack()
    root1.mainloop()
#Function that search by name
def search_n(): 
    global e1
    root2=Tk()
    root2.geometry("400x300")
    root2.resizable(False, False)
    image_3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbn.png', master = root2)
    background1 = Label(root2, image = image_3, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root2)
    frame.pack()
    e1=tkinter.Entry(root2)
    e1.place(x=200,y=130, height = 35)
    image_4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sup.png', master = root2)
    b1=Button(root2,image = image_4,command=result_n, borderwidth= 0 )
    b1.place(x=120,y=200)
    root2.mainloop()
def result_n():
    global e1
    root3=Tk()
    root3.geometry("800x700")
    root3.resizable(False, False)
    image_5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\rbn.png', master = root3)
    background1 = Label(root3, image = image_5, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root3)
    frame.pack()
    entry= e1.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_name, course_name,course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id where faculty_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root3,font = ("Times New Roman", 15), bd = 5, spacing1= 12 , wrap = WORD)
    scroll_bar = Scrollbar(root3,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

    root3.mainloop()
#Function that search by last name
def search_ln():
    global e2
    root4=Tk()
    root4.geometry("400x300")
    root4.resizable(False, False)
    image_6 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbln.png', master = root4)
    background1 = Label(root4, image = image_6, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root4)
    frame.pack()
    e2=tkinter.Entry(root4)
    e2.place(x=200,y=125, height = 30)
    image_7 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\suln.png', master = root4)
    b1=Button(root4,image = image_7,command=results_ln, borderwidth=0)
    b1.place(x=130,y=200)
    root4.mainloop()
def results_ln():
    global e2
    root4=Tk()
    root4.geometry("800x700")
    root4.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\rbln.png', master = root4)
    background1 = Label(root4, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root4)
    frame.pack()
    entry= e2.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT faculty_lastname,faculty_name, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where faculty_lastname =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root4,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root4,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

    root4.mainloop()
#Function that prints all the courses and teachers available with their reviews
def search_all():
    root5=Tk()
    root5.geometry("800x700")
    root5.resizable(False, False)
    image_8 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\loallp.png', master = root5)
    background1 = Label(root5, image = image_8, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root5)
    frame.pack()
    mycursor.execute("SELECT faculty_name, faculty_lastname, course_name, course_number, credits, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    text = tk.Text(root5,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root5,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
        #answer = Label(root5,text = str(rows, ), font = ("Times New Roman", 15))
        #answer.pack(side = LEFT, fill = BOTH)

    root5.mainloop()

def searchCourse():
    root6 = Tk()
    root6.geometry("800x700")
    root6.resizable(False, False)
    image_2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbci.png', master = root6)
    background1 = Label(root6, image = image_2, bd = 0)
    background1.place(x = 0, y = 0)
    img4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbucn.png', master = root6)
    img5 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbuallc.png', master = root6)
    fn=Button(root6,image = img4,command= course_name, borderwidth=0)
    all=Button(root6,image = img5, command=all_courses, borderwidth=0)
    fn.pack(side=LEFT,padx=(150,50), pady = (200,0))
    all.pack(side=LEFT,padx=25, pady = (200,0))
    frame=Frame(root6)
    frame.pack()
    root6.mainloop()

def course_name(): 
    global e3
    root7=Tk()
    root7.geometry("400x300")
    root7.resizable(False, False)
    image_3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sbcn.png', master = root7)
    background1 = Label(root7, image = image_3, bd = 0)
    background1.place(x = 0, y = 0)
    frame=Frame(root7)
    frame.pack()
    e3=tkinter.Entry(root7)
    e3.place(x=170,y=130, height = 35)
    image_4 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sup.png', master = root7)
    b1=Button(root7,image = image_4,command=result_course_name)
    b1.place(x=150,y=200)
    root7.mainloop()
def result_course_name():
    global e3
    root8=Tk()
    root8.geometry("800x700")
    root8.resizable(False, False)
    image_16 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\scs.png', master = root8)
    background16 = Label(root8, image= image_16, bd = 0)
    background16.image = image_16
    background16.place(x = 0, y = 0)
    frame=Frame(root8)
    frame.pack()
    entry= e3.get()
    entry_0 = str(entry)
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id  where course_name =%s", (entry_0,))
    mydata = mycursor.fetchall()
    text = tk.Text(root8,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root8,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')
   
def  all_courses():
    root9=Tk()
    root9.geometry("800x700")
    root9.resizable(False, False)
    image_15 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\allc.png', master = root9)
    background15 = Label(root9, image= image_15)
    background15.image = image_15
    background15.place(x = 0, y = 0)
    frame=Frame(root9)
    frame.pack()
    mycursor.execute("SELECT  course_name,course_number, credits, faculty_name, faculty_lastname, reviews FROM course AS c INNER JOIN faculty AS f ON c.faculty_id = f.faculty_id INNER JOIN reviews_has_faculty AS r ON f.faculty_id = r.faculty_id INNER JOIN reviews AS re ON re.reviews_id = r.reviews_id ")
    mydata = mycursor.fetchall()
    text = tk.Text(root9,font = ("Times New Roman", 15), bd = 5, spacing1= 12, wrap = WORD )
    scroll_bar = Scrollbar(root9,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 30, y = 300, width = 700, height = 300)
    for rows in mydata:
        text.insert(tk.END,  str(rows,) + '\n')

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
root.title('Rate my Professor')
root.geometry("800x700")
root.resizable(False, False)
image_1 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\byui.png')
background = Label(root, image = image_1, bd = 0)
background.place(x = 0, y = 0)
img1 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sp1.png')
img2 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\sc1.png')
img3 = ImageTk.PhotoImage(file = r'C:\\Users\\lhida\\OneDrive - BYU-Idaho\\Pictures\\Saved Pictures\\wr1.png')
b1=Button(root, image = img1,command=searchProfessor, borderwidth = 0)
b2=Button(root,image = img2,command=searchCourse,borderwidth = 0)
b3=Button(root,image = img3,command=writeReview, borderwidth = 0)
b1.pack(side=LEFT,padx=(50,25), pady = (300,0))
b2.pack(side=LEFT,padx=25, pady = (300,0))
b3.pack(side=LEFT,padx=25, pady = (300,0))
frame=Frame(root)
frame.pack()
root.mainloop()
    