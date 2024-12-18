from tkinter import*
from tkinter import messagebox
def logincheck():
    if txt1.get()=="BCA" and txt2.get()=="morning":messagebox.showinfo("login","login successfully")
    else:
        messagebox.showinfo("login","invalid login")
def exitcode():
        exit()
scr=Tk()
scr.title("Login")
scr.geometry("300x200")
lbl1=Label(scr,text="enter usename")
txt1=Entry(scr)
lbl2=Label(scr,text="enter password")
txt2=Entry(scr,show="*")
btnlogin=Button(master=scr,text="login",command= logincheck)
btnexit=Button(master=scr,text="Exit",command=exitcode)
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
btnlogin.pack()
btnexit.pack()
scr.mainloop()
