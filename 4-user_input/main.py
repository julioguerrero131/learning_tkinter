from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print(f'Hello {username}!')

def delete():
    entry.delete(0, END) # deletes the line text

def backspace():
    entry.delete(len(entry.get())-1, END) # deletes last character

window = Tk()

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(side='bottom')

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack(side='bottom')

backspace_button = Button(window, text='Backspace', command=backspace)
backspace_button.pack(side='bottom')

entry = Entry()
entry.config(font=('Ink Free', 30))
entry.config(bg='gold')
entry.config(fg='gray')
#entry.insert(0, 'Spongebob')
#entry.config(state=DISABLED) # ACTIVE/DISABLED
entry.config(width=10) # size entry box
entry.config(show='*') # like passwords
entry.pack()

window.mainloop()