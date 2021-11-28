from tkinter import *
from math import *
from datetime import datetime


root = Tk()

root.title("Calculator by Tuna Peker")
root.iconbitmap("D:/calculator.ico")


def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def clear():
    entry.delete(0, END)


def add():
    a = entry.get()
    global first_number
    global type1
    type1 = "addition"
    first_number = float(a)
    entry.delete(0, END)


def divide():
    a = entry.get()
    global first_number
    global type1
    type1 = "division"
    first_number = float(a)
    entry.delete(0, END)


def multiply():
    a = entry.get()
    global first_number
    global type1
    type1 = "multiplication"
    first_number = float(a)
    entry.delete(0, END)


def subtract():
    a = entry.get()
    global first_number
    global type1
    type1 = "subtraction"
    first_number = float(a)
    entry.delete(0, END)


def equal():
    if type1 == "addition":
        b = entry.get()
        global second_number
        second_number = float(b)
        total = float(first_number + second_number)
        entry.delete(0, END)
        entry.insert(0, total)

    if type1 == "subtraction":
        b = entry.get()
        global third_number
        third_number = float(b)
        total = float(first_number - third_number)
        entry.delete(0, END)
        entry.insert(0, total)

    if type1 == "multiplication":
        b = entry.get()
        global c
        c = float(b)
        total = float(first_number * c)
        entry.delete(0, END)
        entry.insert(0, total)

    if type1 == "division":
        b = entry.get()
        global d
        d = float(b)
        total = first_number / d
        ftotal = float(total)
        entry.delete(0, END)
        entry.insert(0, ftotal)


def root1():
    a = float(entry.get())
    a_root = float(sqrt(a))
    entry.delete(0, END)
    entry.insert(0, a_root)


def pi_button():
    entry.delete(0, END)
    entry.insert(0, pi)


def euler():
    entry.delete(0, END)
    entry.insert(0, e)


def point():
    a = entry.get()
    count = 0

    for i in a:
        if i == ".":
            count += 1

    if count == 0:
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, "{}.".format(current))


def absolute_value():
    a = float(entry.get())
    entry.delete(0, END)
    entry.insert(0, abs(a))


def factorial_number():
    a = float(entry.get())
    entry.delete(0, END)
    entry.insert(0, factorial(a))

entry = Entry(root, width=43, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

button0 = Button(text="0", padx=40, pady=20, command=lambda: click(0))
button0.grid(row=4, column=0)

button1 = Button(text="1", padx=40, pady=20, command=lambda: click(1))
button1.grid(row=3, column=0)

button2 = Button(text="2", padx=40, pady=20, command=lambda: click(2))
button2.grid(row=3, column=1)

button3 = Button(text="3", padx=40, pady=20, command=lambda: click(3))
button3.grid(row=3, column=2)

button4 = Button(text="4", padx=40, pady=20, command=lambda: click(4))
button4.grid(row=2, column=0)

button5 = Button(text="5", padx=40, pady=20, command=lambda: click(5))
button5.grid(row=2, column=1)

button6 = Button(text="6", padx=40, pady=20, command=lambda: click(6))
button6.grid(row=2, column=2)

button7 = Button(text="7", padx=40, pady=20, command=lambda: click(7))
button7.grid(row=1, column=0)

button8 = Button(text="8", padx=40, pady=20, command=lambda: click(8))
button8.grid(row=1, column=1)

button9 = Button(text="9", padx=40, pady=20, command=lambda: click(9))
button9.grid(row=1, column=2)

button_equals = Button(text="=", padx=88, pady=20, command=equal)
button_equals.grid(row=4, column=1, columnspan=2)

button_clear = Button(text="Clear", padx=79, pady=20, command=clear)
button_clear.grid(row=6, column=1, columnspan=2)

button_addition = Button(text="+", padx=39, pady=20, command=add)
button_addition.grid(row=1, column=3)

button_subtraction = Button(text="-", padx=40, pady=20, command=subtract)
button_subtraction.grid(row=2, column=3)

button_division = Button(text="/", padx=40, pady=20, command=divide)
button_division.grid(row=3, column=3)

button_multiplication = Button(text="x", padx=40, pady=20, command=multiply)
button_multiplication.grid(row=4, column=3)

button_root = Button(text="√", padx=39, pady=20, command=root1)
button_root.grid(row=6, column=0)

button_pi = Button(text="π", padx=40, pady=20, command=pi_button)
button_pi.grid(row=7, column=1)

button_euler = Button(text="e", padx=40, pady=20, command=euler)
button_euler.grid(row=7, column=2)

button_point = Button(text=".", padx=41, pady=20, command=point)
button_point.grid(row=6, column=3)

button_abs = Button(text="lxl", padx=37, pady=20, command=absolute_value)
button_abs.grid(row=7, column=0)

button_factorial = Button(text="x!", padx=39, pady=20, command=factorial_number)
button_factorial.grid(row=7, column=3)

button_exit = Button(root, text="Exit", command=root.quit, anchor=E, bd=1)
button_exit.grid(row=8, column=3, sticky=E)

now = datetime.now()
now_time = datetime.strftime(now, "%X")
label1 = Label(root, text="{}".format(now_time))
label1.grid(row=8, column=0, columnspan=2)

root.mainloop()
