//button demo

import tkinter
window=tkinter.Tk()
window.title("GUI")
window.geometry("300x250")
top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side="bottom")
btn1=tkinter.Button(top_frame,text="Button1",
                    fg="red").place(x=10,y=10)
btn2=tkinter.Button(top_frame,text="Button2",
                    fg="green").place(x=80,y=10)
btn3=tkinter.Button(bottom_frame,text="Button3",
                    fg="purple").pack(side="right")
btn4=tkinter.Button(bottom_frame,text="Button4",
                    fg="blue").pack(side="left")
window.mainloop()
