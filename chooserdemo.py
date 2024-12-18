import tkinter as tk
from tkinter.colorchooser import askcolor
def callback():
    result=askcolor(color="#6A9662",
                    title="Bread's color chooser")
    print(result)
root=tk.Tk()
tk.Button(root,text='choose color',fg="darkgreen",
          command=callback).pack(side=tk.LEFT,padx=10)
tk.Button(root,text='quit',fg="red",
          command=quit).pack(side=tk.LEFT,padx=10)
tk.mainloop()
