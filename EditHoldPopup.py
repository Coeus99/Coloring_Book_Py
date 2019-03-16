from tkinter import Toplevel, Message, Button
from tkinter.colorchooser import askcolor
from utilities import get_hold_imagetk

class EditHoldPopup(Toplevel):
    def __init__(self,hold,master):
        Toplevel.__init__(self)
        self.master = master
        self.title("Edit hold")

        self.newhold = None

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
        hold_text.pack()

        color_text = Message(self, text="Color")
        color_text.pack()

        position_text = Message(self, text="Position")
        position_text.pack()

        cancel_button = Button(self, text="Cancel", command=self.destroy)
        cancel_button.pack()
        ok_button = Button(self, text="Ok", command=self.on_ok)
        ok_button.pack()

    def show(self):
        self.transient(self.master)
        self.wait_visibility()
        self.grab_set()
        self.master.wait_window(self)
        return self.newhold

    def ok(self):
        #newhold=...something not None
        self.destroy()
