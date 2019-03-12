from PIL import Image,ImageTk

class Hold:
    def __init__(self):
        self.modelpath = "holds/default.gif"
        self.wall = "left"
        self.position = [0,0,0]
        self.RGBA = [0,0,0,255]
    
    def get_imagetk(self,scale=1.0):
        img = Image.open(self.modelpath)
        scaledsize = int(img.width*scale),int(img.height*scale)
        scaledimg = img.resize(scaledsize)
        rotatedimg = (scaledimg.convert("RGBA")).rotate(self.position[2],expand=True)
        recoloredimgdata = []
        recoloredimg = Image.new("RGBA",rotatedimg.size)
        for pixel in rotatedimg.getdata():
            if pixel == (255,255,255,255):
                recoloredimgdata.append(tuple(self.RGBA))
            else:
                recoloredimgdata.append(pixel)
        recoloredimg.putdata(recoloredimgdata)
        self.imgtk = ImageTk.PhotoImage(recoloredimg)
        return self.imgtk
