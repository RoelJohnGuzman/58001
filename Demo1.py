from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My First Demo")

btm1 = Button(window,text="Click me", fg="red",bg="yellow")
btm1.place(x= 300,y=250)
txtfld = Entry(window, border=2.50)
txtfld.place(x=100,y=200)
tat = Label(window,text="My First Demo", font= "Verdana")
tat.place(x=180, y=100)
window.mainloop()