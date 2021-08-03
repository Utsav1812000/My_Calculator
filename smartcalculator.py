from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title('My Calculator')
#screen.geometry('365x490')
screen.configure(bg='royal blue')
screen.iconbitmap('Calculator.ico')
screen.maxsize(width=460,height=490)
screen.minsize(width=362,height=490)
def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong!',parent=screen)
    
def sin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Try again something is wrong!', parent=screen)

def cos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except :
        messagebox.showinfo('Notification', 'Try again something is wrong!', parent=screen)

def tan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except :
        messagebox.showinfo('Notification', 'Try again something is wrong!', parent=screen)
def log():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except :
        messagebox.showinfo('Notification', 'Try again something is wrong!', parent=screen)
######################################## Binding Functions ###################################################

def on_enter9(e):
    btn9.configure(bg='pink')

def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='pink')

def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter7(e):
    btn7.configure(bg='pink')

def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='pink')

def on_leave6(e):
    btn6.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='pink')

def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='pink')

def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='pink')

def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='pink')

def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='pink')

def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='pink')

def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enterdot(e):
    btndot.configure(bg='pink')

def on_leavedot(e):
    btndot.configure(bg='powder blue')


####################################### Ending of Binding Functions ###########################################

tex = StringVar()
operator = ''

entry1 = Entry(screen,bg='orange',font=('arial',20,'italic bold'),bd='30',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(7),
              activebackground='green',activeforeground='white',bg='powder blue')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(8),
              activebackground='green',activeforeground='white',bg='powder blue')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(9),
              activebackground='green',activeforeground='white',bg='powder blue')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click('+'),
                activebackground='green',activeforeground='white',bg='tomato')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(4),
              activebackground='green',activeforeground='white',bg='powder blue')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(5),
              activebackground='green',activeforeground='white',bg='powder blue')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(6),
              activebackground='green',activeforeground='white',bg='powder blue')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=18,pady=15,command=lambda:click('-'),
                activebackground='green',activeforeground='white',bg='tomato')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(1),
              activebackground='green',activeforeground='white',bg='powder blue')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(2),
              activebackground='green',activeforeground='white',bg='powder blue')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(3),
              activebackground='green',activeforeground='white',bg='powder blue')
btn3.grid(row=3,column=2)

btnmul = Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=17,pady=15,command=lambda:click('*'),
                activebackground='green',activeforeground='white',bg='tomato')
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:click(0),
              activebackground='green',activeforeground='white',bg='powder blue')
btn0.grid(row=4,column=0)

btndot = Button(screen,text='.',font=('arial',20,'italic bold'),bd=8,padx=18,pady=15,command=lambda:click('.'),
              activebackground='green',activeforeground='white',bg='powder blue')
btndot.grid(row=4,column=1)

btnclear = Button(screen,text='C',font=('arial',18,'italic bold'),bd=8,padx=18,pady=15,command=lambda:clear(),
                  activebackground='green',activeforeground='white',bg='dark violet')
btnclear.grid(row=0,column=4)

btnsin = Button(screen,text='sin',font=('arial',18,'italic bold'),bd=8,padx=10,pady=17,command=lambda:sin(),
                  activebackground='green',activeforeground='white',bg='dark violet')
btnsin.grid(row=1,column=4)

btncos = Button(screen,text='cos',font=('arial',18,'italic bold'),bd=8,padx=8,pady=17,command=lambda:cos(),
                  activebackground='green',activeforeground='white',bg='dark violet')
btncos.grid(row=2,column=4)


btnequal = Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=15,pady=15,command=lambda:equal(),
                  activebackground='purple',activeforeground='white',bg='green')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=18,pady=15,command=lambda:click('/'),
                activebackground='green',activeforeground='white',bg='tomato')
btndiv.grid(row=4,column=3)

btntan = Button(screen,text='tan',font=('arial',18,'italic bold'),bd=8,padx=8,pady=17,command=lambda:tan(),
                  activebackground='green',activeforeground='white',bg='dark violet')
btntan.grid(row=3,column=4)

btnlog = Button(screen,text='log',font=('arial',18,'italic bold'),bd=8,padx=8,pady=17,command=lambda:log(),
                  activebackground='green',activeforeground='white',bg='dark violet')
btnlog.grid(row=4,column=4)


######################################### Button Binding ###########################################################

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btndot.bind('<Enter>',on_enterdot)
btndot.bind('<Leave>',on_leavedot)

screen.mainloop()