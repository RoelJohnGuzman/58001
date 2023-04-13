from tkinter import *

window = Tk()
window.geometry("400x200")


label = Label(window,text="My Full name")
label.place(x=150, y=10)

label1 = Label(window,text="First Name")
label1.place(x=100, y=40)
entry = Entry(window)
entry.place(x=200, y=40)

label2 = Label(window,text="Second name")
label2.place(x=100, y=70)
entry1 = Entry(window)
entry1.place(x=200, y=70)

label3 = Label(window,text="Last name")
label3.place(x=100, y=100)
entry3 = Entry(window)
entry3.place(x=200, y=100)

def click():
    click1 = Label(window,text=entry.get()+entry1.get()+entry3.get())
    click1.place(x=200,y=130)

button = Button(window, text="Show Full name", command=click)
button.place(x=100, y=160)

label3 = Label(window,text="Fuil name")
label3.place(x=100, y=130)
entry2 = Entry(window,bd=3)
entry2.insert(END,str(click))

window.mainloop()