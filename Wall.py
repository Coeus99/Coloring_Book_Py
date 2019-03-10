from tkinter import Canvas
from PIL import ImageTk, Image

class Wall(Canvas):
    def __init__(self,wallpath,master):
        Canvas.__init__(self)
        self.master = master
        self.wallpath = wallpath

        #set wall image
        self.wallimg = Image.open(wallpath)
        self.wallimgtk = ImageTk.PhotoImage(self.wallimg)
        self.config(width=self.wallimg.width,height=self.wallimg.height)
        self.wallimgid = self.create_image(0,0,image=self.wallimgtk,anchor="nw")
