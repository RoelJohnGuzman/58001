from tkinter import *
window = Tk()

window.geometry ("400x200+10+10")
window.title("Grid Manager")

#This is where you will put your widget

entry1 = Entry(window, bd=2, justify="center")
entry1.grid(row=0, column=0)
entry1.insert(0,"row 0"+" " +" " "column 0")

entry2 = Entry(window, bd=2, justify="center")
entry2.grid(row=0, column=1)
entry2.insert(0,"row 0"+" " +" " "column 1")

entry3 = Entry(window, bd=2, justify="center")
entry3.grid(row=0, column=2)
entry3.insert(0,"row 0"+" " +" " "column 2")

entry4 = Entry(window, bd=2, justify="center")
entry4.grid(row=1, column=0)
entry4.insert(0,"row 1"+" " +" " "column 0")

entry5 = Entry(window, bd=2, justify="center")
entry5.grid(row=1, column=1)
entry5.insert(0,"row 1"+" " +" " "column 1")

entry6 = Entry(window, bd=2, justify="center")
entry6.grid(row=1, column=2)
entry6.insert(0,"row 1"+" " +" " "column 2")

entry7 = Entry(window, bd=2, justify="center")
entry7.grid(row=2, column=0)
entry7.insert(0,"row 2"+" " +" " "column 0")

entry8 = Entry(window, bd=2, justify="center")
entry8.grid(row=2, column=1)
entry8.insert(0,"row 2"+" " +" " "column 1")

entry9 = Entry(window, bd=2, justify="center")
entry9.grid(row=2, column=2)
entry9.insert(0,"row 2"+" " +" " "column 2")

entry10 = Entry(window, bd=2, justify="center")
entry10.grid(row=3, column=0)
entry10.insert(0,"row 3"+" " +" " "column 0")

entry11 = Entry(window, bd=2, justify="center")
entry11.grid(row=3, column=1)
entry11.insert(0,"row 3"+" " +" " "column 1")

entry12 = Entry(window, bd=2, justify="center")
entry12.grid(row=3, column=2)
entry12.insert(0,"row 3"+" " +" " "column 2")



window.mainloop()