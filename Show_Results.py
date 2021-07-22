from loginwindow import *
# Done by Luis Nepomuceno lg6598x and Jingjie Weng jw9085d
# Class that creates the window that will Show results,shows a droplist that allows the user to select the position they wish to
# see the results for.
class ShowResults(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Header = Label(self, text="Voting Results", width=20, font=("bold", 18))
        self.Header.place(x=100, y=20)

        self.signout = tk.Button(self, bg="black", fg="white", text="signout",
                                 command=lambda: return_clicked(controller))
        self.signout.place(x=440, y=460)

        self.label_position = Label(self, text="")
        self.label_gsu = Label(self, text="GSU Position:", width=20, font=("bold", 11))
        self.label_gsu.place(x=-40, y=80)

        list1 = ["President", "Gsu_Officer", "Faculty_Officer"]

        self.gsuSelected = tk.StringVar()
        self.droplist1 = tk.OptionMenu(self, self.gsuSelected, *list1)
        self.droplist1.config(width=15)
        self.gsuSelected.set("Select")
        self.droplist1.place(x=100, y=77)
        self.positionSelected = tk.StringVar()
        self.select = tk.Button(self, bg="black", fg="white", text="select",
                                command=lambda: self.Choice())
        self.select.place(x=240, y=79)

#   Act as select funcionality,gets the position from gsuSelected and passes it on into report (if it's President
#   only has 1 Position_ID or passes onto button 2 so the user can select the Position_ID.
    def Choice(self):
        position = self.gsuSelected.get()
        if position == "President":
            self.report(position)
        elif position == "Gsu_Officer":
            self.button2(position)
        elif position == "Faculty_Officer":
            self.button2(position)

### acts as button 2 funcionality,it shows a list for 1,2,3 and allows the user to select the Position_ID.
    def button2(self,position):
        droplist2 = tk.OptionMenu(self, self.positionSelected, "1", "2", "3")
        droplist2.config(width=15)
        droplist2.place(x=300, y=77)
        select2 = tk.Button(self, bg="black", fg="white", text="select",
                            command=lambda: self.Choice2(position))
        select2.place(x=440, y=79)
### creates the button where it gets the position_ID and passes it on to report.
    def Choice2(self, position):
        global Faculty
        conn = sqlite3.connect("GsuCandidates.db")
        Position_ID = self.positionSelected.get()
        if position == "Gsu_Officer":
            self.report(position,Position_ID)
        else:
            with open("Students.txt") as f:
                data = f.readline()
            student_id = data
            tv = conn.execute("SELECT faculty from Students WHERE Student_ID=:Student_id",
                                      {"Student_id": student_id})
            for row in tv.fetchall():
                Faculty = row[0]
            self.report(position,Position_ID,Faculty)

### gets position,Position_ID(default = 1) and Faculty(default = "null") then shows all the candidates and their current Votes.
    def report(self,position,Position_ID = "1",Faculty = "null"):
        select3 = tk.Button(self, bg="black", fg="white", text="Show Winner",
                        command=lambda: self.report_winner(position,Position_ID,Faculty))
        select3.place(x=200, y=460)

        conn = sqlite3.connect("GsuCandidates.db")
        record = conn.execute(
            "SELECT First_name,Last_name,Vote_1,Vote_2,Vote_3,Vote_4, Faculty from Gsu_Candidates WHERE Position =:position AND Position_ID =:id AND Faculty=:Faculty",
            {'position': position, 'id': Position_ID,"Faculty" : Faculty})
        candidates = record.fetchall()

        text = tk.Text(self, width=40, heigh=20)
        text.place(x=100, y=120)
        a = 0
        for record in candidates:
            A1 = str(candidates[a][0])
            A2 = str(candidates[a][1])
            A3 = str(candidates[a][2])
            A4 = str(candidates[a][3])
            A5 = str(candidates[a][4])
            A6 = str(candidates[a][5])
            a += 1

            text.insert("0.1", "4th preference:" + A6 + "\n")
            text.insert("0.1", "3rd preference:" + A5 + "\n")
            text.insert("0.1", "2nd preference:" + A4 + "\n")
            text.insert("0.1", "1st preference:" + A3 + "\n")
            text.insert("0.1", A1 + A2 + "\n")

#   Gets the position,Position_Id(default = 1) and Faculty(defaul = "null") and enters the database to acquire the necessary data
#   then it shows the winner of the current position/position_ID.
    def report_winner(self,position,Position_ID = "1",Faculty = "null"):

        conn = sqlite3.connect("GsuCandidates.db")
        record = conn.execute(
            "SELECT First_name,Last_name,Vote_1,Vote_2,Vote_3,Vote_4, Faculty from Gsu_Candidates WHERE Position =:position AND Position_ID =:id AND Faculty=:Faculty",
            {'position': position, 'id': Position_ID, "Faculty": Faculty})
        candidates = record.fetchall()
        sorted_candidates = sorted(candidates, key=lambda i: (i[2], i[3], i[4], i[5]), reverse=True)

        text = tk.Text(self, width=40, heigh=20)
        text.place(x=100, y=120)
        A4 = str(sorted_candidates[0][5])
        A3 = str(sorted_candidates[0][4])
        A2 = str(sorted_candidates[0][3])
        A1 = str(sorted_candidates[0][2])

        if position == "Faculty_Officer":
            text.insert("0.1", "4th preference:" + A4 + "\n")
            text.insert("0.1", "3rd preference:" + A3 + "\n")
            text.insert("0.1", "2nd preference:" + A2 + "\n")
            text.insert("0.1", "1st preference:" + A1 + "\n")
            text.insert("0.1", "Winner:" + sorted_candidates[0][0] + " " + sorted_candidates[0][1] + "\n")
            text.insert("0.1", "Faculty:" + Faculty + "\n")
        else:
            text.insert("0.1", "4th preference:" + A4 + "\n")
            text.insert("0.1", "3rd preference:" + A3 + "\n")
            text.insert("0.1", "2nd preference:" + A2 + "\n")
            text.insert("0.1", "1st preference:" + A1 + "\n")
            text.insert("0.1", "Winner:" + sorted_candidates[0][0] + " " + sorted_candidates[0][1] + "\n")

#returns to the main page
    def return_clicked(self,controller):
        controller.show_window("StartWindow")



