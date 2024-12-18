from tkinter import*
def Addition():
    v1=int(txt1.get())
    v2=int(txt2.get())
    ans=v1+v2
    lblans.config(text=f"your answer is:{ans}")
def Substraction():
        v1=int(txt1.get())
        v2=int(txt2.get())
        ans=v1-v2
        lblans.config(text=f"your answer is:{ans}")
def Multiplication():
    pass
def Division():
    pass
scr=Tk()
scr.title("arithmetic opewration")
scr.geometry("300x200")
txt1=Entry(scr)
txt2=Entry(scr)
lblans=Label(scr,text="your answer is")
btnAdd=Button(master=scr,text="Addition",command=Addition)
btnSub=Button(master=scr,text="Substraction",command=Substraction)
btnMul=Button(master=scr,text="Multiplication",command=Multiplication)
btnDiv=Button(master=scr,text="Division",command=Division)
txt1.pack()
txt2.pack()
btnAdd.pack()
btnSub.pack()
btnMul.pack()
btnDiv.pack()
lblans.pack()
scr.mainloop()
