from tkinter import Label, StringVar, Entry, Button, Tk, mainloop
from tkinter import messagebox
import subprocess

# تنظیمات اولیه
eForce = Tk()
eForce.title('نیروی الکتریکی')
eForce.geometry('500x400')
eForce.resizable(0, 0)

var = StringVar()
vartxt1 = StringVar()
txt = ': الکتریکی نیروی ی اندازه'

# Functions
def calculateForce():
    if field.get() == '' or q.get() == '':
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        num = round(( int(field.get()) * abs(int(q.get())) ), 2)
        var.set(num)
        vartxt1.set(txt)
        return num

def returnToMain():
    eForce.withdraw()
    subprocess.run(["python", "main.py"])

def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        field.delete(0, len(field.get()))
        q.delete(0, len(q.get()))
        vartxt1.set('')
        var.set('')

FONT = "Helvetica 15 bold"

# Labels & Entries & Buttons
Label(eForce, text='کنید وارد را دارید که مقادیری', font = "Helvetica 16 bold italic").place(x=150, y=30)
Label(eForce, text=': میدان اندازه', font = FONT).place(x=300, y=108)
Label(eForce, text=': الکتریکی بار اندازه', font = FONT).place(x=300, y=155)

textVariables = [vartxt1, var]
posotions = [300, 250]
for i in [0, 1]:
    Label(eForce, textvariable = textVariables[i], font = FONT).place(x=posotions[i], y=300)

Button(eForce, text='محاسبه', command= calculateForce).place(x=296, y=240)
Button(eForce, text='بازگشت', command=returnToMain).place(x=194, y=240)
Button(eForce, text='خروج', command=exit).place(x=92, y=240)
Button(eForce, text='reset', command=reset).place(x=398, y=240)

p3 = StringVar()
p4 = StringVar()

field = Entry(eForce, textvariable=p3, width=10)
q = Entry(eForce, textvariable=p4, width=10)
field.place(x=230, y=113)
q.place(x=230, y=160)

mainloop()