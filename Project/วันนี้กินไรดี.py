import tkinter as tk
from typing import Text
from tkinter import *
from PIL import Image, ImageTk
from program import randomlist
from program1 import sum1
from program2 import sum2
from program3 import sum3
from program4 import sum4
import random


window = tk.Tk()
window.geometry("600x800")              # size of app
window.minsize(600, 800)
window.maxsize(600, 800)
window.title("วันนี้กินอะไรดี?")
# window.configure(bg ="#54A2A4")         # set background color

bg = Image.open("draf_p1_cf.jpg")
bg = bg.resize((600,800), Image.ANTIALIAS)
label_bg = ImageTk.PhotoImage(bg)
label = tk.Label(image=label_bg)
label.place( x=-2, y=0)

#explain
frame1 = tk.Frame(master = window, width = 40 ,height = 300 ,bg="white")


label1 = tk.Label(master=frame1, text="1.โปรแกรมนี้เป็นโปรแกรมที่อยู่ในช่วงทดลอง อาจจะเกิดปัญหาในการใช้งาน",bg="white",font="Ayuthaya 14")
label2 = tk.Label(master=frame1, text="2.วิธีการใช้งาน",bg="white",font="Ayuthaya 14")
label3 = tk.Label(master=frame1, text="  2.1 หลังจากกด เริ่ม โปรแกรมจะขึ้นหน้าต่างให้ผู้ใช้เลือกว่าต้องการจะสุ่มอาหารประเภทไหน",bg="white",font="Ayuthaya 14")
label4 = tk.Label(master=frame1, text="  2.2 หลังจากเลือกประเภทของอาหารแล้ว ถ้าต้องการสุ่มใหม่สามารถกดที่ปุ่มสุ่มอีกครั้งหรือปิดหน้าต่างได้เลย",bg="white",font="Ayuthaya 14")
label4_1 = tk.Label(master=frame1, text="         โปรแกรมจะกลีบไปที่หน้าเลือกประเภทอาหาร",bg="white",font="Ayuthaya 14")
label5 = tk.Label(master=frame1, text="  2.3 ถ้าต้องการทราบวิธีทำ คลิ๊กที่ วิธีทำ โปรแกรมจะลิ้งค์ขึ้นหน้าเว็บไซต์ให้อัตโนมัติ",bg="white",font="Ayuthaya 14")
label6 = tk.Label(master=frame1, text="3.ขอบคุณที่ร่วมทดลองใช้",bg="white",font="Ayuthaya 14")

frame1.place(x = 47 , y = 300)
label1.pack(anchor='w')
label2.pack(anchor='w')
label3.pack(anchor='w')
label4.pack(anchor='w')
label4_1.pack(anchor='w')
label5.pack(anchor='w')
label6.pack(anchor='w')

#create button that click to next page
bt = tk.Button(master = window, text="เริ่ม",width=10,height=1,font="Ayuthaya 20",bg="#FCAF38",command=randomlist)
bt.place(x = 220, y = 520)


window.mainloop()

