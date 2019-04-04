from tkinter import *
from tkinter import messagebox
root = Tk()
root.minsize(400,400)
root.maxsize(600,600)
l1 = Label(root, text="Username: ")
l1.grid(row=1, column=1)
l2 = Label(root, text="Password: ")
l2.grid(row=2, column=1)
e1 = Entry(root)
e1.grid(row=1, column=2)
e2 = Entry(root)
e2.grid(row=2, column=2)

def msg():
    m = messagebox.showinfo("Login","Hello "+e1.get()+" "+"( Your Password: " + e2.get() + " )")

b1 = Button(root, text="Submit", command=msg).grid(row=3, column=1)
b2 = Button(root, text="Reset", command=root.destroy).grid(row=3, column=2)

root.mainloop()

