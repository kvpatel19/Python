import tkinter as tk
from tkinter import simpledialog

root=tk.Tk()
root.withdraw()

user_INP=simpledialog.askstring(title="Test",
                    prompt="What is your name?:")
print("Hello",user_INP)
