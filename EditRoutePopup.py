from tkinter import Toplevel,Entry,Button,Listbox,Message

class EditRoutePopup(Toplevel):
    def __init__(self,master):
        Toplevel.__init__(self,master)
        self.master = master

        #get reference to working route
        self.currentroute = master.currentroute

        #title of window

        #route name
        self.name_entry = Entry(self)
        self.name_entry.insert(0,self.currentroute.name)
        self.name_entry.grid(row=0,column=1)

        #grade with - on left + on right
        self.grade_message = Message(self,text=self.currentroute.grade[0]+str(self.currentroute.grade[1])+self.currentroute.grade[2])
        self.grade_message.grid(row=1,column=1)
        self.gradeplus_buttonbutton = Button(self,text="+",command=self.on_gradeplus)
        self.gradeplus_buttonbutton.grid(row=1,column=2)
        self.grademinus_buttonbutton = Button(self,text="-",command=self.on_grademinus)
        self.grademinus_buttonbutton.grid(row=1,column=0)

        #holds

        #tags
        self.taglist = Listbox(self)
        self.taglist.insert('end', "Tags:")
        for tag in self.currentroute.tags:
            self.taglist.insert('end',tag)
        self.taglist.grid(row=2,column=0,columnspan=3)

        #add a tag
        self.tag_entry = Entry(self)
        self.tag_entry.insert(0,"Enter tag here.")
        self.tag_entry.grid(row=3,column=0)
        self.add_tag_button = Button(self,text="Add Tag",command=self.add_tag)
        self.add_tag_button.grid(row=3,column=1)
        self.rem_tag_button = Button(self,text="Remove Tag",command=self.rem_tag)
        self.rem_tag_button.grid(row=3,column=2)

        #cancel and ok
        cancel_button = Button(self, text="Cancel", command = self.on_cancel)
        cancel_button.grid(row=4,column=2)
        ok_button = Button(self, text="Ok", command=self.on_ok)
        ok_button.grid(row=4,column=3)

    def show(self):
        self.transient(self.master)
        self.wait_visibility()
        self.grab_set()
        self.master.wait_window(self)

    def add_tag(self):
        tag = self.tag_entry.get()
        if ((tag!="Enter tag here.")and(tag!="")and(tag not in self.currentroute.tags)):
            self.currentroute.tags.append(tag)
            self.taglist.insert('end',tag)

    def rem_tag(self):
        tag = self.tag_entry.get()
        if (tag in self.currentroute.tags):
            self.currentroute.tags.remove(tag)
            self.refresh_tags()

    def refresh_tags(self):
        self.taglist.delete(1,'end')
        for tag in self.currentroute.tags:
            self.taglist.insert('end',tag)

    def on_gradeplus(self):
        numgrade = self.currentroute.grade[1]
        tempgrade = list(self.currentroute.grade)
        if (numgrade < 16):
            tempgrade[1] = numgrade + 1
            self.currentroute.grade = tuple(tempgrade)
            self.grade_message.configure(text=tempgrade[0]+str(tempgrade[1])+tempgrade[2])
            
    def on_grademinus(self):
        numgrade = self.currentroute.grade[1]
        tempgrade = list(self.currentroute.grade)
        if (numgrade > 0 ):
            tempgrade[1] = numgrade - 1
            self.currentroute.grade = tuple(tempgrade)
            self.grade_message.configure(text=tempgrade[0]+str(tempgrade[1])+tempgrade[2])

    def on_cancel(self):
        self.destroy()

    def on_ok(self):
        routename = self.name_entry.get()
        self.currentroute.name = routename
        self.destroy()
