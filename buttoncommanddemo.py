
import tkinter as tk
from tkinter import messagebox as mb
def answer():
    mb.showerror("answer","sorry,no answer available")
def callback():
    if mb.askyesno('verify','really quit?'):
        mb.showwarning('yes','not yet implemented')
        exit()
    else:
        mb.showinfo('no','quit has been cancelled')
tk.Button(text='quit',command=callback).pack(fill=tk.X)
tk.Button(text='answer',command=answer).pack(fill=tk.X)
tk.mainloop()
