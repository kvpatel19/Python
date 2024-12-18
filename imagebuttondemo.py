from tkinter import*
from PIL import Image,ImageTk
win=Tk()
win.geometry("750x250")
def close_win():
    win.destroy()
image=Image.open('logo.jpg')
image=image.resize((50,50))
img=ImageTk.PhotoImage(image)
Label(win,
      text="click the below button to close the window",
      font=('Aerial 13 bold')).pack(pady=20)
button=Button(win,text="click me",font=('Aerial 13 bold'),
              image=img,compound=LEFT,command=close_win)
button.pack()
win.mainloop()
