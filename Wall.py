from tkinter import Canvas
from PIL import ImageTk, Image

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

    def on_resize(self,event):
        #scale canvas
        hscale = float(event.height)/self.height
        self.height = event.height
        self.width = int(self.width*hscale)
        self.config(width=self.width,height=self.height)
        self.scale("all",0,0,hscale,hscale)
        #scale background
        if(self.wallimgid):
            self.delete(self.wallimgid)
        newsize = int(self.width),int(self.height)
        resizedimg = self.wallimg.resize(newsize)
        self.wallimgtk = ImageTk.PhotoImage(resizedimg)
        self.wallimgid = self.create_image(0,0,image=self.wallimgtk,anchor="nw")