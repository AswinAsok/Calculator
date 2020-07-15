import tkinter
from tkinter import *
from math import sqrt


class Calculator:

    def sqr(self):
        if self.display.cget("text") != "0" and self.display.cget("text") != "":
            if float(self.display.cget("text")) < 0:
                self.label_value.set("Invalid Input")
                return
            self.square_root = True
            self.label_value_all.set(self.display_all.cget("text") + "sqrt(" + str(self.display.cget("text")) + ")")
            self.label_value.set("")

    def square(self):
        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.squared = True
            self.label_value.set(
                    str(float(self.display.cget("text")) * float(self.display.cget("text"))))

    def reciprocal(self):
        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.reciprocal_clicked = True
            self.label_value_all.set(self.display_all.cget("text") + "1/(" + str(self.display.cget("text")) + ")")
            self.label_value.set("")

    def negate(self):

        if self.display.cget("text") == "Cannot Divide By Zero" or self.display.cget("text") == "Invalid Input":
            self.clear()

        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.label_value.set(str(float(self.display.cget("text")) * -1))
            self.negated = True

    def dot_operator(self):

        if self.equals_clicked and self.display.cget("text") != "":
            self.label_value.set("0")
            self.equals_clicked = False

        if self.display.cget("text") == "Cannot Divide By Zero" or self.display.cget("text") == "Invalid Input":
            self.clear()

        if self.display.cget("text") != "":
            if str(self.display.cget("text")).count(".") < 1:
                if str(self.display.cget("text") == "") or str(self.display.cget("text")[-1] != '.'):
                    self.label_value.set(self.display.cget("text") + ".")

    def delete(self):

        if self.display.cget("text") == "0":
            return

        if self.display.cget("text") == "Cannot Divide By Zero" or self.display.cget("text") == "Invalid Input":
            self.clear()

        if not self.equals_clicked:
            if not self.equals_clicked:
                self.label_value.set(str(self.display.cget("text")[:-1]))

    def clear(self):

        self.label_value.set("0")
        self.label_value_all.set("")
        self.equals_clicked = False
        self.squared = False
        self.square_root = False
        self.negated = False
        self.reciprocal_clicked = False

    def pi(self):
        if self.display.cget("text") == "Cannot Divide By Zero" or self.display.cget("text") == "Invalid Input":
            self.clear()

        if self.display.cget("text") != "" and self.display.cget("text") != "0":
            self.label_value.set(str(float(self.display.cget("text")) * 3.14))

    def set_text(self, to_add):

        if self.squared and to_add.isdigit():
            self.label_value.set("")
            self.squared = False

        if self.square_root or self.reciprocal_clicked:
            if not (to_add == "+" or to_add == "-" or to_add == "*" or to_add == "/"):
                return
            else:
                self.squared = False
                self.reciprocal_clicked = False

        if self.display.cget("text") != "":
            if self.negated and self.display.cget("text")[0] == "-":
                if to_add == "+" or to_add == "-" or to_add == "*" or to_add == "/":
                    self.label_value.set("("+self.display.cget("text")+")")
                    self.negated = False

        if to_add == ")" and int(str(self.display_all.cget("text")).count("(")) == 0:
            return

        if self.display_all.cget("text") != "":
            if to_add.isdigit() and self.square_root and self.display_all.cget("text")[-1] == ")":
                return

        if self.display_all.cget("text") != "":
            if self.display_all.cget("text")[-1] == ")" and not to_add.isdigit():
                self.square_root = False

        if self.display_all.cget("text") != "":

            if self.display_all.cget("text")[-1] == ")" and to_add == "(":  # "7-(5+4)(" For Fixing
                return

            if (to_add == "+" or to_add == "-" or to_add == "*" or to_add == "/") and self.display_all.cget("text")[
                 -1] == ")":
                self.label_value_all.set(self.display_all.cget("text") + str(self.display.cget("text")) + to_add)
            elif self.display_all.cget("text")[-1] == ")" and to_add == ")":
                count1 = int(str(self.display_all.cget("text")).count("("))
                count2 = int(str(self.display_all.cget("text")).count(")"))
                if count2 < count1:
                    self.label_value_all.set(self.display_all.cget("text") + str(self.display.cget("text")) + to_add)

        if self.display.cget("text") == "." and self.display_all.cget("text") == "":
            return

        if self.display.cget("text") == "Cannot Divide By Zero" or self.display.cget("text") == "Invalid Input":
            self.clear()

        if self.equals_clicked and self.display.cget("text") != "" and to_add.isdigit():
            self.label_value.set("")

        self.equals_clicked = False

        if not (to_add == "+" or to_add == "-" or to_add == "*" or to_add == "/" or to_add == "(" or to_add == ")"):
            if self.display.cget("text") == "0":
                self.label_value.set("")
            self.label_value.set(str(self.display.cget("text")) + to_add)

        if to_add == "+" or to_add == "-" or to_add == "*" or to_add == "/" or to_add == "(" or to_add == ")":

            if to_add != "(" or to_add != ")":
                if self.display_all.cget("text") != "" and self.display_all.cget("text")[
                     -1] == to_add and self.display.cget("text") == "":
                    return

            if to_add == "(" or to_add == ")" and self.display.cget("text") == "0" and self.display_all.cget(
                    "text") == "":
                self.label_value.set("")
                if to_add == ")":
                    if int(str(self.display_all.cget("text")).count("(")) != 0:
                        self.label_value_all.set(
                            self.display_all.cget("text") + str(self.display.cget("text")) + to_add)
                if to_add == "(":
                    self.label_value_all.set(self.display_all.cget("text") + str(self.display.cget("text")) + to_add)

            if self.display_all.cget("text") != to_add and self.display.cget("text") != "0" and self.display.cget(
                    "text") != "" or self.squared:
                if self.display.cget("text") != "" and str(self.display.cget("text"))[-1] == ".":
                    return
                self.label_value_all.set(self.display_all.cget("text") + str(self.display.cget("text")) + to_add)
                self.label_value.set("")
                self.last_operand = to_add
                self.squared = False

        if self.display.cget("text") == "" and to_add != self.last_operand and self.display_all.cget(
                "text") != "" and not self.squared:
            if self.display_all.cget("text")[-1] != "(" and self.display_all.cget("text")[-1] != ")":
                self.label_value_all.set(self.display_all.cget("text")[0:-1] + to_add)
                self.last_operand = to_add

    def equals_function(self):

        count1 = int(str(self.display_all.cget("text")).count("("))
        count2 = int(str(self.display_all.cget("text")).count(")"))
        if not count2 == count1:
            self.label_value_all.set(self.display_all.cget("text") + self.display.cget("text"))
            self.label_value.set("")
            while count2 < count1:
                self.label_value_all.set(self.display_all.cget("text") + ")")
                count2 = count2 + 1

        if self.display_all.cget("text") == "" or self.display.cget("text") == ".":
            return

        if count1 == count2:
            if self.display_all.cget("text") != "" and self.display_all.cget("text")[-1].isdigit() or self.display.cget(
                    "text") != "" or self.display_all.cget("text")[-1] == ")":
                self.equals_clicked = True
                self.label_value_all.set(self.display_all.cget("text") + self.display.cget("text"))
                try:
                    self.label_value.set(eval(str(self.display_all.cget("text"))))
                except ZeroDivisionError:
                    self.label_value.set("Cannot Divide By Zero")
                    self.equals_clicked = False
                self.label_value_all.set("")

    def __init__(self, window):
        window.geometry("341x495")
        window.title("The Hilarious Calculator")
        self.equals_clicked = False
        self.squared = False
        self.square_root = False
        self.negated = False
        self.reciprocal_clicked = False
        self.label_value = StringVar()
        self.label_value_all = StringVar()
        self.last_operand = ""

        def keyboard(event):
            key = event.char
            if "0" <= key <= "9" or key == ")" or key == "(" or key == "+" or key == "-" or key == "*" or key == "/":
                obj.set_text(key)
            elif key == ".":
                obj.dot_operator()
            elif key == "p" or key == "P":
                obj.pi()
            elif key == "r" or key == "R":
                obj.reciprocal()
            elif key == "n" or key == "N":
                obj.negate()
            elif key == "s":
                obj.sqr()
            elif key == "S":
                obj.square()

        def key_press(event):
            keyboard(event)
            key = event.char
            if key == "1":
                on_enter1(e=None)
            elif key == "2":
                on_enter2(e=None)
            elif key == "3":
                on_enter3(e=None)
            elif key == "4":
                on_enter4(e=None)
            elif key == "5":
                on_enter5(e=None)
            elif key == "6":
                on_enter6(e=None)
            elif key == "7":
                on_enter7(e=None)
            elif key == "8":
                on_enter8(e=None)
            elif key == "9":
                on_enter9(e=None)
            elif key == "0":
                on_enter0(e=None)
            elif key == ".":
                on_enter_dot(e=None)
            elif key == "s":
                on_enter_sqr(e=None)
            elif key == "S":
                on_enter_square(e=None)
            elif key == "p" or key == "P":
                on_enter_pi(e=None)
            elif key == "(":
                on_enter_lb(e=None)
            elif key == ")":
                on_enter_rb(e=None)
            elif key == "n" or key == "N":
                on_enter_pm(e=None)
            elif key == ")":
                on_enter_rb(e=None)
            elif key == "r" or key == "R":
                on_enter_reciprocal(e=None)
            elif key == "*":
                on_enter_multi(e=None)
            elif key == "/":
                on_enter_division(e=None)
            elif key == "-":
                on_enter_minus(e=None)
            elif key == "+":
                on_enter_plus(e=None)

        def key_release(event):
            key = event.char
            if key == "1":
                on_leave1(e=None)
            elif key == "2":
                on_leave2(e=None)
            elif key == "3":
                on_leave3(e=None)
            elif key == "4":
                on_leave4(e=None)
            elif key == "5":
                on_leave5(e=None)
            elif key == "6":
                on_leave6(e=None)
            elif key == "7":
                on_leave7(e=None)
            elif key == "8":
                on_leave8(e=None)
            elif key == "9":
                on_leave9(e=None)
            elif key == "0":
                on_leave0(e=None)
            elif key == ".":
                on_leave_dot(e=None)
            elif key == "s":
                on_leave_sqr(e=None)
            elif key == "S":
                on_leave_square(e=None)
            elif key == "p" or key == "P":
                on_leave_pi(e=None)
            elif key == "(":
                on_leave_lb(e=None)
            elif key == ")":
                on_leave_rb(e=None)
            elif key == "n" or key == "N":
                on_leave_pm(e=None)
            elif key == ")":
                on_leave_rb(e=None)
            elif key == "r" or key == "R":
                on_leave_reciprocal(e=None)
            elif key == "*":
                on_leave_multi(e=None)
            elif key == "/":
                on_leave_division(e=None)
            elif key == "-":
                on_leave_minus(e=None)
            elif key == "+":
                on_leave_plus(e=None)

        window.bind("<Return>", lambda event: obj.equals_function())
        window.bind("<BackSpace>", lambda event: obj.delete())
        window.bind("<Delete>", lambda event: obj.clear())
        window.bind('<KeyPress>', lambda a: key_press(a))
        window.bind('<KeyRelease>', lambda a: key_release(a))

        # ============================Bind Functions==========

        # -------------------------------------------------ROW2

        def on_enter_lb(e):
            left_bracket.configure(bg="#777777")

        def on_leave_lb(e):
            left_bracket.configure(bg="#494949")

        def on_enter_rb(e):
            right_bracket.configure(bg="#777777")

        def on_leave_rb(e):
            right_bracket.configure(bg="#494949")

        def on_enter_sqr(e):
            sqr.configure(bg="#777777")

        def on_leave_sqr(e):
            sqr.configure(bg="#494949")

        def on_enter_square(e):
            square.configure(bg="#777777")

        def on_leave_square(e):
            square.configure(bg="#494949")

        def on_enter_reciprocal(e):
            reciprocal.configure(bg="#7d6bcf")

        def on_leave_reciprocal(e):
            reciprocal.configure(bg="#5E4BB6")

        # -------------------------------------------------ROW3

        def on_enter_clear(e):
            clear.configure(bg="#777777")

        def on_leave_clear(e):
            clear.configure(bg="#494949")

        def on_enter_pi(e):
            pi.configure(bg="#777777")

        def on_leave_pi(e):
            pi.configure(bg="#494949")

        def on_enter_pm(e):
            plus_minus.configure(bg="#777777")

        def on_leave_pm(e):
            plus_minus.configure(bg="#494949")

        def on_enter_division(e):
            division.configure(bg="#7d6bcf")

        def on_leave_division(e):
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

        def on_enter_multi(e):
            multi.configure(bg="#7d6bcf")

        def on_leave_multi(e):
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

        def on_enter_minus(e):
            minus.configure(bg="#7d6bcf")

        def on_leave_minus(e):
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

        def on_enter_plus(e):
            plus.configure(bg="#7d6bcf")

        def on_leave_plus(e):
            plus.configure(bg="#5E4BB6")

        # --------------------------------------------------ROW7

        def on_enter_dot(e):
            dot.configure(bg="#777777")

        def on_leave_dot(e):
            dot.configure(bg="#494949")

        def on_enter0(e):
            zero.configure(bg="#777777")

        def on_leave0(e):
            zero.configure(bg="#404040")

        def on_enter_delete(e):
            delete.configure(bg="#777777")

        def on_leave_delete(e):
            delete.configure(bg="#494949")

        def on_enter_equals(e):
            equals.configure(bg="#ffd245")

        def on_leave_equals(e):
            equals.configure(bg="#FEC208")

        # =====================================================

        self.display_all = Label(window, width=30, bg="#5A5A5A", textvariable=self.label_value_all, fg="white",
                                 font=("Calibri", 16), anchor="se")
        self.display_all.grid(row=0, ipady=14, columnspan=6, rowspan=1, padx=0, pady=0, sticky="W")

        self.display = Label(window, width=21, bg="#5A5A5A", textvariable=self.label_value, fg="white",
                             font=("Calibri", 24), anchor="e")
        self.label_value.set("0")
        self.display.grid(row=1, ipady=16, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")
        # -------------------------------------------------------------------------------------

        left_bracket = Button(window, text="(", width=3, height=2, bg="#494949", fg="white", border=0,
                              font=('Helvetica', '14'), command=lambda: obj.set_text("("))
        left_bracket.grid(row=2, column=0, pady=1, padx=1, sticky="W")

        right_bracket = Button(window, text=")", width=3, height=2, bg="#494949", fg="white", border=0,
                               font=('Helvetica', '14'), command=lambda: obj.set_text(")"))
        right_bracket.grid(row=2, column=0, pady=1, padx=1, stick="E")

        sqr = Button(window, text="√", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.sqr())
        sqr.grid(row=2, column=1)

        square = Button(window, text="x²", width=7, height=2, bg="#494949", fg="white", border=0,
                        relief=GROOVE, font=('Helvetica', '14'), command=lambda: obj.square())
        square.grid(row=2, column=2)

        reciprocal = Button(window, text="1/x", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                            font=('Helvetica', '14'), command=lambda: obj.reciprocal())
        reciprocal.grid(row=2, column=3)

        # -------------------------------------------------------------------------------------

        clear = Button(window, text="C", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.clear())
        clear.grid(row=3, column=0, pady=1, padx=1)

        pi = Button(window, text="π", width=7, height=2, bg="#494949", fg="white", border=0,
                    font=('Helvetica', '14'), command=lambda: obj.pi())
        pi.grid(row=3, column=1)

        plus_minus = Button(window, text="+/-", width=7, height=2, bg="#494949", fg="white", border=0,
                            relief=GROOVE, font=('Helvetica', '14'), command=lambda: obj.negate())
        plus_minus.grid(row=3, column=2)

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

        left_bracket.bind('<Enter>', on_enter_lb)
        left_bracket.bind('<Leave>', on_leave_lb)

        right_bracket.bind('<Enter>', on_enter_rb)
        right_bracket.bind('<Leave>', on_leave_rb)

        sqr.bind('<Enter>', on_enter_sqr)
        sqr.bind('<Leave>', on_leave_sqr)

        square.bind('<Enter>', on_enter_square)
        square.bind('<Leave>', on_leave_square)

        reciprocal.bind('<Enter>', on_enter_reciprocal)
        reciprocal.bind('<Leave>', on_leave_reciprocal)

        # -------------------------------------------------ROW3

        clear.bind('<Enter>', on_enter_clear)
        clear.bind('<Leave>', on_leave_clear)

        pi.bind('<Enter>', on_enter_pi)
        pi.bind('<Leave>', on_leave_pi)

        plus_minus.bind('<Enter>', on_enter_pm)
        plus_minus.bind('<Leave>', on_leave_pm)

        division.bind('<Enter>', on_enter_division)
        division.bind('<Leave>', on_leave_division)

        # -------------------------------------------------ROW4

        seven.bind('<Enter>', on_enter7)
        seven.bind('<Leave>', on_leave7)

        eight.bind('<Enter>', on_enter8)
        eight.bind('<Leave>', on_leave8)

        nine.bind('<Enter>', on_enter9)
        nine.bind('<Leave>', on_leave9)

        multi.bind('<Enter>', on_enter_multi)
        multi.bind('<Leave>', on_leave_multi)

        # --------------------------------------------------ROW5

        four.bind('<Enter>', on_enter4)
        four.bind('<Leave>', on_leave4)

        five.bind('<Enter>', on_enter5)
        five.bind('<Leave>', on_leave5)

        six.bind('<Enter>', on_enter6)
        six.bind('<Leave>', on_leave6)

        minus.bind('<Enter>', on_enter_minus)
        minus.bind('<Leave>', on_leave_minus)

        # --------------------------------------------------ROW6

        one.bind('<Enter>', on_enter1)
        one.bind('<Leave>', on_leave1)

        two.bind('<Enter>', on_enter2)
        two.bind('<Leave>', on_leave2)

        three.bind('<Enter>', on_enter3)
        three.bind('<Leave>', on_leave3)

        plus.bind('<Enter>', on_enter_plus)
        plus.bind('<Leave>', on_leave_plus)

        # --------------------------------------------------ROW7

        dot.bind('<Enter>', on_enter_dot)
        dot.bind('<Leave>', on_leave_dot)

        zero.bind('<Enter>', on_enter0)
        zero.bind('<Leave>', on_leave0)

        delete.bind('<Enter>', on_enter_delete)
        delete.bind('<Leave>', on_leave_delete)

        equals.bind('<Enter>', on_enter_equals)
        equals.bind('<Leave>', on_leave_equals)


root = tkinter.Tk()
root.resizable(0, 0)
root.attributes('-alpha', 0.98)
root.configure(bg="#5A5A5A")
obj = Calculator(root)
root.mainloop()
