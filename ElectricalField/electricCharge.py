from tkinter import *
import subprocess
from tkinter import messagebox
# Built-in
from ElectricalField import EField

# Default settings
root = Tk()
root.title('میدان الکتریکی وارد بر ذره باردار')
root.geometry('500x400')
root.resizable(0, 0)
e = EField()

# Labels
Label(root, text='کنید وارد را دارید که مقادیری', font = "Helvetica 22 bold italic").place(x=115, y=30)

texts = [': الکتریکی بار اندازه', ': فاصله', ': الکتریک دی ثابت']
FONT = "Helvetica 15 bold"
y = 100
for i in range(3):
    Label(root, text=texts[i], font = FONT).place(x=335, y=y)
    y += 40
lbl = StringVar()
Label(root, textvariable = lbl, font = FONT).place(x=335, y=302)

# Outputs
var = StringVar()
Label(root, textvariable = var, font = FONT).place(x=235, y=302)

# Functions
def clicked(n):
    if n == 2:
        k['state'] = NORMAL
    if n ==1:
        k['state'] = DISABLED

def returnToMain():
    root.withdraw()
    subprocess.run(["python", "main.py"])

def calculate():
    q = bar.get()
    r = distance.get()
    number = num.get()
    k2 = k.get()
    if q == "" or r == "" or ((number == 2 and k2 == "") or (number != 1 and number != 2)):
        messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    else:
        try:
            if number == 1:
                m = e.eField_inGeneral(k = 1, electricCharge = int(q), distance = int(r))
                var.set(m)
                lbl.set(':نهایی عدد')
            else:
                m = e.eField_inGeneral(k = int(k2), electricCharge = int(q), distance = int(r))
                var.set(m)
                lbl.set(':نهایی عدد')
        except:
            messagebox.showerror(title='Operation failed', message='فاصله نمیتواند 0 باشد')

# Inputs
bar = Entry(root, width=10)
distance = Entry(root, width=10)
k = Entry(root, state = DISABLED, width=10)
num = IntVar()
rb1 = Radiobutton(root, text='خلاء', variable = num, value = 1, command=lambda:clicked(1))
rb2 = Radiobutton(root, text=':سایر', variable = num, value = 2, command=lambda:clicked(2))

bar.place(x=250, y=108)
distance.place(x=250, y=148)
rb1.place(x=260, y=188)
rb2.place(x=190, y=188)
k.place(x=140, y=188)

# Buttons
Button(root, text='محاسبه', command=calculate).place(x=296, y=240)
Button(root, text='بازگشت', command=returnToMain).place(x=194, y=240)
Button(root, text='خروج', command=exit).place(x=92, y=240)

entries = [bar, distance, k]
def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        for i in range(3):
            entries[i].delete(0, len(entries[i].get()))
        rb1.deselect()
        rb2.deselect()
        lbl.set('')
        var.set('')

Button(root, text='reset', command=reset).place(x=398, y=240)

mainloop()