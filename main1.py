from tkinter import *
window = Tk()# initalise
window.title("my first project")
window.geometry("500x400")#set width and height 
l = Label(window,text = "my firstproject ", bg="blue", fg="white")
l.pack()
p = Entry(window)
p.pack()
b = Button(window,fg = "white",text = "submit",bg = "green")
b.pack()
window.mainloop()#loads window