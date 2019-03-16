from tkinter import Canvas,Widget
from PIL import Image,ImageTk
from Hold import Hold
from EditHoldPopup import EditHoldPopup
import utilities

class Wall(Canvas):
    def __init__(self,wallpath,master):
        Canvas.__init__(self)
        self.master = master
        self.wallpath = wallpath

        #event bindings
        self.bind("<Configure>",self.on_resize)
        self.bind("<Double-Button-1>",self.on_double_button_1)

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
        #TODO
        #only moves doesn't scale *yet*
        for holdid in list(self.holddict):
            prevx,prevy = self.coords(holdid)
            xoffset = prevx * hscale - prevx
            yoffset = prevy * hscale - prevy
            self.move(holdid,xoffset,yoffset)

    def clear(self):
        self.delete("hold")

    def draw_hold(self,hold):
        x = hold.position[0] * self.totalscale
        y = hold.position[1] * self.totalscale
        img = utilities.get_hold_imagetk(hold,self.totalscale)
        holdid = self.create_image(x,y,anchor="nw",image=img,tags="hold")
        self.holddict[holdid]=hold
        #moveable
        Widget.bind(self, "<1>", self.mouse_down)
        Widget.bind(self, "<B1-Motion>", self.mouse_move)

    def delete_hold(self):
        currentitemid=self.find_withtag('current')[0]
        if(currentitemid !=self.wallimgid):
            self.delete(self.holddict[currentitemid])
            del self.holddict[currentitemid]
            self.delete(currentitemid)

    def mouse_down(self,event):
        self.lastx = event.x
        self.lasty = event.y

    def mouse_move(self,event):
        currentitemid = self.find_withtag("current")[0]
        if (currentitemid != self.wallimgid):
            self.move("current",event.x-self.lastx,event.y-self.lasty)
            self.holddict[currentitemid].position[0] = int(event.x / self.totalscale)
            self.holddict[currentitemid].position[1] = int(event.y / self.totalscale)
            self.lastx = event.x
            self.lasty = event.y

    def on_double_button_1(self,event):
        currentitemid = self.find_withtag("current")[0]
        if (currentitemid != self.wallimgid):
            edditedhold = EditHoldPopup(self.holddict[currentitemid],self).show()
            if (edditedhold != None):
                self.delete(currentitemid)
                self.delete(self.holddict[currentitemid])
                del self.holddict[currentitemid]
                self.draw_hold(edditedhold)

