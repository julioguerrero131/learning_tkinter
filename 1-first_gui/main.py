from tkinter import *

# widget = GUI Elements: buttons, labels, images
# windows = container to hold the widget

window = Tk() # initiate instance of a window
window.geometry("420x420")
window.title("First GUI Program c:")

# image to PhotoImage
icon = PhotoImage(file="1-first_gui\images\python_logo.png")
window.iconphoto(True, icon)

window.config(background="blue4") # names or hex-codes

window.mainloop() # initiate window