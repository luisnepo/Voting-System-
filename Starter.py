from tkinter import *
import tkinter as tk
# defines the StartWindow where the user can select if he wants to vote or to check the results of the election.
# Done by Luis Nepomuceno lg6598x
class StartWindow(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.Header = Label(self,text = "Voting menu",width = 25,font= ("bold",20))
        self.Header.place (x=35,y=40)
        self.vote = Button(self,text ="Vote",width = 20,bg ="black",fg = "white",
                           command=lambda: self.vote_clicked(controller)).place(x = 160,y = 150)
        self.vote = Button(self, text="Show Results", width=20, bg="black", fg="white",
                           command=lambda: self.results_clicked(controller)).place(x=160, y=200)

#Shows the voting Window
    def vote_clicked(self,controller):
        controller.show_window("VoteWindow")
#Shows the Results window
    def results_clicked(self,controller):
        controller.show_window("ShowResults")


