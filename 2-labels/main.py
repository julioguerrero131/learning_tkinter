from tkinter import *

# label = area widget that holds text or/and images within a window

window = Tk()

photo = PhotoImage(
    file='2-labels\images\python_logo.png',
)

label = Label(
    window, 
    text="Hello World",
    font=('Arial', 40, "bold"), 
    fg='#00FF00',
    bg='black',
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound='bottom'
)

label.pack() # top-center
# label.place(x=0,y=0) # position

window.mainloop()

