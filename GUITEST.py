import os
import sys
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
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

label1 = tk.Label(root, text="Coffee Badger Press", font=('Arial', 16))
label1.pack(padx=20, pady=20)

last_run_date = (dateparser.parse(lastRunDate.lastRunDate, settings={'DATE_ORDER': 'YMD'})).strftime("%m/%d/%Y")
label2 = tk.Label(root, text="Print All Articles Since Last Print", font=('Arial', 14))
label2.place(x=20,y=100)

label5 = tk.Label(root, text=f"Last print date: {last_run_date}", font=('Arial', 10))
label5.place(x=20,y=125)

label3 = tk.Label(root, text="Print All Articles Between", font=('Arial', 14))
label3.place(x=20,y=150)

label4 = tk.Label(root, text="And", font=('Arial', 14))
label4.place(x=110,y=180)

cal = DateEntry(width= 8, background="magenta3", foreground="white",bd=2)
cal.pack(pady=20)
cal.place(x=160,y=185)

cal2 = DateEntry(width= 8, background="magenta3", foreground="white",bd=2)
cal2.pack(pady=20)
cal2.place(x=30,y=185)

def run_last_date():
    firstDate = dateparser.parse(lastRunDate.lastRunDate, settings={'DATE_ORDER': 'YMD'}).date()
    secondDate = datetime.date.today()
    main.runMain(firstDate, secondDate, sinceLastButton=True)
    restart_program()


def run_date_range():
    firstDate = cal2.get_date() #returns a datetime.date
    secondDate = cal.get_date()
    main.runMain(firstDate, secondDate, sinceLastButton=False)
    restart_program()

button1 = tk.Button(root, text="Go", command=run_last_date, font=('Arial', 18))
button1.pack(padx=300, pady=30)
button1.place(x=310, y=90)

button2 = tk.Button(root, text="Go", command=run_date_range, font=('Arial', 18))
button2.pack(padx=300, pady=30)
button2.place(x=310, y=160)

root.mainloop()
