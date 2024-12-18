from tkinter import *
def welcomemsg(event):
    print("you just clicked me..")
scr=Tk()
scr.title("Button example...")
scr.geometry("300x200")
btn1=Button(master=scr,text="click me..")
btn1.pack()
btn1.bind("<Button>",welcomemsg)
def welcome():
    print("you clicked me..")
btn2=Button(master=scr,text="clicked me..",command=welcome)
btn2.pack()
scr.mainloop()
