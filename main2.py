from tkinter import *
import datetime
window=Tk()
window.geometry("500x600")
window.title("helloworld!")
a = Label(window,text="display the text after clicking the button",fg="blue",bg="red")
a.pack()
j = Label(window,text="enter your full name",fg="blue",bg="red")
j.pack()
k = Entry(window)
k.pack()
def read():
    name = k.get()#gets the value for the entry box
    message = f"hello {name} welcome to the world of programming, the date of today is {datetime.date.today()} and the time is {datetime.datetime.now()}"
    t.insert(END,message)
b = Button(window,text = "click me please!",fg = "red",bg="blue",command=read)
b.pack()
t = Text(window,height = "10")
t.pack()
window.mainloop()
