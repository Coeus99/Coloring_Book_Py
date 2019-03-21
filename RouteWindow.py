from tkinter import Frame,Entry,Button

class RouteWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master

        #title of window

        #route name,grade

        #holds

        #tags

        #add a tag
        self.tag_entry = Entry()
        self.tag_entry.insert(0,"Enter tag here.")
        self.tag_entry.pack()
        self.tag_button = Button(text="Add Tag",command=self.add_tag)
        self.tag_button.pack()

    def add_tag():
        tag = self.tag_entry.get()
        if ((tag!="Enter new tag here.")and(tag!="")and(tag not in self.master.currentroute.tags)):
            self.master.currentroute.tags.append(tag)
