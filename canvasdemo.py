from tkinter import*
root=Tk()
c=Canvas(root,bg="black",height=700,width=1200,
         cursor="arrow")
id=c.create_line(50,50,200,50,200,150,
                 width=4,fill="white")
id=c.create_oval(100,100,400,300,width=5,
                 fill="yellow",
                 outline="red",
                 activefill="green")
f=('Time',40,"bold italic underline")
id=c.create_text(500,200,
                 text="My Canvas Demo",
                 font=f,activefill="green")
c.pack()
root.mainloop()
