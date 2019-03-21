from tkinter import Frame,Entry,Button

class RouteWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master

        #basic window formatting
        self.borderwidth = 10

        #title of window

        #route name,grade
        #grade with - on left + on right

        #holds

        #tags

        #add a tag
        self.tag_entry = Entry(self)
        self.tag_entry.insert(0,"Enter tag here.")
        self.tag_entry.grid(row=0,column=0)
        self.tag_button = Button(self,text="Add Tag",command=self.add_tag)
        self.tag_entry.grid(row=0,column=1)

    def add_tag():
        tag = self.tag_entry.get()
        if ((tag!="Enter new tag here.")and(tag!="")and(tag not in self.master.currentroute.tags)):
            self.master.currentroute.tags.append(tag)
