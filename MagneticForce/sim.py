from tkinter import *
import subprocess
from tkinter import messagebox
import tkinter.ttk
import os
from PIL import Image
# Built-in
from MagneticForce import MForce

# Default settings
root = Tk()
root.title('نیروی مغناطیسی وارد بر سیم حامل جریان')
root.geometry('500x500')
root.resizable(0, 0)
mgnt = MForce()

var = StringVar()
vartxt1 = StringVar()
var2 = StringVar()
vartxt2 = StringVar()
txt = ': مغناطیسی نیروی ی اندازه'
txtDir = ': مغناطیسی نیروی جهت'

# Labels
Label(root, text='کنید وارد را دارید که مقادیری', font = "Helvetica 22 bold italic").place(x=115, y=30)

texts = [': مغناطیسی میدان', ': الکتریکی جریان ی اندازه', ': سیم طول', ": مغناطیسی میدان و سیم بین زاویه", ': مغناطیسی میدان جهت', ': سیم جهت']
FONT = "Helvetica 15 bold"
y = 100
for i in range(6):
    Label(root, text=texts[i], font = FONT).place(x=280, y=y)
    y += 40

# Outputs
textVariables1 = [vartxt1, var]
posotions = [280, 200]
for i in [0, 1]:
    Label(root, textvariable = textVariables1[i], font = FONT).place(x=posotions[i], y=400)

textVariables2 = [vartxt2, var2]
posotions = [280, 200]
for i in [0, 1]:
    Label(root, textvariable = textVariables2[i], font = FONT).place(x=posotions[i], y=440)

# Functions
def returnToMain():
    root.withdraw()
    subprocess.run(["python", "main.py"])

def calculate():
    if b.get() == '' or i.get() == '' or l.get() == '' or angle.get() == '':
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        bv = int(b.get())
        iv = int(i.get())
        lv = int(l.get())
        anglev = int(angle.get())
        result = mgnt.wire_electromagnetic_force(magneticFieldIntensity = bv, eFlow = iv, length = lv, angle = anglev)
        roundNum = round(result, 3)
        var.set(roundNum)
        vartxt1.set(txt)
        


def calculateDir():
    if fieldDirection.get() == '' or wireDirection.get() == '':
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        fd = fieldDirection.get()
        wd = wireDirection.get()
        res = mgnt.whatDirection(bDir = fd, iDir = wd, id=0)
        vartxt2.set(txtDir)
        var2.set(res)
        if os.path.isfile(os.path.join("result.png")):
            res = messagebox.askyesno(title='باز کردن عکس', message='آیا تمایل دارید که عکس شبیه سازی شده ی فرایند را باز کنید؟')
            if res == True:
                image = Image.open("result.png")
                image.show()
# Inputs
b = Entry(root, width=10)
i = Entry(root, width=10)
l = Entry(root, width=10)
angle = Entry(root, width=10)

b.place(x=210, y=108)
i.place(x=210, y=148)
l.place(x=210, y=188)
angle.place(x=210, y=228)

# Buttons
Button(root, text='محاسبه مقدار', command=calculate).place(x=66, y=350)
Button(root, text='بازگشت', command=returnToMain).place(x=152, y=350)
Button(root, text='خروج', command=exit).place(x=238, y=350)
Button(root, text='محاسبه جهت', command=calculateDir).place(x=324, y=350)

entries = [b, i, l, angle]
def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        for i in range(4):
            entries[i].delete(0, len(entries[i].get()))
        vartxt1.set('')
        var.set('')
        vartxt2.set('')
        var2.set('')
        fieldDirection.set('')
        wireDirection.set('')

Button(root, text='reset', command=reset).place(x=410, y=350)

# Combo box
directions = ['درون سو', 'برون سو', 'آسمان',  'زمین', 'شرق', 'غرب']
fieldDirection = tkinter.ttk.Combobox(root, values=directions, state='readonly')
wireDirection = tkinter.ttk.Combobox(root, values=directions, state='readonly')

fieldDirection.place(x=185,y=268, width=80)
wireDirection.place(x=185,y=308, width=80)

mainloop()