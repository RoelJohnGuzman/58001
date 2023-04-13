from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="Enter the value.")
        self.lbl1.place(x=100,y=50)

        self.lbl3 = Label(win, text="Radius")
        self.lbl3.place(x=100,y=100)

        self.lbl2 = Label(win, text="Diameter")
        self.lbl2.place(x=100, y=150)

        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=200,y=50)

        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=200,y=100)

        self.txt2 = Entry(win,bd=3)
        self.txt2.place(x=200,y=150)

        self.btnrad = Button(win,text="Radius")
        self.btnrad.place(x=100,y=200)

        self.btnrad.bind('<Button-1>', self.rad,self.dia)
        self.btndia = Button(win,text="Diameter")
        self.btndia.place(x=150,y=200)
        self.btndia.bind('<Button-1>',self.dia)

        self.btnclr = Button(win, text="Clear", fg="Red")
        self.btnclr.place(x=100, y=300)
        self.btnclr.bind('<Button-1>', self.clear)
#add event-handling /bind () method

    def rad(self,rad):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = (num1*num1)*3.1416
        result1 = 2*3.1416*(num1)
        self.txt3.insert(END, str(result))
        self.txt2.insert(END, str(result1))

    def dia(self,sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        result = ((num1/2)*(num1/2))*3.1416
        result1 = 2 * 3.1416 * (num1/2)
        self.txt3.insert(END, str(result))
        self.txt2.insert(END, str(result1))

    def clear(self, clear):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()