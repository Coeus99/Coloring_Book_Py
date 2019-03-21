import pickle
from tkinter import Frame,Menu,filedialog
from Wall import Wall
from Route import Route
from Hold import Hold
from RouteWindow import RouteWindow

class ColoringBook(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        master.title("Coloring Book Plus")

        #initialize walls
        self.leftwall = Wall("walls/left_wall_bolts.gif",self)
        self.rightwall = Wall("walls/right_wall_bolts.gif",self)
        self.leftwall.pack(fill="both",expand="yes",side="left")

        #route class to be worked on
        self.currentroute = Route()

        #key bindings
        master.bind("n",self.cycle_wall)
        master.bind("a",self.add_hold)
        master.bind("d",self.delete_hold)
        master.bind("<Control-s>",self.save_route_as)
        master.bind("<Control-o>",self.open_route)

        #main menubar
        self.init_mainmenubar()

        #route window
        self.route_window = RouteWindow(self)

    def cycle_wall(self,event):
        if(self.leftwall.winfo_ismapped()):
            self.leftwall.pack_forget()
            self.rightwall.pack(fill="both",expand="yes",side="left")
        else:
            self.rightwall.pack_forget()
            self.leftwall.pack(fill="both",expand="yes",side="left")

    def add_hold(self,event):
        newhold = Hold()
        self.currentroute.holds.append(newhold)
        if (self.leftwall.winfo_ismapped()):
            newhold.wall = "left"
            newhold.position[0] = int(self.leftwall.width/2)
            newhold.position[1] = int(self.leftwall.height/2)
            self.leftwall.draw_hold(newhold)
        else:
            newhold.wall = "right"
            newhold.position[0] = int(self.rightwall.width/2)
            newhold.position[1] = int(self.rightwall.height/2)
            self.rightwall.draw_hold(newhold)

    def delete_hold(self,event):
        #hold is removed from route in the nested calls
        if (self.leftwall.winfo_ismapped()):
            self.leftwall.delete_hold()
        else:
            self.rightwall.delete_hold()
    
    def save_route_as(self,event):
        outfile = filedialog.asksaveasfile(parent=self,mode='wb',title="Save route as",initialdir="./routes",defaultextension=".route")
        if (outfile != None):
            pickle.dump(self.currentroute,outfile)

    def open_route(self,event):
        infile = filedialog.askopenfile(parent=self,mode='rb',title="Open route",initialdir="./routes",defaultextension=".route")
        if (infile != None):
            self.rightwall.clear()
            self.leftwall.clear()
            self.currentroute = pickle.load(infile)
            for hold in self.currentroute.holds:
                if (hold.wall == "left"):
                    self.leftwall.draw_hold(hold)
                elif (hold.wall == "right"):
                    self.rightwall.draw_hold(hold)

    def display_route_window(self,event):
        if (self.route_window.winfo_ismapped()):
            self.route_window.forget_pack()
        else:
            self.route_window.pack(side='right')

    def init_mainmenubar(self):
        mainmenubar = Menu(self.master)
        self.master.config(menu=mainmenubar)

        #file menu
        filemenu = Menu(mainmenubar)
        mainmenubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save As", command=lambda:self.save_route_as(None))
        filemenu.add_command(label="Open", command=lambda:self.open_route(None))

        editmenu = Menu(mainmenubar)
        editmenu.add_command(label="Add Hold", command=lambda:self.add_hold(None))
        mainmenubar.add_cascade(label = "Edit",menu=editmenu)

        windowmenu = Menu(mainmenubar)
        windowmenu.add_command(label="Route", command=lambda:self.display_route_window(None))
        mainmenubar.add_cascade(label = "Window",menu=windowmenu)

        viewmenu = Menu(mainmenubar)
        viewmenu.add_command(label="Cycle Wall", command=lambda:self.cycle_wall(None))
        mainmenubar.add_cascade(label = "View",menu=viewmenu)


