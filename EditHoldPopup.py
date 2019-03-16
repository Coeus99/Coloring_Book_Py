from tkinter import Toplevel, Message, Button,Label,filedialog
from tkinter.colorchooser import askcolor
from utilities import get_hold_imagetk

class EditHoldPopup(Toplevel):
    def __init__(self,hold,master):
        Toplevel.__init__(self)
        self.master = master
        self.title("Edit hold")

        self.modified = False
        self.modifiedhold = hold

        #######################
        # hold         color  #
        #  i             c    #
        # new_i        new_c  #
        #                     #
        # pos                 #
        # xyzr                #
        #---------------------#
        #           cancel  ok#
        #######################

        hold_text = Message(self, text="Hold Model")
        hold_text.grid(row=0,column=0)
        hold_img = get_hold_imagetk(hold)
        self.hold_label = Label(self, image=hold_img)
        self.hold_label.grid(row=1,column=0)
        hold_browse_button = Button(self, text="Browse", command=self.on_browse)
        hold_browse_button.grid(row=2,column=0)

        color_text = Message(self, text="Color")
        color_text.grid(row=0,column=1)

        position_text = Message(self, text="Position")
        position_text.grid(row=3,column=0)

        cancel_button = Button(self, text="Cancel", command=self.on_cancel)
        cancel_button.grid(row=4,column=0)
        ok_button = Button(self, text="Ok", command=self.destroy)
        ok_button.grid(row=4,column=1)

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
        self.modified = True
        directory = filedialog.askopenfilename(parent=self,title="Open hold image",initialdir="./holds",defaultextension=".gif")
        self.modifiedhold.modelpath = directory
        self.update_hold_img()

    def on_cancel(self):
        self.modified = False
        self.destroy()
