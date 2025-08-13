from tkinter import *
from turtle import Turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label["text"] = "New Text"
my_label.config(text="New Text")

input = Entry(width=10)
input.grid(column=0, row=0)

def button_clicked():
    new_txt = input.get()
    my_label.config(text=new_txt)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=3, row=0)

button = Button(text="Button", command=button_clicked)
button.grid(column=2, row=2)


entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=4, row=3)























window.mainloop()
