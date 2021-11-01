from tkinter import *
from random import randint


root = Tk()

root.title('tits')
frame = Frame(relief=SUNKEN, borderwidth=3)
frame.pack(ipady=5)

def r():
    n=entry.get()
    if n.isdigit() and n!='0':
        labelrandom['text'] = randint(1, int(n))
        labelrandom.pack()
    else:
        labelrandom['text'] = 'smtg wrong'
        labelrandom.pack()

labelrandom = Label()

entry = Entry(master=frame, width=5)
entry.pack(side=RIGHT, padx=5, ipadx=10)

btn_submit = Button(frame, text="Submit", command=r)
btn_submit.pack(side=RIGHT, padx=5, ipadx=10)


root.mainloop()
