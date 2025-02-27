from tkinter import *
from PIL import Image,ImageTk

# button = click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    label.config(text=f'Count: {count}')
    label2.pack()

window = Tk()

button = Button(window, text='Click me!')

button.config(command=click)
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.config(activebackground='red')
button.config(activeforeground='yellow')

# Resized Image
img= (Image.open("images/point_up_emoji.png"))
resized_image= img.resize((100,100), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
button.config(image=new_image)
button.config(compound='bottom')

button.config(state=ACTIVE) # ACTIVE/DISABLED

label = Label(window, text=f'Count: {count}')
label.config(font=('Monospace', 50))
label.pack()

button.pack()

label2 = Label(window, image=new_image)

window.mainloop()