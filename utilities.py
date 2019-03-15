from PIL import Image,ImageTk
from tkinter import Label

def get_hold_imagetk(hold,scale=1.0):
    img = Image.open(hold.modelpath)
    #scale image
    scaledsize = int(img.width*scale),int(img.height*scale)
    scaledimg = img.resize(scaledsize)
    #rotate image
    rotatedimg = (scaledimg.convert("RGBA")).rotate(hold.position[2],expand=True)
    #recolor image
    recoloredimg = Image.new("RGBA",rotatedimg.size)
    recoloredimgdata = []
    for pixel in rotatedimg.getdata():
        if pixel == (255,255,255,255):
            recoloredimgdata.append(tuple(hold.RGBA))
        else:
            recoloredimgdata.append(pixel)
    recoloredimg.putdata(recoloredimgdata)
    imgtk = ImageTk.PhotoImage(recoloredimg)
    label = Label(image=imgtk)
    label.image = imgtk #keep a reference so PhotoImage object doesn't get garbage collected
    return imgtk
