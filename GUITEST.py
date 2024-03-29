import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Coffee Badger Press")

label = tk.Label(root, text="Coffee Badger Press", font=('Arial', 18))
label.pack(padx=20, pady=20)

entry = tk.Entry(root)
entry.pack()

root.mainloop()