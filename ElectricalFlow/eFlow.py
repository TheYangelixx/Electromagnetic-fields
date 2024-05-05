from tkinter import Label, StringVar, Entry, Button, Tk, mainloop
from tkinter import messagebox
import subprocess

# Deault settings
eFlow = Tk()
eFlow.title('جریان الکتریکی')
eFlow.geometry('500x400')
eFlow.resizable(0, 0)

var = StringVar()
vartxt1 = StringVar()
txt = ': الکتریکی میدان ی اندازه'

# Functions
def calculateFlow():
    if charge.get() == '' or time.get() == '':
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        try:
            num = int(charge.get()) / int(time.get())
            roundNum = round(num, 3)
            var.set(roundNum)
            vartxt1.set(txt)
            return roundNum
        except:
            messagebox.showerror(title='Operation failed', message='مدت زمان نمیتواند 0 باشد')

def returnToMain():
    eFlow.withdraw()
    subprocess.run(["python", "main.py"])

def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        charge.delete(0, len(charge.get()))
        time.delete(0, len(time.get()))
        vartxt1.set('')
        var.set('')

FONT = "Helvetica 15 bold"

# Buttons & Labels & Entries
Label(eFlow, text='کنید وارد را دارید که مقادیری', font = "Helvetica 16 bold italic").place(x=150, y=30)
Label(eFlow, text=': الکتریکی بار اندازه', font = FONT).place(x=300, y=108)
Label(eFlow, text=': زمان مدت', font = FONT).place(x=300, y=155)

textVariables = [vartxt1, var]
posotions = [300, 250]
for i in [0, 1]:
    Label(eFlow, textvariable = textVariables[i], font = FONT).place(x=posotions[i], y=300)

p1 = StringVar()
p2 = StringVar()

charge = Entry(eFlow, textvariable=p1, width=10)
time = Entry(eFlow, textvariable=p2, width=10)
charge.place(x=230, y=113)
time.place(x=230, y=160)

Button(eFlow, text='محاسبه', command=calculateFlow).place(x=296, y=240)
Button(eFlow, text='بازگشت', command=returnToMain).place(x=194, y=240)
Button(eFlow, text='خروج', command=exit).place(x=92, y=240)
Button(eFlow, text='reset', command=reset).place(x=398, y=240)

mainloop()