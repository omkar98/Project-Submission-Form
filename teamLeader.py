from tkinter import *


root = Tk()
root.minsize(400,400)
root.maxsize(600,600)
l1 = Label(root, text="Enter Team Leader Name: ")
l1.grid(row=1, column=1)
e1 = Entry(root)
e1.grid(row=1, column=2)

l2 = Label(root, text="Number of team Members: ")
l2.grid(row=2, column=1)
e2 = Entry(root)
e2.grid(row=2, column=2)

l3 = Label(root, text="Preferred Guide: ")
l3.grid(row=3, column=1)

# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { 'Kapre Mam','Aijaz Sir','Bhandare Sir','Rajurkar Mam','Joshi Mam'}
tkvar.set('Kapre Mam') # set the default option
 
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 3, column =2)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)

l3 = Label(root, text="Roll No: ")
l3.grid(row=4, column=1)
e2 = Entry(root)
e2.grid(row=4, column=2)

l4 = Label(root, text="Class: ")
l4.grid(row=5, column=1)

# Create a Tkinter variable
tkvar1 = StringVar(root)
 
# Dictionary with options
choices = { 'TECSE - A', 'TECSE - B'}
tkvar1.set('TECSE - A') # set the default option
 
popupMenu = OptionMenu(root, tkvar1, *choices)
popupMenu.grid(row = 5, column =2)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar1.get() )
 
# link function to change dropdown
tkvar1.trace('w', change_dropdown)

b1 = Button(root, text="Next Step>>")
b1.grid(row=8, column=2)



root.mainloop()
