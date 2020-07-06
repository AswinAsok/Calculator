import tkinter
from tkinter import *
from math import *


class Calculator:

    def sqroot(self):
        if self.display.cget("text") != "":
            self.label_valueall.set(self.displayall.cget("text") + "sqrt(" + str(self.display.cget("text")) + ")")
            self.label_value.set("")

    def square(self):
        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.squared = True
            self.label_valueall.set(
                self.displayall.cget("text") + str(float(self.display.cget("text")) * float(self.display.cget("text"))))
            self.label_value.set("")

    def reciprocal(self):
        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.label_valueall.set(self.displayall.cget("text") + "1/(" + str(self.display.cget("text")) + ")")
            self.label_value.set("")

    def negate(self):

        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if self.display.cget("text") != "":
            self.label_value.set(str(float(self.display.cget("text")) * -1))

    def dot_operator(self):

        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if (self.display.cget("text") == "" or self.display.cget("text")[-1] != '.' and str(
                self.display.cget("text")).count(".") < 1):
            self.label_value.set(self.display.cget("text") + ".")

    def delete(self):

        if (self.display.cget("text") == "0"):
            return

        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if not self.equals_clicked:
            if not self.equals_clicked:
                self.label_value.set(str(self.display.cget("text")[:-1]))

    def clear(self):

        self.label_value.set("0")
        self.label_valueall.set("")

    def pi(self):
        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if (self.display.cget("text") != ""):
            self.label_value.set(str(float(self.display.cget("text")) * 3.14))

    def set_text(self, toadd):

        if self.displayall.cget("text")!="":
            if  (toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/") and self.displayall.cget("text")[-1]==")":
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
            elif self.displayall.cget("text")[-1]==")" and toadd == ")":
                count1 = int(str(self.displayall.cget("text")).count("("))
                count2 = int(str(self.displayall.cget("text")).count(")"))
                if count2<count1:
                    self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)

        if (self.display.cget("text") == "." and self.displayall.cget("text") == ""):
            return

        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if self.equals_clicked and self.display.cget("text") != "" and toadd.isdigit():
            self.label_value.set("")

        self.equals_clicked = False

        if not (toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/" or toadd == "(" or toadd == ")"):
            if self.display.cget("text") == "0":
                self.label_value.set("")
            self.label_value.set(str(self.display.cget("text")) + toadd)

        if toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/" or toadd == "(" or toadd == ")":

            if toadd != "(" or toadd != ")":
                if self.displayall.cget("text") != "" and self.displayall.cget("text")[
                    -1] == toadd and self.display.cget("text") == "":
                    return

            if toadd == "(" or toadd == ")" and self.display.cget("text") == "0" and self.displayall.cget("text") == "":
                self.label_value.set("")
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)

            if self.displayall.cget("text") != toadd and self.display.cget("text") != "0" and self.display.cget(
                    "text") != "" or self.squared:
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
                self.label_value.set("")
                self.last_operand = toadd
                self.squared = False


        if self.display.cget("text") == "" and toadd != self.last_operand and self.displayall.cget("text") != "" and not self.squared:
            if self.displayall.cget("text")[-1] != "(" and self.displayall.cget("text")[-1] != ")":
                self.label_valueall.set(self.displayall.cget("text")[0:-1] + toadd)
                self.last_operand = toadd

    def equals_function(self):

        if self.displayall.cget("text") == "" or self.display.cget("text") == ".":
            return

        if self.displayall.cget("text") != "" and self.displayall.cget("text")[-1].isdigit() or self.display.cget(
                "text") != "" or self.displayall.cget("text")[-1] == ")":
            self.equals_clicked = True
            self.label_valueall.set(self.displayall.cget("text") + self.display.cget("text"))
            try:
                self.label_value.set(eval(self.displayall.cget("text")))
            except ZeroDivisionError:
                self.label_value.set("Cannot Divide By Zero")
                self.equals_clicked = False
            self.label_valueall.set("")

    def __init__(self, window):
        window.geometry("341x495")
        window.title("The Hilarious Calculator")
        self.equals_clicked = False
        self.squared = False
        self.label_value = StringVar()
        self.label_valueall = StringVar()
        self.last_operand = ""

        self.displayall = Label(window, width=30, bg="#5A5A5A", textvariable=self.label_valueall, fg="white",
                                font=("Calibri", 16), anchor="se")
        self.displayall.grid(row=0, ipady=14, columnspan=6, rowspan=1, padx=0, pady=0, sticky="W")

        self.display = Label(window, width=21, bg="#5A5A5A", textvariable=self.label_value, fg="white",
                             font=("Calibri", 24), anchor="e")
        self.label_value.set("0")
        self.display.grid(row=1, ipady=16, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")
        # -------------------------------------------------------------------------------------

        lbracket = Button(window, text="(", width=3, height=2, bg="#494949", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: obj.set_text("("))
        lbracket.grid(row=2, column=0, pady=1, padx=1, sticky="W")

        rbracket = Button(window, text=")", width=3, height=2, bg="#494949", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: obj.set_text(")"))
        rbracket.grid(row=2, column=0, pady=1, padx=1, stick="E")

        sqroot = Button(window, text="√", width=7, height=2, bg="#494949", fg="white", border=0,
                        font=('Helvetica', '14'), command=lambda: obj.sqroot())
        sqroot.grid(row=2, column=1)

        square = Button(window, text="x²", width=7, height=2, bg="#494949", fg="white", border=0,
                        relief=GROOVE, font=('Helvetica', '14'), command=lambda: obj.square())
        square.grid(row=2, column=2)

        reciprocal = Button(window, text="1/x", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                            font=('Helvetica', '14'), command=lambda: obj.reciprocal())
        reciprocal.grid(row=2, column=3)

        # -------------------------------------------------------------------------------------

        Clear = Button(window, text="C", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.clear())
        Clear.grid(row=3, column=0, pady=1, padx=1)

        pi = Button(window, text="π", width=7, height=2, bg="#494949", fg="white", border=0,
                    font=('Helvetica', '14'), command=lambda: obj.pi())
        pi.grid(row=3, column=1)

        plusminus = Button(window, text="+/-", width=7, height=2, bg="#494949", fg="white", border=0,
                           relief=GROOVE, font=('Helvetica', '14'), command=lambda: obj.negate())
        plusminus.grid(row=3, column=2)

        division = Button(window, text="/", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: obj.set_text("/"))
        division.grid(row=3, column=3)

        # ------------------------------------------------------------------------

        seven = Button(window, text="7", width=7, height=2, bg="#404040", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("7"))
        seven.grid(row=4, column=0, pady=1, padx=1)

        eight = Button(window, text="8", width=7, height=2, bg="#404040", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("8"))
        eight.grid(row=4, column=1)

        nine = Button(window, text="9", width=7, height=2, bg="#404040", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("9"))
        nine.grid(row=4, column=2)

        multi = Button(window, text="X", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("*"))
        multi.grid(row=4, column=3)

        # ------------------------------------------------------------------------

        four = Button(window, text="4", width=7, height=2, bg="#404040", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("4"))
        four.grid(row=5, column=0, pady=1, padx=1)

        five = Button(window, text="5", width=7, height=2, bg="#404040", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("5"))
        five.grid(row=5, column=1)

        six = Button(window, text="6", width=7, height=2, bg="#404040", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("6"))
        six.grid(row=5, column=2)

        minus = Button(window, text="-", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("-"))
        minus.grid(row=5, column=3)

        # --------------------------------------------------------------------------

        one = Button(window, text="1", width=7, height=2, bg="#404040", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("1"))
        one.grid(row=6, column=0, pady=2, padx=1)

        two = Button(window, text="2", width=7, height=2, bg="#404040", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("2"))
        two.grid(row=6, column=1)

        three = Button(window, text="3", width=7, height=2, bg="#404040", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("3"))
        three.grid(row=6, column=2)

        plus = Button(window, text="+", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("+"))
        plus.grid(row=6, column=3)

        # --------------------------------------------------------------------------

        zero = Button(window, text="0", width=7, height=2, bg="#404040", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("0"))
        zero.grid(row=7, column=1, pady=1, padx=1)

        dot = Button(window, text=".", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.dot_operator())
        dot.grid(row=7, column=0)

        delete = Button(window, text="\u232b", width=7, height=2, bg="#494949", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda: obj.delete())
        delete.grid(row=7, column=2)

        equals = Button(window, text="=", width=7, height=2, bg="#FEC208", border=0, fg="black",
                        font=('Helvetica', '14'), command=lambda: obj.equals_function())
        equals.grid(row=7, column=3, padx=2)


window = tkinter.Tk()
window.resizable(0, 0)
window.attributes('-alpha', 0.98)
window.configure(bg="#5A5A5A")
obj = Calculator(window)
window.mainloop()
