# -*- coding: utf-8 -*-
"""
@author: avarma030
"""

# importing Libraries

import random
import string
from tkinter import *
import pyperclip


# initialize window

gui = Tk()
gui.geometry("400x400")
gui.resizable(0, 0)
gui.title("Password Generator")
gui.configure(background = 'teal')


# heading for GUI

heading = Label(gui, background = 'teal', text = 'RANDOM PASSWORD GENERATOR', font = 'calibri 15 bold').pack()
Label(gui, text = 'avarma030', font = 'arial 10').pack(side=BOTTOM)


# select password length

pass_label = Label(gui, background = 'teal', text = 'Select Password Length', font = 'arial 11 bold').pack()
pass_len = IntVar()
length = Spinbox(gui, from_ = 6, to_ = 32, textvariable = pass_len, width = 15).pack()


# define password generator

pass_str = StringVar()

def pass_generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) \
                   + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice \
                   (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


# creating the button

Button(gui, text="Generate Password", command=pass_generator).pack(pady=5)
Entry(gui, textvariable=pass_str, width=20).pack()


# function for copying password

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(gui, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)


# loop to run program
gui.mainloop()
