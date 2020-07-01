import tkinter
from tkinter import *


# -----------------------------FUNCTIONS--------------------


def clear():
    label_value.set("")


def set_text(toadd):
    if delete["state"] == 'disabled':
        clear()

    delete["state"] = 'normal'
    from_label = str(display.cget("text")) + toadd
    label_value.set(from_label)


def del_function():
    from_label = display.cget("text")

    print("del")
    if len(str(from_label)) == 1:
        delete["state"] = 'disabled'

    from_label = str(from_label[:-1])
    label_value.set(from_label)


def operation(operand):

    global last_operand, before_operation
    before_operation = ""

    last_operand = operand

    from_label = display.cget("text")
    clear()

    before_operation = float(from_label)


def equals_function():
    global equal

    if display.cget("text") != "":
        if last_operand == '+':
            equal = before_operation + float(display.cget("text"))

        elif last_operand == '-':
            equal = before_operation - float(display.cget("text"))

        elif last_operand == '*':
            equal = before_operation * float(display.cget("text"))

        elif last_operand == "/":
            equal = before_operation / float(display.cget("text"))

        label_value.set(equal)


# ------------------------------Class---------------------------


class Calculator():

    def __init__(self, window):
        window.geometry("325x427")
        window.title("The Hilarious Calculator")
        global label_value
        label_value = StringVar()
        global display

        display = Label(window, width=29, bg="#494949", textvariable=label_value, fg="white", font=("Calibri", 16),
                        anchor="se")
        display.grid(ipady=55, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")

        Clear = Button(window, text="C", width=7, height=2, bg="#494949", fg="white", border=0, relief=GROOVE,
                       font=('Helvetica', '14'), command=clear)
        Clear.grid(row=1, column=0)

        pi = Button(window, text="π", width=7, height=2, bg="#494949", fg="white", border=0, relief=GROOVE,
                    font=('Helvetica', '14'))
        pi.grid(row=1, column=1)

        plusminus = Button(window, text="+/-", width=7, height=2, bg="#494949", fg="white", border=0, relief=GROOVE,
                           font=('Helvetica', '14'))
        plusminus.grid(row=1, column=2)

        division = Button(window, text="/", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: operation("/"))
        division.grid(row=1, column=3)

        # ------------------------------------------------------------------------

        seven = Button(window, text="7", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: set_text("7"))
        seven.grid(row=2, column=0)

        eight = Button(window, text="8", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: set_text("8"))
        eight.grid(row=2, column=1)

        nine = Button(window, text="9", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                      command=lambda: set_text("9"))
        nine.grid(row=2, column=2)

        multi = Button(window, text="X", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: operation("*"))
        multi.grid(row=2, column=3)

        # ------------------------------------------------------------------------

        four = Button(window, text="4", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                      command=lambda: set_text("4"))
        four.grid(row=3, column=0)

        five = Button(window, text="5", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                      command=lambda: set_text("5"))
        five.grid(row=3, column=1)

        six = Button(window, text="6", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                     command=lambda: set_text("6"))
        six.grid(row=3, column=2)

        minus = Button(window, text="-", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: operation("-"))
        minus.grid(row=3, column=3)

        # --------------------------------------------------------------------------

        one = Button(window, text="1", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                     command=lambda: set_text("1"))
        one.grid(row=4, column=0)

        two = Button(window, text="2", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                     command=lambda: set_text("2"))
        two.grid(row=4, column=1)

        three = Button(window, text="3", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: set_text("3"))
        three.grid(row=4, column=2)

        plus = Button(window, text="+", width=7, height=2, bg="#5E4BB6", fg="white", border=0, font=('Helvetica', '14'),
                      command=lambda: operation("+"))
        plus.grid(row=4, column=3)

        # --------------------------------------------------------------------------

        zero = Button(window, text="0", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                      command=lambda: set_text("0"))
        zero.grid(row=5, column=0)

        dot = Button(window, text=".", width=7, height=2, bg="#494949", fg="white", border=0, font=('Helvetica', '14'),
                     command=lambda: set_text("."))
        dot.grid(row=5, column=1)

        global delete
        delete = Button(window, text="del", width=7, height=2, bg="#494949", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda: del_function())
        delete.grid(row=5, column=2)

        global equals
        equals = Button(window, text="=", width=7, height=2, bg="#FEC208", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda: equals_function())
        equals.grid(row=5, column=3)


window = tkinter.Tk()
window.resizable(0, 0)
obj = Calculator(window)
window.mainloop()
