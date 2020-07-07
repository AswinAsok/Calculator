import tkinter
from tkinter import *
from math import *


class Calculator:

    def sqroot(self):
        if self.display.cget("text") != "0" and self.display.cget("text") != "":
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

        if self.equals_clicked and self.display.cget("text") != "":
            self.label_value.set("0")
            self.equals_clicked = False

        if (self.display.cget("text") == "Cannot Divide By Zero"):
            self.clear()

        if str(self.display.cget("text")).count(".") < 1:
            if str(self.display.cget("text") == "") or str(self.display.cget("text")[-1] != '.'):
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

        if self.displayall.cget("text") != "":

            if self.displayall.cget("text")[-1] == ")" and toadd == "(":  # "7-(5+4)(" For Fixing
                return

            if (toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/") and self.displayall.cget("text")[
                -1] == ")":
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
            elif self.displayall.cget("text")[-1] == ")" and toadd == ")":
                count1 = int(str(self.displayall.cget("text")).count("("))
                count2 = int(str(self.displayall.cget("text")).count(")"))
                if count2 < count1:
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
                if toadd == ")":
                    if int(str(self.displayall.cget("text")).count("(")) != 0:
                        self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
                if toadd == "(":
                    self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)

            if self.displayall.cget("text") != toadd and self.display.cget("text") != "0" and self.display.cget(
                    "text") != "" or self.squared:
                if self.display.cget("text")[-1] == ".":
                    print("true")
                    return
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
                self.label_value.set("")
                self.last_operand = toadd
                self.squared = False

        if self.display.cget("text") == "" and toadd != self.last_operand and self.displayall.cget(
                "text") != "" and not self.squared:
            if self.displayall.cget("text")[-1] != "(" and self.displayall.cget("text")[-1] != ")":
                self.label_valueall.set(self.displayall.cget("text")[0:-1] + toadd)
                self.last_operand = toadd

    def equals_function(self):

        count1 = int(str(self.displayall.cget("text")).count("("))
        count2 = int(str(self.displayall.cget("text")).count(")"))
        if not count2 == count1:
            self.label_valueall.set(self.displayall.cget("text") + self.display.cget("text"))
            self.label_value.set("")
            while (count2 < count1):
                self.label_valueall.set(self.displayall.cget("text") + ")")
                count2 = count2 + 1

        if self.displayall.cget("text") == "" or self.display.cget("text") == ".":
            return

        if count1 == count2:
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

        # ============================Bind Functions===========
        # -------------------------------------------------ROW2

        def on_enterlb(e):
            lbracket.configure(bg="#777777")

        def on_leavelb(e):
            lbracket.configure(bg="#494949")

        def on_enterrb(e):
            rbracket.configure(bg="#777777")

        def on_leaverb(e):
            rbracket.configure(bg="#494949")

        def on_entersqroot(e):
            sqroot.configure(bg="#777777")

        def on_leavesqroot(e):
            sqroot.configure(bg="#494949")

        def on_entersquare(e):
            square.configure(bg="#777777")

        def on_leavesquare(e):
            square.configure(bg="#494949")

        def on_enterreci(e):
            reciprocal.configure(bg="#7d6bcf")

        def on_leavereci(e):
            reciprocal.configure(bg="#5E4BB6")

        # -------------------------------------------------ROW3

        def on_enterClear(e):
            Clear.configure(bg="#777777")

        def on_leaveClear(e):
            Clear.configure(bg="#494949")

        def on_enterpi(e):
            pi.configure(bg="#777777")

        def on_leavepi(e):
            pi.configure(bg="#494949")

        def on_enterpm(e):
            plusminus.configure(bg="#777777")

        def on_leavepm(e):
            plusminus.configure(bg="#494949")

        def on_enterdivision(e):
            division.configure(bg="#7d6bcf")

        def on_leavedivision(e):
            division.configure(bg="#5E4BB6")

        # --------------------------------------------------ROW4

        def on_enter7(e):
            seven.configure(bg="#777777")

        def on_leave7(e):
            seven.configure(bg="#404040")

        def on_enter8(e):
            eight.configure(bg="#777777")

        def on_leave8(e):
            eight.configure(bg="#404040")

        def on_enter9(e):
            nine.configure(bg="#777777")

        def on_leave9(e):
            nine.configure(bg="#404040")

        def on_entermulti(e):
            multi.configure(bg="#7d6bcf")

        def on_leavemulti(e):
            multi.configure(bg="#5E4BB6")

        # --------------------------------------------------ROW5

        def on_enter4(e):
            four.configure(bg="#777777")

        def on_leave4(e):
            four.configure(bg="#404040")

        def on_enter5(e):
            five.configure(bg="#777777")

        def on_leave5(e):
            five.configure(bg="#404040")

        def on_enter6(e):
            six.configure(bg="#777777")

        def on_leave6(e):
            six.configure(bg="#404040")

        def on_enterminus(e):
            minus.configure(bg="#7d6bcf")

        def on_leaveminus(e):
            minus.configure(bg="#5E4BB6")

        # --------------------------------------------------ROW6

        def on_enter1(e):
            one.configure(bg="#777777")

        def on_leave1(e):
            one.configure(bg="#404040")

        def on_enter2(e):
            two.configure(bg="#777777")

        def on_leave2(e):
            two.configure(bg="#404040")

        def on_enter3(e):
            three.configure(bg="#777777")

        def on_leave3(e):
            three.configure(bg="#404040")

        def on_enterplus(e):
            plus.configure(bg="#7d6bcf")

        def on_leaveplus(e):
            plus.configure(bg="#5E4BB6")

        # --------------------------------------------------ROW7

        def on_enterdot(e):
            dot.configure(bg="#777777")

        def on_leavedot(e):
            dot.configure(bg="#494949")

        def on_enter0(e):
            zero.configure(bg="#777777")

        def on_leave0(e):
            zero.configure(bg="#404040")

        def on_enterdelete(e):
            delete.configure(bg="#777777")

        def on_leavedelete(e):
            delete.configure(bg="#494949")

        def on_enterequals(e):
            equals.configure(bg="#ffd245")

        def on_leaveequals(e):
            equals.configure(bg="#FEC208")

        # =====================================================

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

        # ====================================Binding==============================================
        # -------------------------------------------------ROW2

        lbracket.bind('<Enter>', on_enterlb)
        lbracket.bind('<Leave>', on_leavelb)

        rbracket.bind('<Enter>', on_enterrb)
        rbracket.bind('<Leave>', on_leaverb)

        sqroot.bind('<Enter>', on_entersqroot)
        sqroot.bind('<Leave>', on_leavesqroot)

        square.bind('<Enter>', on_entersquare)
        square.bind('<Leave>', on_leavesquare)

        reciprocal.bind('<Enter>', on_enterreci)
        reciprocal.bind('<Leave>', on_leavereci)

        # -------------------------------------------------ROW3

        Clear.bind('<Enter>', on_enterClear)
        Clear.bind('<Leave>', on_leaveClear)

        pi.bind('<Enter>', on_enterpi)
        pi.bind('<Leave>', on_leavepi)

        plusminus.bind('<Enter>', on_enterpm)
        plusminus.bind('<Leave>', on_leavepm)

        division.bind('<Enter>', on_enterdivision)
        division.bind('<Leave>', on_leavedivision)

        # -------------------------------------------------ROW4

        seven.bind('<Enter>', on_enter7)
        seven.bind('<Leave>', on_leave7)

        eight.bind('<Enter>', on_enter8)
        eight.bind('<Leave>', on_leave8)

        nine.bind('<Enter>', on_enter9)
        nine.bind('<Leave>', on_leave9)

        multi.bind('<Enter>', on_entermulti)
        multi.bind('<Leave>', on_leavemulti)

        # --------------------------------------------------ROW5

        four.bind('<Enter>', on_enter4)
        four.bind('<Leave>', on_leave4)

        five.bind('<Enter>', on_enter5)
        five.bind('<Leave>', on_leave5)

        six.bind('<Enter>', on_enter6)
        six.bind('<Leave>', on_leave6)

        minus.bind('<Enter>', on_enterminus)
        minus.bind('<Leave>', on_leaveminus)

        # --------------------------------------------------ROW6

        one.bind('<Enter>', on_enter1)
        one.bind('<Leave>', on_leave1)

        two.bind('<Enter>', on_enter2)
        two.bind('<Leave>', on_leave2)

        three.bind('<Enter>', on_enter3)
        three.bind('<Leave>', on_leave3)

        plus.bind('<Enter>', on_enterplus)
        plus.bind('<Leave>', on_leaveplus)

        # --------------------------------------------------ROW7

        dot.bind('<Enter>', on_enterdot)
        dot.bind('<Leave>', on_leavedot)

        zero.bind('<Enter>', on_enter0)
        zero.bind('<Leave>', on_leave0)

        delete.bind('<Enter>', on_enterdelete)
        delete.bind('<Leave>', on_leavedelete)

        equals.bind('<Enter>', on_enterequals)
        equals.bind('<Leave>', on_leaveequals)


window = tkinter.Tk()
window.resizable(0, 0)
window.attributes('-alpha', 0.98)
window.configure(bg="#5A5A5A")
obj = Calculator(window)
window.mainloop()
