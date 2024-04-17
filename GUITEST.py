import tkinter as tk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox

root = tk.Tk()

root.geometry("400x290")
root.title("Coffee Badger Press")

label1 = tk.Label(root, text="Coffee Badger Press", font=('Arial', 16))
label1.pack(padx=20, pady=20)

label2 = tk.Label(root, text="Print All Articles Since Last Print", font=('Arial', 14))
label2.place(x=20,y=100)

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

def show_msg():
    messagebox.showinfo("Test Message!")

button1 = tk.Button(root, text="Go", command=show_msg, font=('Arial', 18))
button1.pack(padx=300, pady=30)
button1.place(x=310, y=90)

button2 = tk.Button(root, text="Go", font=('Arial', 18))
button2.pack(padx=300, pady=30)
button2.place(x=310, y=160)

def get_dates():
    firstDate = cal.get_date
    secondDate = cal2.get_date
    

root.mainloop()
