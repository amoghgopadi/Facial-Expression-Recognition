import sys
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import Image, ImageTk

window=Tk()
window.title("FER")

img = ImageTk.PhotoImage(Image.open("/home/riderasg/amogh/8th Sem/major project/project/final/content/editorial.jpeg"))
panel = tkinter.Label(window, image = img)
panel.place(relx = 0.5, rely = 1.08, anchor = S)


img1 = ImageTk.PhotoImage(Image.open("/home/riderasg/amogh/8th Sem/major project/project/final/content/logo.jpeg"))
panel1 = tkinter.Label(window, image = img1)
panel1.place(relx = 0.75, anchor = NE)


# add widgets here
def web_cam():
    os.system('python camera.py')

def image_loading():
    os.system('python photo.py')

def video_loading():
    os.system('python video.py')

btn=Button(window,text="Web Cam",fg='black',bg='green',padx=12,pady=12,width=10,font = ('Comic Sans MS',20,"bold"),command=web_cam)
#btn.place(x=400,y=175)
btn.place(x=220,y=300)

btn=Button(window,text="Image",fg='black',bg='green',padx=12,pady=12,width=10,font = ('Comic Sans MS',20,"bold"),command=image_loading)
#btn.place(x=750,y=175)
btn.place(x=420,y=300)
   
btn=Button(window,text="Video",fg='black',bg='green',padx=12,pady=12,width=10,font = ('Comic Sans MS',20,"bold"),command=video_loading)
#btn.place(x=400,y=250)
btn.place(x=620,y=300)

btn=Button(window,text="Exit",bg='green',padx=12,pady=12,width=10,font = ('Comic Sans MS',20,"bold"),command=window.destroy)
#btn.place(x=750,y=250)
btn.place(x=820,y=300)

window.geometry("1200x1000")

l = tkinter.Label(window,bg = "#C0C0C0", font=("Helvetica", 48,"bold"), fg = "black", height=1, text = "Facial Expression Recognition") 
l.place(relx = 0.48, rely = 0.30, anchor = N) 

window.configure(bg="#19547b")
window.mainloop()
