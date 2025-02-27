from tkinter import *
from PIL import Image,ImageTk

def display():
    if(x.get()==1 and y.get()==0):
        print('I like python')
    elif(x.get()==0 and y.get()==1):
        print('I like java')
    elif(x.get()==1 and y.get()==1):
        print('I like both')
    elif(x.get()==0 and y.get()==0):
        print('I dont like either')

window = Tk()

x = IntVar()
y = IntVar()

# Checkbox 1
checkbox1 = Checkbutton(window, text='Python',variable=x, onvalue=1, offvalue=0, command=display)
checkbox1.pack()
checkbox1.config(font=('Arial', 20))
checkbox1.config(fg='blue3')
checkbox1.config(bg='black')
checkbox1.config(activeforeground='blue3')
checkbox1.config(activebackground='black')

img1= (Image.open("images/python_logo.png"))
resized_image1= img1.resize((50,50), Image.LANCZOS)
new_image1 = ImageTk.PhotoImage(resized_image1)

checkbox1.config(image=new_image1, compound='left')
checkbox1.config(padx=25, pady=10, width=250, height=50)
checkbox1.config(anchor='w')

# Checkbox 2
checkbox2 = Checkbutton(window, text='Java',variable=y, onvalue=1, offvalue=0, command=display)
checkbox2.pack()
checkbox2.config(font=('Arial', 20))
checkbox2.config(fg='blue3')
checkbox2.config(bg='black')
checkbox2.config(activeforeground='blue3')
checkbox2.config(activebackground='black')

img2= (Image.open("images/java_logo.png"))
resized_image2= img2.resize((50,50), Image.LANCZOS)
new_image2 = ImageTk.PhotoImage(resized_image2)

checkbox2.config(image=new_image2, compound='left')
checkbox2.config(padx=25, pady=10, width=250, height=50)
checkbox2.config(anchor='w')


window.mainloop()