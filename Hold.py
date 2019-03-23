from PIL import Image,ImageTk

class Hold:
    def __init__(self):
        self.modelpath = "holds/default.gif"
        self.wall = "left"
        self.position = [0,0,0]
        self.RGB = [255,255,255]
