
import tkinter as tk
from tkinter import ttk
def selection(event):
      print("you selected month:",monthchoosen.get())
window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 
ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Lucida Handwriting", 15)).grid(row = 0,
                                               column = 1) 
  
ttk.Label(window, text = "Select the Month :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25)
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 25,
                            textvariable = n)
monthchoosen.grid(column=1,row=5)
monthchoosen['values'] = (' January',' February', 
                          ' March', ' April', 
                          ' May', ' June', 
                          ' July', ' August', 
                          ' September', ' October', 
                          ' November', ' December') 
  
monthchoosen.current(4) 
btn=ttk.Button(window,text="click to get").grid(column=1,row=7)
btn.bind("<Button>",selection)  


window.mainloop()
