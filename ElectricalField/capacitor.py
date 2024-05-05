from tkinter import *
import subprocess
from tkinter import messagebox
# Built-in
from ElectricalField import EField

# Default settings
root = Tk()
root.title('میدان الکتریکی بین صفحات خازن')
root.geometry('500x500')
root.resizable(0, 0)
e = EField()

# Labels
Label(root, text='کنید وارد را دارید که مقادیری', font = "Helvetica 22 bold italic").place(x=115, y=30)

texts = [': الکتریکی بار', ': خازن صفحات مساحت', ': ولتاژ', ": خازن صفحات بین فاصله", ': الکتریک دی ثابت']
FONT = "Helvetica 15 bold"
y = 100
for i in range(5):
    Label(root, text=texts[i], font = FONT).place(x=335, y=y)
    y += 40
lbl = StringVar()
Label(root, textvariable = lbl, font = FONT).place(x=335, y=402)

# Outputs
var = StringVar()
Label(root, textvariable = var, font = FONT).place(x=200, y=402)

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
    if (bar.get() == "" or area.get() == "" or ((num.get() == 2 and k.get() == "") or (num.get() != 1 and num.get() != 2))):
        if voltage.get() != "" and distance.get() != "":
            try:
                m = e.eField_capacitor_2(voltage = int(voltage.get()), distance = int(distance.get()))
                var.set(m)
                lbl.set(':نهایی عدد')
            except:
                messagebox.showerror(title='Operation failed', message='فاصله ی بین صفحات نمیتواند 0 باشد')
        else:
            messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
    elif voltage.get() == "" or distance.get() == "":
        if (bar.get() == "" or area.get() == "" or ((num.get() == 2 and k.get() == "") or (num.get() != 1 and num.get() != 2))) or (num.get() == 2 and k.get() == ""):
            messagebox.showerror(title='Operation failed', message='داده های کافی نیست')
        else:
            try:
                if num.get() == 1:
                    kNew = 1
                elif num.get() == 2:
                    kNew = int(k.get())
                m = e.eField_capacitor_1(electricCharge = int(bar.get()), k = kNew, area = int(area.get()))
                m *= (10**12)
                var.set(f"{m} x 10**-12")
                lbl.set('نهایی عدد')    
            except:
                messagebox.showerror(title='Operation failed', message='ثابت دی الکتریک یا مساحت نمیتوانند 0 باشند')
    else:
        messagebox.showerror(title='Operation failed', message='داده ها مطابقت ندارند')
       

# Inputs
bar = Entry(root, width=10)
area = Entry(root, width=10)
voltage = Entry(root, width=10)
distance = Entry(root, width=10)
k = Entry(root, state = DISABLED, width=10)
num = IntVar()
rb1 = Radiobutton(root, text='خلاء', variable = num, value = 1, command=lambda:clicked(1))
rb2 = Radiobutton(root, text=':سایر', variable = num, value = 2, command=lambda:clicked(2))

bar.place(x=250, y=108)
area.place(x=250, y=148)
voltage.place(x=250, y=188)
distance.place(x=250, y=228)
rb1.place(x=260, y=268)
rb2.place(x=190, y=268)
k.place(x=140, y=268)

# Buttons
Button(root, text='محاسبه', command=calculate).place(x=296, y=335)
Button(root, text='بازگشت', command=returnToMain).place(x=194, y=335)
Button(root, text='خروج', command=exit).place(x=92, y=335)

entries = [bar, area, voltage, distance, k]
def reset():
    res = messagebox.askyesno(title='Warning', message='آیا مطمئنید که می خواهید داده ها را پاک کنید؟')
    if res == True:
        for i in range(5):
            entries[i].delete(0, len(entries[i].get()))
        rb1.deselect()
        rb2.deselect()
        lbl.set('')
        var.set('')

Button(root, text='reset', command=reset).place(x=398, y=335)

mainloop()