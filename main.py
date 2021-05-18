from tkinter import *


def get_clicked():
    print("I got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button1 = Button(text="Click Me", command=get_clicked)
button2 = Button(text="Click Me", command=get_clicked)
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()