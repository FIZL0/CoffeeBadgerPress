import tkinter as tk

root = tk.Tk()

root.geometry("400x290")
root.title("Coffee Badger Press")

label1 = tk.Label(root, text="Coffee Badger Press", font=('Arial', 16))
label1.pack(padx=20, pady=20)

label2 = tk.Label(root, text="Print All Articles Since Last Print", font=('Arial', 14))
label2.place(x=20,y=100)

label3 = tk.Label(root, text="Print All Articles Since", font=('Arial', 14))
label3.place(x=20,y=180)

entry = tk.Entry(root, width=10)
entry.pack()
entry.place(x=220,y=185)

button1 = tk.Button(root, text="Go", font=('Arial', 18))
button1.pack(padx=300, pady=30)
button1.place(x=310, y=90)

button2 = tk.Button(root, text="Go", font=('Arial', 18))
button2.pack(padx=300, pady=30)
button2.place(x=310, y=170)

root.mainloop()
