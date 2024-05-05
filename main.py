#  Importing Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Default Settings
root = Tk()
root.title('الکتریسیته و مغناطیس')
root.geometry('600x400')
root.resizable(0, 0)
tab_parent = ttk.Notebook(root)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#e0aaff")
s.map("TNotebook", background= [("selected", "#b486ab")])

var2 = StringVar()
FONT = "Helvetica 16 bold italic"

# Notebooks
home = ttk.Frame(tab_parent)
mFieldInternsity = ttk.Frame(tab_parent)
eFieldInternsity = ttk.Frame(tab_parent)
mForce = ttk.Frame(tab_parent)
eForce = ttk.Frame(tab_parent)
eFlow = ttk.Frame(tab_parent)

tab_parent.add(home, text='خانه')
tab_parent.add(mFieldInternsity, text='میدان مغناطیسی')
tab_parent.add(mForce, text='نیروی مغناطیسی')
tab_parent.add(eFieldInternsity, text='میدان الکتریکی')
tab_parent.add(eForce, text='نیروی الکتریکی')
tab_parent.add(eFlow, text='جریان الکتریکی')

tab_parent.pack(expand=1, fill='both')

# Functions
def btn_Click(n):
    root.withdraw()
    if n == 0:
        subprocess.run(["python", "MagneticField\simLoole.py"])
    elif n == 1:
        subprocess.run(["python", "MagneticField\Ring.py"])
    elif n == 2:
        subprocess.run(["python", "ElectricalField\capacitor.py"])
    elif n == 3:
        subprocess.run(["python", "ElectricalField\electricCharge.py"])
    elif n == 4:
        subprocess.run(["python", "MagneticForce\sim.py"])
    elif n == 5:
        subprocess.run(["python", "MagneticForce\moving_electricCharge.py"])
    elif n == 6:
        subprocess.run(["python", "ElectricalFlow\eFlow.py"])
    else:
        subprocess.run(["python", "ElectricalForce\eForce.py"])

# خانه
Label(home, text="", bg='#7b2cbf').place(x=1, y=320, width=600, height=20)
Label(home, text="", bg='#7b2cbf').place(x=550, y=1, width=20, height=500)
Label(home, text='طرز کار برنامه : از طریق تب ها و سربرگ های بالای برنامه میتوانید به بخش ', fg='#240046').place(x=130, y= 40)
Label(home, text='مورد نظر بروید. این برنامه در محاسبه ی اندازه ی میدان های مغناطیسی و ', fg='#240046').place(x=135, y=60)
Label(home, text='الکتریکی، نیروی های مغناطیسی و الکتریکی و اندازه ی جریان به شما کمک ', fg='#240046').place(x=132, y=80)
Label(home, text=' میکند و به وسیله ی آن میتوانید عکس شبیه سازی شده ی نیروی مغناطیسی', fg='#240046').place(x=128, y=100)
Label(home, text=' وارد بر سیم حامل جریان یا ذره ی باردار متحرک را استخراج کنید', fg='#240046').place(x=192, y=120)
Label(home, text='در این برنامه باید تمامی مقادیر را برحسب دستگاه بین المللی یکاها وارد کنید', fg='#240046').place(x=126, y=140)
Label(home, text='به این صورت : ').place(x=415, y=160)

Label(home, text='اندازه ی میدان : نیوتون بر کولن', fg='#240046').place(x=300, y= 200)
Label(home, text='اندازه بار الکتریکی : کولن', fg='#240046').place(x=300, y= 220)
Label(home, text='اندازه جریان الکتریکی : آمپر', fg='#240046').place(x=300, y= 240)
Label(home, text='طول : متر', fg='#240046').place(x=300, y= 260)
Label(home, text='زاویه : درجه', fg='#240046').place(x=300, y= 280)
Label(home, text='مساحت : متر مربع', fg='#240046').place(x=130, y= 200)
Label(home, text='ولتاز : ولت', fg='#240046').place(x=130, y= 220)
Label(home, text='مدت زمان : ثانیه', fg='#240046').place(x=130, y= 240)

