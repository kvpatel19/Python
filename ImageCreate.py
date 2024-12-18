from tkinter import*
from PIL import ImageTk,Image
root=Tk()
canvas=Canvas(root,width=1000,height=1000)
canvas.pack()
img=ImageTk.PhotoImage(Image.open("logo.jpg"))
canvas.create_image(30,30,anchor=NW,image=img)
root.mainloop()
