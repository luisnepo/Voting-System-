# imports tkinter for the window options,sqlite for the database,tkinter.messagebox for showing errors and info on pop ups
# and datetime that serves as the deadline definer.
import tkinter as tk
from tkinter import *
import sqlite3
import tkinter.messagebox as tm
import datetime

today_date = datetime.datetime.now()
deadline = datetime.datetime(2020, 1, 28)
# done by Mohammed Islam im7494x
#Defines the first window to appear,allows the user to login
class LoginWindow(tk.Frame):
    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.Header = Label(self,text = "Login window",width = 20, font =("bold",18))
        self.Header.place(x = 120,y = 53)

        self.StudentID_label = Label(self,text = "Student_ID:",width = 20,font =("bold",12))
        self.StudentID_label.place(x = 105,y= 125)

        self.Password_label = Label(self,text = "Password:",width = 20,font =("bold",12))
        self.Password_label.place(x = 105,y= 165)

        self.entry_student_ID = Entry(self)
        self.entry_student_ID.place(x = 240,y= 130)

        self.entry_password = Entry(self,show = "*")
        self. entry_password.place(x = 240, y =170)

        self.login_button = Button(self,text = "login",width = 20,  bg = "black", fg = "white",
                              command=lambda: self.LoginClicked(controller))
        self.login_button.place(x=180 ,y=300)


#gets the data from the student ID and password entrys and then checks to see if the user is within the database.
    def LoginClicked(self,controller):
        db = sqlite3.connect("GsuCandidates.db")
        cursor = db.cursor()


        StudentID_txt = getattr(self, "entry_student_ID")
        StudentID = StudentID_txt.get()

        password_txt = getattr(self, "entry_password")
        password = password_txt.get()

        query = "SELECT * FROM Students WHERE Student_ID = '{}' AND Password = '{}'".format(StudentID, password)

        cursor.execute(query)
        rows = cursor.fetchall()
    # checks if there is a row where the Student ID and Password match,if so allow the user to login but first performs
    # a check using the today_date and deadline,if the user is trying to vote outside the deadline a pop up error will open up.
        if len(rows) == 1:
            if today_date <= deadline:
                f = open("Students.txt","w+")
                f.write(StudentID)
                tm.showinfo("login","Welcome")
                controller.show_window("StartWindow")
            else:
                tm.showerror("Login error", "Elections are over")
        else:
            tm.showerror("Login error","incorrect username/password")




