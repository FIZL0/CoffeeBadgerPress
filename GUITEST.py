import os
import sys
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from PIL import ImageTk, Image
import datetime
import main
import lastRunDate
import dateparser

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = tk.Tk()

root.geometry("400x290")
root.title("Coffee Badger Press")

#image
imgg = Image.open("ascii-art.png")
newimg = imgg.resize((100, 100))
img = ImageTk.PhotoImage(newimg)
panel = tk.Label(root, image=img)
panel.place(x=50,y=20)

#title
title = """Coffee Badger
  Press"""
label1 = tk.Label(root, text=title, font=('Arial', 16))
label1.place(x=170,y=50)

#first button label
label2 = tk.Label(root, text="Print All Articles Since Last Print", font=('Arial', 14))
label2.place(x=20,y=140)

#last print label
last_run_date = (dateparser.parse(lastRunDate.lastRunDate, settings={'DATE_ORDER': 'YMD'})).strftime("%m/%d/%Y")
label5 = tk.Label(root, text=f"Last print date: {last_run_date}", font=('Arial', 10))
label5.place(x=20,y=165)

#second button label
label3 = tk.Label(root, text="Print All Articles Between", font=('Arial', 14))
label3.place(x=20,y=190)

label4 = tk.Label(root, text="And", font=('Arial', 14))
label4.place(x=110,y=220)

#calendar date entry
cal = DateEntry(width= 8, background="magenta3", foreground="white",bd=2)
cal.pack(pady=20)
cal.place(x=160,y=225)

#calendar date entry
cal2 = DateEntry(width= 8, background="magenta3", foreground="white",bd=2)
cal2.pack(pady=20)
cal2.place(x=30,y=225)

#button text function
def change_btn_txt(int: int):
    if int == 1:
        btn1_txt.set("Wait...")
    else:
        btn2_txt.set("Wait...")

#first button function
def run_last_date():
    firstDate = dateparser.parse(lastRunDate.lastRunDate, settings={'DATE_ORDER': 'YMD'}).date()
    secondDate = datetime.date.today()
    change_btn_txt(1)
    root.update_idletasks()
    main.runMain(firstDate, secondDate, sinceLastButton=True)
    restart_program()

#second button function
def run_date_range():
    firstDate = cal2.get_date() #returns a datetime.date
    secondDate = cal.get_date()
    change_btn_txt(2)
    root.update_idletasks()
    main.runMain(firstDate, secondDate, sinceLastButton=False)
    restart_program()

#first button
btn1_txt = tk.StringVar()
btn1_txt.set("Go")
button1 = tk.Button(root, textvariable=btn1_txt, command=run_last_date, font=('Arial', 18), width=5)
button1.place(x=300, y=130)

#second button
btn2_txt = tk.StringVar()
btn2_txt.set("Go")
button2 = tk.Button(root, textvariable=btn2_txt, command=run_date_range, font=('Arial', 18), width=5)
#button2.pack(padx=300, pady=30)
button2.place(x=300, y=200)

root.mainloop()
