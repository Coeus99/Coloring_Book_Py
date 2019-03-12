from tkinter import Frame
from Wall import Wall
from Route import Route
from Hold import Hold

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

        #start a new route
        self.newroute = Route()

        #key bindings
        master.bind("n",self.cycle_wall)
        master.bind("a",self.add_hold)

    def cycle_wall(self,event):
        if(self.leftwallseen):
            self.leftwall.pack_forget()
            self.rightwall.pack(fill="both",expand="yes",side="left")
            self.leftwallseen = False
        else:
            self.rightwall.pack_forget()
            self.leftwall.pack(fill="both",expand="yes",side="left")
            self.leftwallseen = True

    def add_hold(self,event):
        newhold = Hold()
        if (self.leftwallseen):
            newhold.wall = "left"
            self.leftwall.draw_hold(newhold)
        else:
            newhold.wall = "right"
            self.rightwall.draw_hold(newhold)
        self.newroute.holds.append(newhold)
