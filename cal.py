from tkinter import *


class MyWindow:
    def __init__(self, win):
        lbl0 = Label(win, text='ENTER SCORE HERE: ')
        self.lbl1 = Label(win, text='Quiz 1')
        self.lbl2 = Label(win, text='Quiz 2')
        self.lbl3 = Label(win, text='Quiz 3')
        self.lbl4 = Label(win, text='Quiz 4')
        self.lbl5 = Label(win, text='Quiz 5')

        self.lbl6 = Label(win, text='TOTAL : ')
        self.lbl7 = Label(win, text='YOUR AVERAGE IS :')

        self.b1 = Button(win, text='COMPUTE', command=self.add)
        self.b1.place(x=175, y=30)

        self.clr = Button(win, text='CLEAR', command=self.add)
        self.clr.place(x=235, y=30)

        lbl0.place(x=10, y=10)
        self.lbl1.place(x=10, y=30)
        self.lbl2.place(x=10, y=55)
        self.lbl3.place(x=10, y=80)
        self.lbl4.place(x=10, y=105)
        self.lbl5.place(x=10, y=130)

        self.lbl6.place(x=175, y=64)
        self.lbl7.place(x=175, y=90)

        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()

        self.t6 = Entry()
        self.t7 = Entry()

        self.t1.place(x=50, y=33)
        self.t2.place(x=50, y=58)
        self.t3.place(x=50, y=83)
        self.t4.place(x=50, y=108)
        self.t5.place(x=50, y=133)

        self.t6.place(x=218, y=64)
        self.t7.place(x=270, y=90)

        ent = Label(win, text='ENTER GRADES HERE : ')
        self.Prelim = Label(win, text='Prelim (40%)  ')
        self.Midterm = Label(win, text='Midterm (40%) ')
        self.Final = Label(win, text='Final (20%) ')
        self.Result = Label(win, text='STUDENT FINAL GRADE : ')

        self.b2 = Button(win, text='COMPUTE')
        self.b2.bind('<Button-1>', self.sub)
        self.b2.place(x=250, y=257)
        self.clr2 = Button(win, text='CLEAR', command=self.add)
        self.clr2.place(x=310, y=257)

        self.Pre = Entry()
        self.Mid = Entry()
        self.Fin = Entry()
        self.Res = Entry()

        self.Prelimre = Label(win, text='=')
        self.Midterre = Label(win, text='=')
        self.Finalre = Label(win, text='=')

        self.Prelimre.place(x=185, y=188)
        self.Midterre.place(x=185, y=208)
        self.Finalre.place(x=185, y=228)

        self.Pre.place(x=80, y=190)
        self.Mid.place(x=80, y=210)
        self.Fin.place(x=80, y=230)
        self.Res.place(x=130, y=260)

        self.Prere = Entry()
        self.Midre = Entry()
        self.Finre = Entry()
        self.Resre = Entry()

        self.Prere.place(x=200, y=190)
        self.Midre.place(x=200, y=210)
        self.Finre.place(x=200, y=230)

        ent.place(x=10, y=170)
        self.Prelim.place(x=10, y=190)
        self.Midterm.place(x=10, y=210)
        self.Final.place(x=10, y=230)
        self.Result.place(x=10, y=260)

    def add(self):
        self.t6.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        num3 = int(self.t3.get())
        num4 = int(self.t4.get())
        num5 = int(self.t5.get())
        result1 = num1+num2+num3+num4+num5
        result2 = result1/5
        self.t6.insert(END, str(result1))
        self.t7.insert(END, str(result2))

    def sub(self, event):
        num1 = int(self.Pre.get())
        num2 = int(self.Mid.get())
        num3 = int(self.Fin.get())
        pre = num1*.4
        mid = num2*.4
        fin = num3*.2
        Res = pre+mid+fin
        self.Prere.insert(END, str(pre))
        self.Midre.insert(END, str(mid))
        self.Finre.insert(END, str(fin))
        self.Res.insert(END, str(Res))


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
