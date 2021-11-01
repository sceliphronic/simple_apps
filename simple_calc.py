from tkinter import *
root = Tk()
root.title("Address Entry Form")
xyc = []

def calc():
    a = ''
    x = str(xyc[0].get())
    y = str(xyc[1].get())
    c = xyc[2].get()

    if x.isdigit() and y.isdigit() and not (c == '/' and y == '0'):
        x = int(x)
        y = int(y)
        print(x, y, c)
        a1 = (lambda x, y: x + y)
        b2 = (lambda x, y: x - y)
        c3 = (lambda x, y: x * y)
        g4 = (lambda x, y: x / y)
        if len(c) == 1:
            if c == "+":
                a = (a1(x=x, y=y))
            elif c == '-':
                a = (b2(x=x, y=y))
            elif c == '*':
                a = (c3(x=x, y=y))
            elif c == '/':
                a = (g4(x=x, y=y))

        print(a)
        lbl_result["text"] = a
    else:
        lbl_result["text"] = 'smtg wronge'

frm_form = Frame(relief=SUNKEN, borderwidth=3)
frm_form.pack()

labels = [
    "1s number",
    "2d number:",
    "sign",
    ]

for idx, text in enumerate(labels):
    label = Label(master=frm_form, text=text)
    entry = Entry(master=frm_form, width=50)
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)
    xyc.append(entry)

lbl_result = Label(master=root)
lbl_result.pack()

btn_convert = Button(
    master=root,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command = calc
)
btn_convert.pack()

root.mainloop()





