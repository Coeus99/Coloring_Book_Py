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
        pixel = list(pixel)
        brightness = (pixel[0] + pixel[1] + pixel[2])/765
        #brightness = 0 : black : 0,0,0
        #brightness = 1 : color : r,g,b
        pixel[0] = int(hold.RGB[0] * brightness)
        pixel[1] = int(hold.RGB[1] * brightness)
        pixel[2] = int(hold.RGB[2] * brightness)
        recoloredimgdata.append(tuple(pixel))

    recoloredimg.putdata(recoloredimgdata)
    imgtk = ImageTk.PhotoImage(recoloredimg)
    label = Label(image=imgtk)
    label.image = imgtk #keep a reference so PhotoImage object doesn't get garbage collected
    return imgtk
