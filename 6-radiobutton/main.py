# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *
from PIL import Image,ImageTk

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

select = IntVar()

# Images
pizza= (Image.open("images/pizza.png"))
resized_pizza= pizza.resize((50,50), Image.LANCZOS)
new_pizza = ImageTk.PhotoImage(resized_pizza)

hotdog= (Image.open("images/hot-dog.png"))
resized_hotdog= hotdog.resize((50,50), Image.LANCZOS)
new_hotdog = ImageTk.PhotoImage(resized_hotdog)

burger= (Image.open("images/hamburger.png"))
resized_burger= burger.resize((50,50), Image.LANCZOS)
new_burger = ImageTk.PhotoImage(resized_burger)

foodImages = [new_pizza, new_burger, new_hotdog]

# Radiobuttons
for index in range(len(food)):
    radiobutton = Radiobutton(
        window, 
        text=food[index], 
        variable=select, 
        value=index,
        padx = 25,
        font=('Impact', 50),
        image=foodImages[index],
        compound='left'
    )
    radiobutton.pack(anchor='w')

window.mainloop()