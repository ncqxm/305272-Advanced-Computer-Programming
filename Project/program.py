import tkinter as tk
from tkinter import*
from typing import Sized
from PIL import Image, ImageTk
from program1 import sum1
from program2 import sum2
from program3 import sum3
from program4 import sum4
from tkinter import Canvas, PhotoImage
import random

def randomlist():
    window = tk.Toplevel()
    window.geometry("600x800")
    window.minsize(600, 800)
    window.maxsize(600, 800)
    window.title("วันนี้กินไรดี?")
    window.configure(bg="#54A2A4")

    frame1 = tk.Frame(master = window)
    label1 = tk.Label(master = frame1, text="Frame 1", width=100, height=100)
    bg = Image.open("D:\\งาน\\comproglab\\วันนี้กินไรดี กลุ่ม 14\\Project\draft_p1_1.jpg") 
    bg = bg.resize((600,800),Image.ANTIALIAS)
    label_bg = ImageTk.PhotoImage(bg)

    label = tk.Label(master= frame1 ,image=label_bg)
    label.place(x=-2,y=0)


    frame1.pack()
    label1.pack()


    Button1 = tk.Button(master = window,text = "ข้าว",font="Ayuthaya 40",width=7,height=2,foreground="white",background="#F95335",command=sum1)
    Button2 = tk.Button(master = window,text = "ก๋วยเตี๋ยว",font="Ayuthaya 40",width=7,height=2,foreground="white",background="#F95335",command=sum2)
    Button3 = tk.Button(master = window,text = "อื่นๆ",font="Ayuthaya 40",width=7,height=2,foreground="white",background="#F95335",command=sum3)
    Button4 = tk.Button(master = window,text = "สุ่มทั้งหมด",font="Ayuthaya 40",width=7,height=2,foreground="white",background="#F95335",command=sum4)

    Button1.place(x=45,y=360)
    Button2.place(x=330,y=360)
    Button3.place(x=45,y=550)
    Button4.place(x=330,y=550)

    window.mainloop()