messagebox.showinfo(title='Information Box', message='یکی از مباحث را از طریق پنجره های بالا انتخاب کنید')

# میدان مفناطیسی
Label(mFieldInternsity, text=':در مغناطیسی میدان', font = FONT).place(x=250, y=30)

img1 = Image.open('images\simLoole.jpg')
new_image1 = img1.resize((195, 195))
simloole = ImageTk.PhotoImage(new_image1)

img2 = Image.open('images\halqe.png')
new_image2 = img2.resize((195, 195))
halqe = ImageTk.PhotoImage(new_image2)

Label(mFieldInternsity, image=simloole).place(x=70, y=70)
Label(mFieldInternsity, image=halqe).place(x=335, y=70)

Button(mFieldInternsity, text='سیم لوله حامل جریان الکتریکی', command=lambda: btn_Click(0), bg='#b486ab').place(x=90, y=300)
Button(mFieldInternsity, text='حلقه حامل جریان الکتریکی', command=lambda: btn_Click(1), bg='#b486ab').place(x=360, y=300)

# میدان الکتریکی
Label(eFieldInternsity, text=': الکتریکی میدان', font = FONT).place(x=240, y=30)

img3 = Image.open('images\khazan.png')
new_image3 = img3.resize((195, 195))
khzan = ImageTk.PhotoImage(new_image3)

img4 = Image.open('images\meydanBarZare.jpg')
new_image4 = img4.resize((195, 195))
zarre = ImageTk.PhotoImage(new_image4)

Label(eFieldInternsity, image=khzan).place(x=70, y=70)
Label(eFieldInternsity, image=zarre).place(x=335, y=70)

Button(eFieldInternsity, text='بین صفحات خازن', command=lambda: btn_Click(2), bg='#b486ab').place(x=120, y=300)
Button(eFieldInternsity, text='وارد بر ذره باردار در فاصله معین', command=lambda: btn_Click(3), bg='#b486ab').place(x=352, y=300)

# نیروی مغناطیسی
Label(mForce, text=': بر وارد مغناطیسی نیروی', font = FONT).place(x=240, y=30)

img5 = Image.open('images\sim.png')
new_image5 = img5.resize((195, 195))
sim = ImageTk.PhotoImage(new_image5)

img6 = Image.open('images\magneticFBarzare.jpg')
new_image6 = img6.resize((195, 195))
zareBardar = ImageTk.PhotoImage(new_image6)

Label(mForce, image=sim).place(x=70, y=70)
Label(mForce, image=zareBardar).place(x=335, y=70)

Button(mForce, text='سیم حامل جریان', command=lambda: btn_Click(4), bg='#b486ab').place(x=120, y=300)
Button(mForce, text='ذره باردار متحرک', command=lambda: btn_Click(5), bg='#b486ab').place(x=380, y=300)

# جریان الکتریکی
Label(eFlow, text=': الکتریکی جریان', font = FONT).place(x=240, y=30)

img7 = Image.open('images\jaryan.jpg')
new_image7 = img7.resize((195, 195))
jaryan = ImageTk.PhotoImage(new_image7)

Label(eFlow, image=jaryan).place(x=202.5, y=70)
Button(eFlow, text='محاسبه ی جریان الکتریکی', command=lambda: btn_Click(6), bg='#b486ab').place(x=235, y=300)

# نیروی الکتریکی
Label(eForce, text=': الکتریکی نیروی', font = FONT).place(x=240, y=30)

img8 = Image.open('images\chargeInEField.png')
new_image8 = img8.resize((195, 195))
chargeInEField = ImageTk.PhotoImage(new_image8)

Label(eForce, image=chargeInEField).place(x=202.5, y=70)

Button(eForce, text='میدان بر ذره', command=lambda: btn_Click(7), bg='#b486ab').place(x=265, y=300)

mainloop()