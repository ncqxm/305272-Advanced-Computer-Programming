import tkinter as tk
from tkinter import* 
from PIL import Image, ImageTk
from tkinter import Canvas, PhotoImage
import random
import webbrowser


def sum1():
    
    ricelist=["ข้าวกะเพราหมูกรอบ","ข้าวกะเพราหมูสับ","ข้าวกะเพราไก่","ข้าวกะเพรากุ้ง",
            "ข้าวหมูแดง","ข้าวหมูกระเทียม","ผัดผงกะหรี่","ผัดผักบุ้งไฟแดง","ข้าวไข่เจียวหมูสับ","ข้าวมันไก่",
            "ข้าวผัด","ข้าวผัดอเมริกัน","ข้าวผัดแหนม","ข้าวผัดปูใส่ไข่","ข้าวผัดกุ้งใส่ไข่","ข้าวผัดกุนเชียง",
            "ข้าวผัดปลาหมึกน้ำพริกเผา"]#ลิสต์ข้าว

    pricedict={"ข้าวกะเพราหมูกรอบ":35,
            "ข้าวกะเพราหมูสับ":25,
            "ข้าวกะเพราไก่":25,
            "ข้าวกะเพรากุ้ง":35,
            "ข้าวหมูแดง":25,
            "ข้าวหมูกระเทียม":25,
            "ผัดผงกะหรี่":40,
            "ผัดผักบุ้งไฟแดง":20,
            "ข้าวไข่เจียวหมูสับ":20,
            "ข้าวมันไก่":25,
            "ข้าวผัด":30,
            "ข้าวผัดอเมริกัน":30,
            "ข้าวผัดแหนม":35,
            "ข้าวผัดปูใส่ไข่":35,
            "ข้าวผัดกุ้งใส่ไข่":35,
            "ข้าวผัดกุนเชียง":35,
            "ข้าวผัดปลาหมึกน้ำพริกเผา":40}

    linkdict={"ข้าวกะเพราหมูกรอบ":"https://www.wongnai.com/recipes/ugc/4d4cdfb4975d44a19bfdc04c8e808614",
            "ข้าวกะเพราหมูสับ":"https://www.sanook.com/women/167459/",
            "ข้าวกะเพราไก่":"https://www.wongnai.com/recipes/stir-fried-minced-chicken-and-basil-by-big-c",
            "ข้าวกะเพรากุ้ง":"https://cooking.kapook.com/view217205.html",
            "ข้าวหมูแดง":"https://food.mthai.com/food-recipe/95307.html",
            "ข้าวหมูกระเทียม":"https://www.nestleprofessional.co.th/recipes/fried-pork-with-garlic",
            "ผัดผงกะหรี่":"https://www.wongnai.com/recipes/ugc/c61afb3cb3d94c4cadb3c8bef4bf8597",
            "ผัดผักบุ้งไฟแดง":"https://cooking.kapook.com/view172553.html",
            "ข้าวไข่เจียวหมูสับ":"https://th.openrice.com/th/recipe/%E0%B9%84%E0%B8%82%E0%B9%88%E0%B9%80%E0%B8%88%E0%B8%B5%E0%B8%A2%E0%B8%A7%E0%B8%AB%E0%B8%A1%E0%B8%B9%E0%B8%AA%E0%B8%B1%E0%B8%9A/4907",
            "ข้าวมันไก่":"https://www.wongnai.com/recipes/hainanese-chicken-rice",
            "ข้าวผัด":"https://cooking.kapook.com/view227497.html",
            "ข้าวผัดอเมริกัน":"https://food.mthai.com/baby/122860.html",
            "ข้าวผัดแหนม":"https://www.sanook.com/women/172837/",
            "ข้าวผัดปูใส่ไข่":"https://www.wongnai.com/recipes/crab-meat-fried-rice",
            "ข้าวผัดกุ้งใส่ไข่":"https://www.wongnai.com/recipes/fried-rice-with-shrimp",
            "ข้าวผัดกุนเชียง":"https://www.wongnai.com/recipes/fried-rice-with-chinese-sausage",
            "ข้าวผัดปลาหมึกน้ำพริกเผา":"https://www.kruamoomoo.com/%E0%B8%9B%E0%B8%A5%E0%B8%B2%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8%81%E0%B8%9C%E0%B8%B1%E0%B8%94%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%9E%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B9%80%E0%B8%9C%E0%B8%B2-pla-muk-pad-prik-pa/"}

    caldict={"ข้าวกะเพราหมูกรอบ":650,
            "ข้าวกะเพราหมูสับ":580,
            "ข้าวกะเพราไก่":557.7,
            "ข้าวกะเพรากุ้ง":540,
            "ข้าวหมูแดง":540,
            "ข้าวหมูกระเทียม":525,
            "ผัดผงกะหรี่":746.1,
            "ผัดผักบุ้งไฟแดง":210,
            "ข้าวไข่เจียวหมูสับ":500,
            "ข้าวมันไก่":597,
            "ข้าวผัด":163,
            "ข้าวผัดอเมริกัน":790,
            "ข้าวผัดแหนม":610,
            "ข้าวผัดปูใส่ไข่":610,
            "ข้าวผัดกุ้งใส่ไข่":595,
            "ข้าวผัดกุนเชียง":590,
            "ข้าวผัดปลาหมึกน้ำพริกเผา":535}

    immagedict={"ข้าวกะเพราหมูกรอบ":"กะเพราหมูกรอบ.jpg",
            "ข้าวกะเพราหมูสับ":"กะเพราหมูสับ.jpg",
            "ข้าวกะเพราไก่":"กะเพราหมูสับ.jpg",
            "ข้าวกะเพรากุ้ง":"กะเพรากุ้ง.jpg",
            "ข้าวหมูแดง":"หมูแดง.jpg",
            "ข้าวหมูกระเทียม":"หมูกระเทียม.jpg",
            "ผัดผงกะหรี่":"ผงกะหรี่.jpg",
            "ผัดผักบุ้งไฟแดง":"ผักบุ้งไฟแดง.jpg",
            "ข้าวไข่เจียวหมูสับ":"ข้าวไข่เจียวหมูสับ.jpg",
            "ข้าวมันไก่":"ข้าวมันไก่.jpg",
            "ข้าวผัด":"ข้าวผัดแหนม.jpg",
            "ข้าวผัดอเมริกัน":"ข้าวผัดอเมริกัน.jpg",
            "ข้าวผัดแหนม":"ข้าวผัดแหนม.jpg",
            "ข้าวผัดปูใส่ไข่":"ข้าวผัดปู.jpg",
            "ข้าวผัดกุ้งใส่ไข่":"ข้าวผัดกุ้งใส่ไข่.jpg",
            "ข้าวผัดกุนเชียง":"ข้าวผัดกุนเชียง.jpg",
            "ข้าวผัดปลาหมึกน้ำพริกเผา":"ข้าวผัดปลาหมึกน้ำพริกเผา.jpg"}

    menu = random.choice(ricelist)#โค้ดที่เป็นตัวสุ่ม เวลาจะสุ่มอีกครั้งสามารถกลับมาที่โค้ดนี้ได้เลย
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

    #bg
    frame1 = tk.Frame(master = window)
    label_1 = tk.Label(master = frame1, text="Frame 1", width=100, height=100)

    bg3 = Image.open("D:\\งาน\\comproglab\\วันนี้กินไรดี กลุ่ม 14\\Project\\draft_p3_bg.jpg")
    bg3 = bg3.resize((600,800), Image.ANTIALIAS)
    label_bg3 = ImageTk.PhotoImage(bg3)
    labelbg3 = tk.Label(master = frame1 ,image=label_bg3)
    labelbg3.place(x=-2,y=0)

    frame1.pack()
    label_1.pack()


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

    Button3.bind("<Button-1>", lambda e: callback(link))
  


    label.place(x=200,y=60)
    label1.place(x=60,y=490)
    label2.place(x=340,y=490)
    Button3.place(x=205,y=640)
    Button4.place(x=410,y=725)


    window.mainloop()


