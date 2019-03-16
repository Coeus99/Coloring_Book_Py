from tkinter import Toplevel
from tkinter.colorchooser import askcolor
from utilities import get_hold_imagetk

class EditHoldPopup(Toplevel):
    def __init__(self,hold,master):
        Toplevel.__init__(self)
        self.master = master
        self.title("Edit hold")
        
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

        
