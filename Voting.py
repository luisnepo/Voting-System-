from loginwindow import *
from Gsu_Candidate import Candidates
# Done by Luis Nepomuceno lg6598x with the help of Jingjie Weng jw9085d
#defines the Voting Window,where the usar can select President,Gsu_Officer or Faculty_Officer
 class VoteWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Header = Label(self, text="Voting system", width=20, font=("bold", 18))
        self.Header.place(x=120, y=20)

        self.signout = tk.Button(self, bg = "black", fg = "white", text="signout", command=lambda:self.return_clicked(controller))
        self.signout.place(x=440, y=460)


        self.label_gsu = Label(self, text="GSU Position:", width=20, font=("bold", 11))
        self.label_gsu.place(x=-40, y=80)

        list1 = ["President", "GSU_Officer", "Faculty_Officer"]

        self.gsuSelected = tk.StringVar()
        self.droplist1 = tk.OptionMenu(self, self.gsuSelected, *list1)
        self.droplist1.config(width=15)
        self.gsuSelected.set("Select")
        self.droplist1.place(x=100, y=77)
        self.positionSelected = tk.StringVar()
        self.select = tk.Button(self, bg="black", fg="white", text="select",
                                command=lambda: self.Choice())
        self.select.place(x=240, y=79)
#checks what the user choose in gsuSelected and then if the user entered President passes self,position to the Candidates.President
# if the user chooses Gsu_Officer or Faculty_Officer then it goes to Button2 where the user can choose the Position_ID
    def Choice(self):
        position = self.gsuSelected.get()
        if position == "President":
            Candidates.president(self,position)
        elif position == "GSU_Officer":
            self.button2()
        elif position == "Faculty_Officer":
            self.button2()
#makes a drop list and another button to appear on the window,where it lets the user choose which Position_ID it wants to vote for.
    def button2(self):
        position = self.gsuSelected.get()
        droplist2 = tk.OptionMenu(self, self.positionSelected, "1", "2", "3")
        droplist2.config(width=15)
        droplist2.place(x=300, y=77)
        select2 = tk.Button(self, bg="black", fg="white", text="select",
                        command=lambda: self.Choice2(position))
        select2.place(x=440, y=79)
# gets position_ID from the user selection on droplist 2 and then checks if the user chooses Gsu_Officer,if so passes position_ID
# to GsuOfficer in candidates,else it gets the student Faculty and passes position_ID and Faculty to FacultyOfficer
# in cadidates.
    def Choice2(self,position):
        conn = sqlite3.connect("GsuCandidates.db")
        position_ID = self.positionSelected.get()
        if position == "GSU_Officer":
            Candidates.GsuOfficer(self,position_ID)
        else :
            with open("Students.txt") as f:
                data = f.readline()
                student_id = data
                tv= conn.execute("SELECT faculty from Students WHERE Student_ID=:Student_id",{ "Student_id": student_id})
            for row in tv.fetchall():
                Faculty = row[0]
            Candidates.FacultyOfficer(self,position_ID,Faculty)

#returns to the main page
    def return_clicked(self,controller):
        controller.show_window("StartWindow")





