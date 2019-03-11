from tkinter import Frame
from Wall import Wall
from Route import Route

class ColoringBook(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master
        master.title("Coloring Book Plus")

        #initialize walls
        self.leftwall = Wall("walls/left_wall_bolts.gif",self)
        self.rightwall = Wall("walls/right_wall_bolts.gif",self)
        self.leftwall.pack(fill="both",expand="yes",side="left")
        self.leftwallseen = True 
        self.rightwallseen = False

        #start a new route
        newroute = Route()

        #key bindings
        master.bind("n",self.cycle_wall)

    def cycle_wall(self,event):
        if(self.leftwallseen):
            self.leftwall.pack_forget()
            self.rightwall.pack(fill="both",expand="yes",side="left")
            self.rightwallseen = True
            self.leftwallseen = False
        else:
            self.rightwall.pack_forget()
            self.leftwall.pack(fill="both",expand="yes",side="left")
            self.leftwallseen = True 
            self.rightwallseen = False
