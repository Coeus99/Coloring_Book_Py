import pickle
from tkinter import Frame,filedialog
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

        #route class to be worked on
        self.newroute = Route()

        #key bindings
        master.bind("n",self.cycle_wall)
        master.bind("a",self.add_hold)
        master.bind("<Control-s>",self.save_route_as)
        master.bind("<Control-o>",self.open_route)

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
    
    def save_route_as(self,event):
        #copy holds in wall dicts into route class
        leftwallholds = list(self.leftwall.holddict)
        rightwallholds = list(self.rightwall.holddict)
        for holdid in leftwallholds:
            self.newroute.holds.append(self.leftwall.holddict[holdid])
        for holdid in rightwallholds:
            self.newroute.holds.append(self.rightwall.holddict[holdid])
        #dump object to file
        outfile = filedialog.asksaveasfile(parent=self,mode='wb',title="Save route as")
        pickle.dump(self.newroute,outfile)

    def open_route(self,event):
        #clear current route
        self.leftwall.clear()
        self.rightwall.clear()
        #read in route
        with open("temp.route", "rb") as infile:
            self.newroute = pickle.load(infile)
        #draw route on walls
        for hold in self.newroute.holds:
            if (hold.wall == "left"):
                self.leftwall.draw_hold(hold)
            elif (hold.wall == "right"):
                self.rightwall.draw_hold(hold)

        
