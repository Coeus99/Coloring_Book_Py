from tkinter import Canvas,Widget
from PIL import Image,ImageTk
from Hold import Hold

class Wall(Canvas):
    def __init__(self,wallpath,master):
        Canvas.__init__(self)
        self.master = master
        self.wallpath = wallpath

        #event bindings
        self.bind("<Configure>",self.on_resize)

        #set wall image
        self.wallimg = Image.open(wallpath)
        self.wallimgtk = ImageTk.PhotoImage(self.wallimg)
        self.wallimgid = self.create_image(0,0,image=self.wallimgtk,anchor="nw")

        #get dimensions
        self.width = self.wallimg.width
        self.height = self.wallimg.height
        self.config(width=self.width,height=self.height)

        #keep track of holds on wall
        self.holddict = {}

    def on_resize(self,event):
        #scale canvas
        hscale = float(event.height)/self.height
        self.totalscale = float(event.height)/self.wallimg.height
        self.height = event.height
        self.width = int(self.width*hscale)
        self.config(width=self.width,height=self.height)
        #scale background
        if(self.wallimgid):
            self.delete(self.wallimgid)
        newsize = int(self.width),int(self.height)
        resizedimg = self.wallimg.resize(newsize)
        self.wallimgtk = ImageTk.PhotoImage(resizedimg)
        self.wallimgid = self.create_image(0,0,image=self.wallimgtk,anchor="nw")
        self.tag_lower(self.wallimgid)
        #scale holds
        for holdid in list(self.holddict):
            prevx,prevy = self.coords(holdid)
            xoffset = prevx * hscale - prevx
            yoffset = prevy * hscale - prevy
            self.move(holdid,xoffset,yoffset)

    def draw_hold(self,hold):
        x = hold.position[0] * self.totalscale
        y = hold.position[1] * self.totalscale
        img = hold.get_imagetk(self.totalscale)
        holdid = self.create_image(x,y,anchor="nw",image=img)
        #NOTE
        #this next line creates a new object... so how will I modify the original when I move it?
        #when saving the route do I have to just run through the dictionaries again?
        #or can I use something similar to a C pointer in the dictionary instead?
        self.holddict[holdid]=hold
        #moveable
        Widget.bind(self, "<1>", self.mouse_down)
        Widget.bind(self, "<B1-Motion>", self.mouse_move)

    def mouse_down(self,event):
        self.lastx = event.x
        self.lasty = event.y

    def mouse_move(self,event):
        currentitemid = self.find_withtag("current")[0]
        if (currentitemid != self.wallimgid):
            self.move("current",event.x-self.lastx,event.y-self.lasty)
            self.holddict[currentitemid].position[0] = int(event.x / self.totalscale)
            self.holddict[currentitemid].position[1] = int(event.y / self.totalscale)
            #here is where I need to update the route if I do not do it while saving the route (saving the route now seems like a better option
        self.lastx = event.x
        self.lasty = event.y

