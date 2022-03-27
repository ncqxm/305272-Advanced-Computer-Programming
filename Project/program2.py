import tkinter as tk
from tkinter import* 
from PIL import Image, ImageTk
from tkinter import Canvas, PhotoImage
import random
import webbrowser

def sum2():
    noodlelist=["ก๋วยเตี๋ยวน้ำใส","ก๋วยเตี๋ยวน้ำตก","ก๋วยเตี๋ยวเรือ","ก๋วยเตี๋ยวต้มยำน้ำข้น/ใส","ก๋วยเตี๋ยวต้มยำแห้ง",
                "เย็นตาโฟ","ราดหน้า","ก๋วยเตี๋ยวคั่วไก่","เกี๊ยวน้ำ","ข้าวซอย","สุกี้น้ำ","สุกี้แห้ง",
                "ก๋วยจั๊บ"]#ลิสต์ก๋วยเตี๋ยว

    caldict = {"ก๋วยเตี๋ยวน้ำใส":147,
            "ก๋วยเตี๋ยวน้ำตก":462,
            "ก๋วยเตี๋ยวเรือ":180,
            "ก๋วยเตี๋ยวต้มยำน้ำข้น/ใส":335,
            "ก๋วยเตี๋ยวต้มยำแห้ง":310,
            "เย็นตาโฟ":420,
            "ราดหน้า":690,
            "ก๋วยเตี๋ยวคั่วไก่":435,
            "เกี๊ยวน้ำ":275,
            "ข้าวซอย":395,
            "สุกี้น้ำ":345,
            "สุกี้แห้ง":350,
            "ก๋วยจั๊บ":240}

    linkdict = {"ก๋วยเตี๋ยวน้ำใส":"https://www.wongnai.com/recipes/ugc/6c273742a82a4d588d5a610113a62bf9",
            "ก๋วยเตี๋ยวน้ำตก":"https://cooking.kapook.com/view117325.html",
            "ก๋วยเตี๋ยวเรือ":"https://www.wongnai.com/recipes/boat-noodle",
            "ก๋วยเตี๋ยวต้มยำน้ำข้น/ใส":"https://www.wongnai.com/recipes/tom-yum-noodle",
            "ก๋วยเตี๋ยวต้มยำแห้ง":"https://cookpad.com/th/recipes/9052448-%E0%B8%81%E0%B8%A7%E0%B8%A2%E0%B9%80%E0%B8%95%E0%B8%A2%E0%B8%A7%E0%B9%81%E0%B8%AB%E0%B8%87%E0%B8%95%E0%B8%A1%E0%B8%A2%E0%B8%B3%E0%B9%82%E0%B8%9A%E0%B8%A3%E0%B8%B2%E0%B8%93",
            "เย็นตาโฟ":"https://www.wongnai.com/recipes/yen-ta-four",
            "ราดหน้า":"https://www.wongnai.com/recipes/thai-noodle-with-pork-in-gravy",
            "ก๋วยเตี๋ยวคั่วไก่":"https://www.happyfresh.co.th/blog/recipe/stir-fried-noodles-with-chicken/",
            "เกี๊ยวน้ำ":"https://www.wongnai.com/recipes/dumpling-soup",
            "ข้าวซอย":"https://www.wongnai.com/recipes/northern-thai-curried-noodles-soup",
            "สุกี้น้ำ":"https://www.wongnai.com/recipes/homemade-sukiyaki",
            "สุกี้แห้ง":"https://www.wongnai.com/recipes/ugc/47161c946e194a3d82defc69589cf035",
            "ก๋วยจั๊บ":"https://www.wongnai.com/recipes/chinese-roll-noodle-soup"}

    pricedict = {"ก๋วยเตี๋ยวน้ำใส":35,
            "ก๋วยเตี๋ยวน้ำตก":40,
            "ก๋วยเตี๋ยวเรือ":40,
            "ก๋วยเตี๋ยวต้มยำน้ำข้น/ใส":40,
            "ก๋วยเตี๋ยวต้มยำแห้ง":40,
            "เย็นตาโฟ":40,
            "ราดหน้า":40,
            "ก๋วยเตี๋ยวคั่วไก่":45,
            "เกี๊ยวน้ำ":45,
            "ข้าวซอย":45,
            "สุกี้น้ำ":40,
            "สุกี้แห้ง":40,
            "ก๋วยจั๊บ":35}

    immagedict ={"ก๋วยเตี๋ยวน้ำใส":"น้ำใส.jpg",
            "ก๋วยเตี๋ยวน้ำตก":"น้ำตก.jpeg",
            "ก๋วยเตี๋ยวเรือ":"เรือ.jpg",
            "ก๋วยเตี๋ยวต้มยำน้ำข้น/ใส":"ต้มยำน้ำข้น.jpg",
            "ก๋วยเตี๋ยวต้มยำแห้ง":"ต้มยำแห้ง.jpg",
            "เย็นตาโฟ":"เย็นตาโฟ.jpg",
            "ราดหน้า":"ราดหน้า.jpg",
            "ก๋วยเตี๋ยวคั่วไก่":"คั่วไก่.jpg",
            "เกี๊ยวน้ำ":"เกี๊ยวน้ำ.jpg",
            "ข้าวซอย":"ช้าวซอย.jpg",
            "สุกี้น้ำ":"สุกี้น้ำ.jpg",
            "สุกี้แห้ง":"สุกี้แห้ง.jpg",
            "ก๋วยจั๊บ":"ก๋วยจั๊บ.jpg"}

    menu = random.choice(noodlelist)#โค้ดที่เป็นตัวสุ่ม เวลาจะสุ่มอีกครั้งสามารถกลับมาที่โค้ดนี้ได้เลย
    cal = caldict[menu]#ดึงค่าแคลลอลี่จากดิจ
    link = linkdict[menu]#ดึงลิงค์จากดิจ
    price = pricedict[menu]#ดึงราคาจากดิจราคา
    immage= immagedict[menu]#ดึงชื่อรูปจากดิจ

    def callback(url):
        webbrowser.open_new(url)


    window = tk.Toplevel()
    window.geometry("600x800")
    window.minsize(600, 800)
    window.maxsize(600, 800)
    window.title("วันนี้กินไรดี?")
    window.configure(bg="#54A2A4")

    frame1 = tk.Frame(master = window)
    label1 = tk.Label(master = frame1, text="Frame 1", width=100, height=100)

    bg3 = Image.open("D:\\งาน\\comproglab\\วันนี้กินไรดี กลุ่ม 14\\Project\\draft_p3_bg.jpg")
    bg3 = bg3.resize((600,800), Image.ANTIALIAS)
    label_bg3 = ImageTk.PhotoImage(bg3)
    labelbg3 = tk.Label(master = frame1 ,image=label_bg3)
    labelbg3.place(x=-2,y=0)

    frame1.pack()
    label1.pack()

    #pic of food
    label_2 = tk.Label(master = frame1, text="Frame 1", width=100, height=100)
    bg = Image.open(immage)
    bg = bg.resize((300,230), Image.ANTIALIAS)
    label_bg = ImageTk.PhotoImage(bg)
    label7 = tk.Label(master = frame1,image=label_bg)
    label7.place(x=152, y=205)

    label_2.pack()


    label = tk.Label(master = window,text = menu,font="Ayuthaya 30",width=10,height=1,fg="white",bg="#FCAF38")
    label1 = tk.Label(master = window,text = str(price) + " บาท",font="Ayuthaya 20",width=13,height=3,fg="white",bg="#674A40")
    label2 = tk.Label(master = window,text = str(cal) + " แคลอรี",font="Ayuthaya 20",width=13,height=3,fg="white",bg="#674A40")
    Button3 = tk.Button(master = window,text = "วิธีทำ",font="Ayuthaya 20",width=12,height=1)
    Button4 = tk.Button(master = window,text = "สุ่มอีกครั้ง",font="Ayuthaya 18",width=10,height=1,fg="white", bg="#F95335", command = window.destroy)

    Button3.bind("<Button-1>",lambda e: callback(link))

    label.place(x=200,y=60)
    label1.place(x=60,y=490)
    label2.place(x=340,y=490)
    Button3.place(x=205,y=640)
    Button4.place(x=410,y=725)
       
           
    window.mainloop()
