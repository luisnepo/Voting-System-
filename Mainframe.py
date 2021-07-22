#importing tkinter to build the GUI and the classes defined on Starter,loginwindow,Voting,Show_resutls
import tkinter as tk
from Starter import StartWindow
from loginwindow import LoginWindow
from Voting import VoteWindow
from Show_Results import ShowResults
# Done by Luis Nepomuceno lg6598x
# Main class,defines the blueprint for all the windows within the system.
class MainFrame(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.title("Main menu")
        self.geometry("500x500")

        window = tk.Frame(self)
        window.pack(side = "top", fill = "both", expand = True)
        window.grid_rowconfigure(0,weight =1)
        window.grid_columnconfigure(0,weight =1)

        self.frames = {}
        avaiable_frames = (StartWindow,LoginWindow,VoteWindow,ShowResults)
        for i in avaiable_frames:
            page_name = i.__name__
            frame = i(parent = window,controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0,column = 0,sticky = "nsew")
        self.show_window("LoginWindow")
#defines which frame is going to appear on the screen.
    def show_window(self, window_name):
        frame = self.frames[window_name]
        frame.tkraise()


exe = MainFrame()
exe.mainloop()