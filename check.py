from tkinter import *
from tkinter import messagebox
from teamLeader import *

status = 0
root = Tk()
root.minsize(400,400)
root.maxsize(600,600)
l1 = Label(root, text="Enter Project Name: ")
l1.grid(row=1, column=1)
e1 = Entry(root)
e1.grid(row=1, column=2)

def msg():
    if status==0:
        m = messagebox.showinfo("Success","Success! Your Project "+e1.get()+" can be taken.")
    if status==1:
        m = messagebox.showinfo("Failure","Sorry! Your Project "+e1.get()+" has already been taken by other team.")

b1 = Button(root, text="Check Availability")
b1.grid(row=2, column=1)

root.mainloop()
