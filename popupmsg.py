from tkinter import*
win= Tk()
win.geometry("750x250")
def close_win(top):
   top.destroy()
def insert_val(e):
   e.insert(0, "Hello World!")
def popupwin():
   top= Toplevel(win)
   top.geometry("750x250")
   entry= Entry(top, width= 25)
   entry.pack()
   Button(top,text= "Insert", command= lambda:insert_val(entry)).pack(pady= 5,side=TOP)
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)
label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
label.pack(pady=20)
button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()
