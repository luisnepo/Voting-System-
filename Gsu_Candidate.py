from Voting import *

conn = sqlite3.connect("GsuCandidates.db")

#done by Luis Nepomuceno lg6598x
# Class where it gets the vote from VotingWindow and it gets the required data from the database to add the votes needed.
class Candidates(tk.Frame):
    #gets and shows the candidates for President
    def president(self,position):
        record = conn.execute(
            "SELECT First_name,Last_name from Gsu_Candidates WHERE Position =:position",
            {'position': position})
        Candidates.show_candidates(self,record)

    #gets and shows the candidates for FacultyOfficer
    def FacultyOfficer(self,position_ID,Faculty):
        record = conn.execute(
            "SELECT First_name,Last_name from Gsu_Candidates WHERE Position =:position AND Position_ID=:position_ID AND Faculty=:Faculty",
            {'position': "Faculty_Officer", "position_ID": position_ID, "Faculty": Faculty})
        Candidates.show_candidates(self,record)

    # gets and shows the candidates to GsuOfficer
    def GsuOfficer(self, position_ID):
        record = conn.execute(
            "SELECT First_name,Last_name from Gsu_Candidates WHERE Position =:position AND Position_ID=:position_ID",
            {'position': "Gsu_Officer", "position_ID": position_ID})
        Candidates.show_candidates(self,record)

    # shows the candidates for choosen position.
    def show_candidates(self,record):
        self.text = tk.Text(self, width=25, heigh=4)
        self.text.place(x=140, y=120)
        records = record.fetchall()
        for record in records:
            self.text.insert("0.1", "\n")
            self.text.insert("0.1", record)
        Candidates.GetVotes(self)

    #allows the user to vote and saves the entrys
    def GetVotes(self):
        self.warning = Label(self, text="Enter Last names to Vote:", width=20, font=("bold", 10))
        self.warning.place(x=150, y=240)
        self.Vote1 = Label(self, text="1st preference:", width=20, font=("bold", 10))
        self.Vote1.place(x=60, y=280)
        self.Vote2 = Label(self, text="2nd Preference:", width=20, font=("bold", 10))
        self.Vote2.place(x=60, y=320)
        self.Vote3 = Label(self, text="3rd Preference:", width=20, font=("bold", 10))
        self.Vote3.place(x=60, y=360)
        self.Vote4 = Label(self, text="4th Preference:", width=20, font=("bold", 10))
        self.Vote4.place(x=60, y=400)

        self.entry_Vote1 = Entry(self)
        self.entry_Vote1.place(x=200, y=280)
        self.entry_Vote2 = Entry(self)
        self.entry_Vote2.place(x=200, y=320)
        self.entry_Vote3 = Entry(self)
        self.entry_Vote3.place(x=200, y=360)
        self.entry_Vote4 = Entry(self)
        self.entry_Vote4.place(x=200, y=400)

        self.submit = tk.Button(self, bg="black", fg="white", text="Vote",
                            command=lambda: Candidates.Voting(self))
        self.submit.place(x=250, y=450)

    def Voting(self):
        last_1_txt = getattr(self,"entry_Vote1")
        last_1 = last_1_txt.get()
        last_2_txt = getattr(self,"entry_Vote2")
        last_2 = last_2_txt.get()
        last_3_txt = getattr(self,"entry_Vote3")
        last_3 = last_3_txt.get()
        last_4_txt = getattr(self,"entry_Vote4")
        last_4 = last_4_txt.get()

        if last_1 == last_2 or last_1 == last_3 or last_1 == last_4 or last_2 == last_3 or last_2 == last_4 or last_3 == last_4:
            tm.showerror("Voting Error", "No duplicate voting allowed")
            self.entry_Vote1.delete(0, END)
            self.entry_Vote2.delete(0, END)
            self.entry_Vote3.delete(0, END)
            self.entry_Vote4.delete(0, END)
        else :
            tm.showinfo("Vote", "Voting Sucessfull")
            self.entry_Vote1.delete(0, END)
            self.entry_Vote2.delete(0, END)
            self.entry_Vote3.delete(0, END)
            self.entry_Vote4.delete(0, END)

            votes_1 = conn.execute("SELECT Vote_1  from Gsu_Candidates WHERE Last_name =:Last_name",
                                   {'Last_name': last_1})
            for row in votes_1.fetchall():
                actual_votes = row[0]
                New_vote_1 = actual_votes + 1

            votes_2 = conn.execute("SELECT Vote_2 from Gsu_Candidates WHERE Last_name =:Last_name",
                                   {'Last_name': last_2})
            for row in votes_2.fetchall():
                actual_votes = row[0]
                New_vote_2 = actual_votes + 1

            votes_3 = conn.execute("SELECT Vote_3 from Gsu_Candidates WHERE Last_name =:Last_name",
                                   {'Last_name': last_3})
            for row in votes_3.fetchall():
                actual_votes = row[0]
                New_vote_3 = actual_votes + 1

            votes_4 = conn.execute("SELECT Vote_4 from Gsu_Candidates WHERE Last_name =:Last_name",
                                   {'Last_name': last_4})
            for row in votes_4.fetchall():
                actual_votes = row[0]
                New_vote_4 = actual_votes + 1

            conn.execute("UPDATE Gsu_Candidates SET Vote_1 =:New_vote_1  WHERE Last_name =:Last_name",
                         {"New_vote_1": New_vote_1, "Last_name": last_1})

            conn.execute("UPDATE Gsu_Candidates SET Vote_2 =:New_vote_2  WHERE Last_name =:Last_name",
                         {"New_vote_2": New_vote_2, "Last_name": last_2})

            conn.execute("UPDATE Gsu_Candidates SET Vote_3 =:New_vote_3  WHERE Last_name =:Last_name",
                         {"New_vote_3": New_vote_3, "Last_name": last_3})

            conn.execute("UPDATE Gsu_Candidates SET Vote_4 =:New_vote_4  WHERE Last_name =:Last_name",
                         {"New_vote_4": New_vote_4, "Last_name": last_4})

            conn.commit()
