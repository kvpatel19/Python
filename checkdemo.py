import tkinter as tk
from tkinter import ttk
root=tk.Tk()
my_boolean_var=tk.BooleanVar()
my_ck=ttk.Checkbutton(text="check when the option true",
                      variable=my_boolean_var)
my_ck.pack()
