# importing Libraries

import random
import string
from tkinter import *
import pyperclip

# initialize window

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")
root.configure(background='teal')

# heading
heading = Label(root,background='teal', text='PASSWORD GENERATOR', font='calibri 15 bold').pack()
Label(root, text='avarma030', font='arial 10').pack(side=BOTTOM)

# select password length
pass_label = Label(root,background='teal', text='Select Password Length', font='arial 11 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=6, to_=32, textvariable=pass_len, width=15).pack()

# define function

pass_str = StringVar()

def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# button

Button(root, text="Generate Password", command=Generator).pack(pady=5)

Entry(root, textvariable=pass_str, width=20).pack()


# function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
