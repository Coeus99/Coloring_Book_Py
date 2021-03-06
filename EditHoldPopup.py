from tkinter import Toplevel,Message,Button,Label,Entry,filedialog
from tkinter.colorchooser import askcolor
from utilities import get_hold_imagetk

class EditHoldPopup(Toplevel):
    def __init__(self,hold,master):
        Toplevel.__init__(self)
        self.master = master
        self.title("Edit hold")

        self.modified = False
        self.originalhold = hold
        self.modifiedhold = hold

        #hold image
        hold_img = get_hold_imagetk(hold)
        self.hold_label = Label(self, image=hold_img)
        self.hold_label.grid(row=0,column=0,rowspan=2,columnspan=2)

        #options
        hold_browse_button = Button(self, text="Browse Models", command=self.on_browse)
        hold_browse_button.grid(row=0,column=2)
        color_button = Button(self, text="Change Color", command=self.on_color)
        color_button.grid(row=1,column=2)

        x_text = Message(self, text="x")
        x_text.grid(row=3,column=0)
        self.xentry = Entry(self)
        self.xentry.insert(0,hold.position[0])
        self.xentry.grid(row=4,column=0)
        self.yentry = Entry(self)
        y_text = Message(self, text="y")
        y_text.grid(row=3,column=1)
        self.yentry.grid(row=4,column=1)
        self.yentry.insert(0,hold.position[1])
        self.rentry = Entry(self)
        r_text = Message(self, text="r")
        r_text.grid(row=3,column=2)
        self.rentry.insert(0,hold.position[2])
        self.rentry.grid(row=4,column=2)

        xscale_text = Message(self, text="x-scale")
        xscale_text.grid(row=5,column=0)
        self.xscale_entry = Entry(self)
        self.xscale_entry.insert(0,hold.xscale)
        self.xscale_entry.grid(row=6,column=0)
        yscale_text = Message(self, text="y_scale")
        yscale_text.grid(row=5,column=1)
        self.yscale_entry = Entry(self)
        self.yscale_entry.insert(0,hold.yscale)
        self.yscale_entry.grid(row=6,column=1)

        cancel_button = Button(self, text="Cancel", command=self.on_cancel)
        cancel_button.grid(row=7,column=0)
        ok_button = Button(self, text="Ok", command=self.on_ok)
        ok_button.grid(row=7,column=1)

    def show(self):
        self.transient(self.master)
        self.wait_visibility()
        self.grab_set()
        self.master.wait_window(self)
        if (self.modified):
            return self.modifiedhold
        else:
            return None

    def update_hold_img(self):
        self.hold_label.configure(image=get_hold_imagetk(self.modifiedhold))
        self.hold_label.update()

    def on_browse(self):
        directory = filedialog.askopenfilename(parent=self,title="Open hold image",initialdir="./holds",defaultextension=".gif")
        if directory != ():
            self.modified = True
            self.modifiedhold.modelpath = directory
            self.update_hold_img()

    def on_color(self):
        color = askcolor()
        if color != (None, None):
            self.modified = True
            color = color[0]
            colorlist = []
            for x in color:
                colorlist.append(int(x))
            self.modifiedhold.RGB = colorlist
            self.update_hold_img()

    def check_positional_changes(self):
        newposition = []
        newposition.append(int(self.xentry.get()))
        newposition.append(int(self.yentry.get()))
        newposition.append(int(self.rentry.get()))
        newxscale=float(self.xscale_entry.get())
        newyscale=float(self.yscale_entry.get())
        if (newposition != self.originalhold.position):
            self.modifiedhold.position = newposition
            self.modified = True
        if(newxscale != self.originalhold.xscale):
            self.modifiedhold.xscale = newxscale
            self.modified = True
        if(newyscale != self.originalhold.yscale):
            self.modifiedhold.yscale = newyscale
            self.modified = True


    def on_ok(self):
        self.check_positional_changes()
        self.destroy()

    def on_cancel(self):
        self.modified = False
        self.destroy()
