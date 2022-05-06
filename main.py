from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog clock")
        self.root.geometry("640x480+400+20")
        self.root.config(bg="#02595b")
        self.root.resizable(0, 0)

        #clock title
        title = Label(self.root, text="SAEEF ANALOG CLOCK", font="exo 25 bold", bg="#038387", fg="#ffffff")
        title.place(x=0, y=0, width=640)

        #clock label
        self.label = Label(self.root, bg="#ffffff", bd=10, relief="raised")
        self.label.place(x=125, y=65, height=400, width=400)
        self.runClock()


    def clockImage(self, hr, mnt, sec):
        clock = Image.new("RGB", (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)
        #create clock image
        bgImg = Image.open("clock.jpg")
        bgImg = bgImg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bgImg, (50, 50))
        #use math
        origin = 200, 200
        #create hour line
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="black", width=4)
        #create minute line
        draw.line((origin, 200+70*sin(radians(mnt)), 200-70*cos(radians(mnt))), fill="green", width=3)
        #create second line
        draw.line((origin, 200+90*sin(radians(sec)), 200-90*cos(radians(sec))), fill="#ff00ff", width=2)
        #create circle
        draw.ellipse((192, 190, 210, 210), fill="#ff00ff")
        #save new image
        clock.save("newClock.png")

    def runClock(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        hr = (h/12)*360
        mnt = (m/60)*360
        sec = (s/60)*360

        self.clockImage(hr, mnt, sec)
        self.img = ImageTk.PhotoImage(file="newClock.png")
        self.label.config(image=self.img)
        self.label.after(200, self.runClock)

if __name__=="__main__":
    root = Tk()
    app = Clock(root)
    root.mainloop()
