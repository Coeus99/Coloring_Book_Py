from tkinter import Canvas

class Wall(Cavnas):
    def __init__(self,wallpath,master):
        Canvas.__init__(self)
        self.master = master
        self.wallpath = wallpath

        #set wall image
        self.wallimg = Image.open(wallpath)
        self.wallimgtk = ImageTk.PhotoImage(self.wallimg)
        self.wallimgid = self.create_image(0,0,image=self.wallimgtk,anchor=NW)
