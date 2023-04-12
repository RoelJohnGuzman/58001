from tkinter import *

window = Tk()
window.title("Crush kita")
window.geometry("500x400")

label = Label(window,text="What is your name?: ")
label.grid(row=1,column=1)

entry = Entry(window)
entry. grid(row=1, column=2)

def click():
    click1 = Label(window,text=entry.get())
    click1.grid(row=3,column=1)

button = Button(window, text="Click me!", command=click)
button.grid(row=2,column=1)

window.mainloop()