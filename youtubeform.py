from tkinter import*
from pytube import YouTube

form=Tk()
form.geometry('500x300')
form.title("you tube downloader")
form.resizable(0,0)

Label(form,text="you tube downloader",
      font='arail 18 bold',fg='green').pack()
Label(form,text="paste your link here",
      font='arail 14 bold',fg='purple').pack()
txt=StringVar()
txt_link=Entry(form,width=70,textvariable=txt).pack()
def download():
    url=YouTube(str(txt.get()))
    v=url.streams.first()
    v.download()
    Label(form,text="successful download").pack()
Button(form,text="Download",font='arail 15 bold',
       fg='Brown',command=download).pack()

form.mainloop()
