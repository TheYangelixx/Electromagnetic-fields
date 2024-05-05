from tkinter import Label, StringVar, Entry, Button, Tk, mainloop
from tkinter import messagebox
import subprocess
# کتابخانه ای که خودم ساختم
from MagneticField import MField

# Default settings
eFlow = Tk()
eFlow.title('میدان مغناطیسی سیم لوله')
eFlow.geometry('500x400')
eFlow.resizable(0, 0)
mgnt = MField()

var = StringVar()
vartxt1 = StringVar()
txt = ': مغناطیسی میدان ی اندازه'

# Functions
def calculateB():
    if i.get() == '' or n.get() == '' or l.get() == '':
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        try:
            iv = int(i.get())
            nv = int(n.get())
            lv = int(l.get())
            result = mgnt.solenoid_mField_intensity(numOfRings = nv, eFlow = iv, length = lv)
            result *= 10**7
            roundNum = round(result, 3)
            var.set(f"{roundNum} x 10**-7")
            vartxt1.set(txt)
        except:
            messagebox.showerror(title='Operation failed', message='طول سیم نمیتواند 0 باشد')

def returnToMain():
    eFlow.withdraw()
    subprocess.run(["python", "main.py"])

def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        i.delete(0, len(i.get()))
        n.delete(0, len(n.get()))
        l.delete(0, len(l.get()))
        vartxt1.set('')
        var.set('')

FONT = "Helvetica 15 bold"

# Labels & Entries & Buttons
Label(eFlow, text='کنید وارد را دارید که مقادیری', font = "Helvetica 16 bold italic").place(x=150, y=30)
Label(eFlow, text=': الکتریکی جریان ی اندازه', font = FONT).place(x=300, y=108)
Label(eFlow, text=': سیم ی ها دور تعداد', font = FONT).place(x=300, y=155)
Label(eFlow, text=': سیم طول', font = FONT).place(x=300, y=202)

textVariables = [vartxt1, var]
posotions = [300, 150]
for i in [0, 1]:
    Label(eFlow, textvariable = textVariables[i], font = FONT).place(x=posotions[i], y=347)

p1 = StringVar()
p2 = StringVar()
p3 = StringVar()

i = Entry(eFlow, textvariable=p1, width=10)
n = Entry(eFlow, textvariable=p2, width=10)
l = Entry(eFlow, textvariable=p3, width=10)
i.place(x=230, y=113)
n.place(x=230, y=207)
l.place(x=230, y=160)

Button(eFlow, text='محاسبه', command=calculateB).place(x=296, y=240)
Button(eFlow, text='بازگشت', command=returnToMain).place(x=194, y=240)
Button(eFlow, text='خروج', command=exit).place(x=92, y=240)
Button(eFlow, text='reset', command=reset).place(x=398, y=240)

mainloop()