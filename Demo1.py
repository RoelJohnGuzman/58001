from tkinter import *

window = Tk()
window.geometry("500x400")

label = Label(window,text="gender")
label.place(relx=.5, rely=.5)
label.pack(anchor= CENTER)

var1= IntVar()
var2= IntVar()


r1= Radiobutton(window, text="Male",variable=var1)
r2= Radiobutton(window, text="Female",variable=var2)
r1.place(relx=.52, rely=.52)
r2.place(relx=.55, rely=.55)
r1.pack(anchor= CENTER)
r2.pack(anchor= CENTER)

check1 = Checkbutton(window,text="100-200")
check2 = Checkbutton(window,text= "201-300")
check3 = Checkbutton(window, text="301-400")
check1.pack()
check2.pack()
check3.pack()

label1 = Label(window, text="Select from list of fruit")
label1.pack()

list = Listbox(window, selectmode="Single")
list.insert(1,"Apple")
list.insert(2,"Orange")
list.insert(3,"Mango")
list.pack()
window.mainloop()