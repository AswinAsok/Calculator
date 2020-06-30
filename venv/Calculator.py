import tkinter
from tkinter import *


# -----------------------------FUNCTIONS--------------------


def clear():
    var.set("")


def set_text(toadd):
    if delete["state"] == 'disabled':
        clear()

    delete["state"] = 'normal'
    new_text = str(display.cget("text")) + toadd
    var.set("")
    var.set(new_text)


def del_function():
    new_text = display.cget("text")
    if len(str(new_text)) == 1:
        delete["state"] = 'disabled'
    var.set("")
    new_text = str(new_text[:-1])
    var.set(new_text)


def operation(operand):
    global last_operand, current_display
    last_operand = ""
    last_operand = operand
    equals["state"] = 'normal'
    current_display = display.cget("text")
    var.set("")


def equals_function():

    delete["state"] = 'disabled'
    global current_display

    from_display = display.cget("text")
    if from_display != "":
        if from_display == "":
            from_display = current_display

        if last_operand == "+":
            current_display = float(current_display) + float(from_display)

        elif last_operand == "-":
            current_display = float(current_display) - float(from_display)

        elif last_operand == "*":
            current_display = float(current_display) * float(from_display)

        elif last_operand == "/":
            current_display = float(current_display) / float(from_display)

        var.set("")
        var.set(current_display)


# ------------------------------Class---------------------------


class Calculator():

    def __init__(self, window):
        window.geometry("313x412")
        window.title("The Hilarious Calculator")
        global var
        var = StringVar()
        global display
        display = Label(window, width=28, fg="#494949", textvariable=var, bg="white", font=("Calibri", 16), anchor="e")
        display.grid(ipady=55, padx=0, pady=0, columnspan=4, rowspan=1)

        Clear = Button(window, text="C", width=10, height=3, bg="#494949", fg="white",border=0, relief = GROOVE ,command=clear)
        Clear.grid(row=1, column=0, sticky="W",pady=1,padx=0)

        pi = Button(window, text="π", width=10, height=3, bg="#494949", fg="white",border=0,relief = GROOVE)
        pi.grid(row=1, column=1)

        plusminus = Button(window, text="+/-", width=10, height=3, bg="#494949", fg="white",border=0,relief = GROOVE)
        plusminus.grid(row=1, column=2)

        division = Button(window, text="/", width=10, height=3, bg="#5E4BB6", fg="white",border=0,
                          command=lambda: operation("/"))
        division.grid(row=1, column=3)

        # ------------------------------------------------------------------------

        seven = Button(window, text="7", width=10, height=3, bg="#494949", fg="white",border=0,command=lambda: set_text("7"))
        seven.grid(row=2, column=0, sticky="W",pady=1)
        seven.grid_propagate(False)

        eight = Button(window, text="8", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("8"))
        eight.grid(row=2, column=1)

        nine = Button(window, text="9", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("9"))
        nine.grid(row=2, column=2)

        multi = Button(window, text="X", width=10, height=3, bg="#5E4BB6", fg="white",border=0, command=lambda: operation("*"))
        multi.grid(row=2, column=3)

        # ------------------------------------------------------------------------

        four = Button(window, text="4", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("4"))
        four.grid(row=3, column=0, sticky="W",pady=1)

        five = Button(window, text="5", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("5"))
        five.grid(row=3, column=1)

        six = Button(window, text="6", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("6"))
        six.grid(row=3, column=2)

        minus = Button(window, text="-", width=10, height=3, bg="#5E4BB6", fg="white",border=0, command=lambda: operation("-"))
        minus.grid(row=3, column=3)

        # --------------------------------------------------------------------------

        one = Button(window, text="1", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("1"))
        one.grid(row=4, column=0, sticky="W",pady=1)

        two = Button(window, text="2", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("2"))
        two.grid(row=4, column=1)

        three = Button(window, text="3", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("3"))
        three.grid(row=4, column=2)

        plus = Button(window, text="+", width=10, height=3, bg="#5E4BB6", fg="white",border=0, command=lambda: operation("+"))
        plus.grid(row=4, column=3)

        # --------------------------------------------------------------------------

        zero = Button(window, text="0", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("0"))
        zero.grid(row=5, column=0, sticky="W",pady=1)

        dot = Button(window, text=".", width=10, height=3, bg="#494949", fg="white",border=0, command=lambda: set_text("."))
        dot.grid(row=5, column=1)

        global delete
        delete = Button(window, text="del", width=10, height=3, bg="#494949",border=0, fg="white",
                        command=lambda: del_function())
        delete.grid(row=5, column=2)

        global equals
        equals = Button(window, text="=", width=10, height=3, bg="#FEC208",border=0, fg="black",state='disabled',
                        command=lambda: equals_function())
        equals.grid(row=5, column=3)


window = tkinter.Tk()
window.resizable(0,0)
obj = Calculator(window)
window.mainloop()
