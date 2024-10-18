from tkinter import *


root = Tk()
root.title("Products")
root.geometry('400x300')

lb1 = Label(text = "Hey there!", fg = "red", bg = "aqua", height = 1, width = 300)

label1 = Label(text = "Enter Values" , bg = "white")
a = Entry()
b = Entry()

def display():
    a1 = int(a.get())
    b1 = int(b.get())
    global message
    message = "Welcome to the application! "
    text_box.insert(END, a1 * b1)

text_box = Text(height = 3)
btn = Button(text = "Begin", command = display, height = 1, bg = "aqua", fg = "blue")

lb1.pack()
label1.pack()
a.pack()
b.pack()
btn.pack()
text_box.pack()
root.mainloop()