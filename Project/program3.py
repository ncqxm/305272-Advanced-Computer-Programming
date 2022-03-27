import tkinter as tk
from tkinter import* 
from PIL import Image, ImageTk
from tkinter import Canvas, PhotoImage
import random
import webbrowser

def sum3():
    ottherlist=["ยำมาม่า","ยำวุ้นเส้น","ยำรวม","ยำทะเล","ยำกุ้งสด","ยำคอหมูย่าง","ส้มตำไทย","ส้มตำปูไทย",
                "ส้มตำปูปลาร้า","ส้มตำป่า","ตำหมูตกครก","สลัดผัก","สลัดโรล","สลัดผลไม้","สเต็กหมู","สเต็กไก่",
                "สเต็กปลา","สเต็กเนื้อ","สปาเก็ตตี้","ซูชิ","ขนมจีนน้ำยา","ขนมจีนน้ำเงี้ยว","ลาบ",
                "ไก่ย่าง","ไก่ต้มน้ำปลา"]#ลิสต์อื่นๆ

    caldict = {"ยำมาม่า":215,
            "ยำวุ้นเส้น":120,
            "ยำรวม":150,
            "ยำทะเล":150,
            "ยำกุ้งสด":68,
            "ยำคอหมูย่าง":165,
            "ส้มตำไทย":55,
            "ส้มตำปูไทย":35,
            "ส้มตำปูปลาร้า":130,
            "ส้มตำป่า":307,
            "ตำหมูตกครก":165,
            "สลัดผัก":100,
            "สลัดโรล":"ชิ้นละ 50",
            "สลัดผลไม้":86,
            "สเต็กหมู":259,
            "สเต็กไก่":353.5,
                "สเต็กปลา":260,
            "สเต็กเนื้อ":133,
            "สปาเก็ตตี้":157.7,
            "ซูชิ":"ชิ้นละ 35-68",
            "ขนมจีนน้ำยา":526,
            "ขนมจีนน้ำเงี้ยว":308,
            "ลาบ":130,
                "ไก่ย่าง":167,
            "ไก่ต้มน้ำปลา":220}

    linkdict = {"ยำมาม่า":"https://www.phuyings.com/%E0%B9%84%E0%B8%A5%E0%B8%9F%E0%B9%8C%E0%B8%AA%E0%B9%84%E0%B8%95%E0%B8%A5%E0%B9%8C/%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3/%E0%B8%AB%E0%B8%B2%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7-5-%E0%B8%AA%E0%B8%B9%E0%B8%95%E0%B8%A3%E0%B8%A2%E0%B8%B3%E0%B8%A1%E0%B8%B2%E0%B8%A1%E0%B9%88%E0%B8%B2/",
            "ยำวุ้นเส้น":"https://www.happyfresh.co.th/blog/recipe/%E0%B8%A2%E0%B8%B3%E0%B8%A7%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99/",
            "ยำรวม":"https://www.wongnai.com/recipes/ugc/0c709fe26b304b3e8ba32684e68110ca",
            "ยำทะเล":"https://www.wongnai.com/recipes/ugc/85377cad5d234a4da107d5a303074dd5",
            "ยำกุ้งสด":"https://www.wongnai.com/recipes/ugc/f688e31ab54946e2aed83c3d1f9b4176",
            "ยำคอหมูย่าง":"https://chefoldschool.com/2021/01/11/%E0%B8%A2%E0%B8%B3%E0%B8%84%E0%B8%AD%E0%B8%AB%E0%B8%A1%E0%B8%B9%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87-%E0%B8%AA%E0%B8%B9%E0%B8%95%E0%B8%A3%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%94-%E0%B9%81%E0%B8%8B%E0%B9%88/",
            "ส้มตำไทย":"https://www.wongnai.com/food-tips/somtum-series",
            "ส้มตำปูไทย":"https://www.wongnai.com/food-tips/somtum-series",
            "ส้มตำปูปลาร้า":"https://www.wongnai.com/food-tips/somtum-series",
            "ส้มตำป่า":"https://www.wongnai.com/food-tips/somtum-series",
            "ตำหมูตกครก":"https://www.wongnai.com/recipes/ugc/f3aa0d7ce7904682922debd1a06e7b5d",
            "สลัดผัก":"https://www.cookingth.com/salad/ ",
            "สลัดโรล":"https://cooking.kapook.com/view139471.html",
            "สลัดผลไม้":"https://sites.google.com/site/fruitsforlife42945/menu-xahar-cak-phl-mi/slad-phl-mi",
            "สเต็กหมู":"https://www.sgethai.com/article/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%97%E0%B9%8D%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%95%E0%B9%87%E0%B8%81%E0%B8%AB%E0%B8%A1%E0%B8%B9/",
            "สเต็กไก่":"https://www.wongnai.com/recipes/black-pepper-chicken-breast-steak ",
                "สเต็กปลา":"https://cooking.kapook.com/view182424.html",
            "สเต็กเนื้อ":"https://food.trueid.net/detail/x2plkbb3pW62",
            "สปาเก็ตตี้":"https://www.gourmetandcuisine.com/gc_club/detail/90",
            "ซูชิ":"https://surrealsushi.com/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3%E0%B8%8B%E0%B8%B9%E0%B8%8A%E0%B8%B4%E0%B8%81%E0%B8%B4%E0%B8%99%E0%B9%80%E0%B8%AD%E0%B8%87%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%86%E0%B8%97%E0%B8%B5/",
            "ขนมจีนน้ำยา":"https://www.wongnai.com/recipes/thai-rice-noodles-in-fish-curry-sauce",
            "ขนมจีนน้ำเงี้ยว":"http://lannainfo.library.cmu.ac.th/lannafood/detail_lannafood.php?id_food=16",
            "ลาบ":"https://www.sanook.com/women/80021/?utm_source=WM_SEM_DSA_WOMEN&utm_medium=CPC&utm_campaign=SEM&gclid=CjwKCAjw8KmLBhB8EiwAQbqNoEH_zgNi9gQxYB1JWdfj-p-l7U3fGlHqcw65mURKAxboeUAcT1AvdhoCTaIQAvD_BwE",
                "ไก่ย่าง":"https://siamallfood.com/knowledge/10-%E0%B8%AA%E0%B8%B9%E0%B8%95%E0%B8%A3%E0%B8%AB%E0%B8%A1%E0%B8%B1%E0%B8%81%E0%B9%84%E0%B8%81%E0%B9%88%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87/",
            "ไก่ต้มน้ำปลา":"https://food.mthai.com/food-recipe/114621.html"}#ลิงค์วิธีทำ

    pricedict = {"ยำมาม่า":30,
            "ยำวุ้นเส้น":30,
            "ยำรวม":50,
            "ยำทะเล":60,
            "ยำกุ้งสด":50,
            "ยำคอหมูย่าง":45,
            "ส้มตำไทย":25,
            "ส้มตำปูไทย":25,
            "ส้มตำปูปลาร้า":30,
            "ส้มตำป่า":30,
            "ตำหมูตกครก":45,
            "สลัดผัก":30,
            "สลัดโรล":25,
            "สลัดผลไม้":40,
            "สเต็กหมู":79,
            "สเต็กไก่":79,
                "สเต็กปลา":79,
            "สเต็กเนื้อ":119,
            "สปาเก็ตตี้":79,
            "ซูชิ":"ชิ้นละ 5-10",
            "ขนมจีนน้ำยา":40,
            "ขนมจีนน้ำเงี้ยว":40,
            "ลาบ":30,
                "ไก่ย่าง":280,
            "ไก่ต้มน้ำปลา":280}

    immagedict ={"ยำมาม่า":"ยำมาม่า.jpg",
            "ยำวุ้นเส้น":"ยำวุ้นเส้น.jpg",
            "ยำรวม":"ยำรวม.jpg",
            "ยำทะเล":"ยำทะเล.jpg",
            "ยำกุ้งสด":"ยำกุ้งสด.jpg",
            "ยำคอหมูย่าง":"ยำคอหมูย่าง.jpg",
            "ส้มตำไทย":"ตำไทย.jpg",
            "ส้มตำปูไทย":"ตำปูไทย.jpg",
            "ส้มตำปูปลาร้า":"ตำปูปลาร้า.jpg",
            "ส้มตำป่า":"ตำป่า.jpg",
            "ตำหมูตกครก":"ตำหมูตกครก.jpg",
            "สลัดผัก":"สลัดผัก.jpg",
            "สลัดโรล":"สลัดโรล.jpg",
            "สลัดผลไม้":"สลัดผลไม้.jpg",
            "สเต็กหมู":"สเต็กหมู.jpg",
            "สเต็กไก่":"สเต็กไก่.jpg",
                "สเต็กปลา":"สเต็กปลา.jpg",
            "สเต็กเนื้อ":"เนื้อ.jpg",
            "สปาเก็ตตี้":"สปาเก็ตตี้.jpg",
            "ซูชิ":"ซูชิ.jpg",
            "ขนมจีนน้ำยา":"จีนน้ำยา.jpg",
            "ขนมจีนน้ำเงี้ยว":"จีนน้ำเงี้ยว.jpg",
            "ลาบ":"ลาบ.jpg",
                "ไก่ย่าง":"ไก่ย่าง.jpg",
            "ไก่ต้มน้ำปลา":"ไก่ต้มน้ำปลา.jpg"}


    menu = random.choice(ottherlist)#โค้ดที่เป็นตัวสุ่ม เวลาจะสุ่มอีกครั้งสามารถกลับมาที่โค้ดนี้ได้เลย
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

    bg3 = Image.open("draft_p3_bg.jpg")
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
