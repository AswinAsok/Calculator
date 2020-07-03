import tkinter
from tkinter import *


class Calculator:

    def negate(self):
        self.label_value.set(str(int(self.display.cget("text")) * -1))

    def dot_operator(self):
        if (self.display.cget("text") == "" or self.display.cget("text")[-1] != '.' and str(
                self.display.cget("text")).count(".") < 1):
            self.label_value.set(self.display.cget("text") + ".")

    def delete(self):
        if not self.equals_clicked:
            if not self.equals_clicked:
                self.label_value.set(str(self.display.cget("text")[:-1]))

    def clear(self):
        self.label_value.set("")
        self.label_valueall.set("")

    def pi(self):
        if(self.display.cget("text")!=""):
            self.label_value.set(str(int(self.display.cget("text"))*3.14))

    def set_text(self, toadd):

        self.equals_clicked = False

        if not (toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/"):
            self.label_value.set(str(self.display.cget("text")) + toadd)

        if toadd == "+" or toadd == "-" or toadd == "*" or toadd == "/":
            if self.displayall.cget("text") != toadd and self.display.cget("text") != "":
                self.label_valueall.set(self.displayall.cget("text") + str(self.display.cget("text")) + toadd)
                self.label_value.set("")
                self.last_operand = toadd

        if self.display.cget("text") == "" and toadd != self.last_operand and self.displayall.cget("text") != "":
            self.label_valueall.set(self.displayall.cget("text")[0:-1] + toadd)
            self.last_operand = toadd

    def equals_function(self):
        if self.displayall.cget("text") != "" and self.displayall.cget("text")[-1].isdigit() or self.display.cget(
                "text") != "":
            self.equals_clicked = True
            self.label_valueall.set(self.displayall.cget("text") + self.display.cget("text"))
            self.label_value.set(eval(self.displayall.cget("text")))
            self.label_valueall.set("")

    def __init__(self, window):
        window.geometry("348x448")
        window.title("The Hilarious Calculator")
        self.equals_clicked = False
        self.label_value = StringVar()
        self.label_valueall = StringVar()
        self.last_operand = ""

        self.displayall = Label(window, width=31, bg="#5A5A5A", textvariable=self.label_valueall, fg="white",
                                font=("Calibri", 16), anchor="se")
        self.displayall.grid(row=0, ipady=20, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")

        self.display = Label(window, width=24, bg="#5A5A5A", textvariable=self.label_value, fg="white",
                             font=("Calibri", 20), anchor="e")
        self.display.grid(row=1, ipady=20, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")

        Clear = Button(window, text="C", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.clear())
        Clear.grid(row=2, column=0, pady=1, padx=1)

        pi = Button(window, text="π", width=7, height=2, bg="#494949", fg="white", border=0,
                    font=('Helvetica', '14'),command=lambda: obj.pi())
        pi.grid(row=2, column=1)

        plusminus = Button(window, text="+/-", width=7, height=2, bg="#494949", fg="white", border=0,
                           relief=GROOVE, font=('Helvetica', '14'), command=lambda: obj.negate())
        plusminus.grid(row=2, column=2)

        division = Button(window, text="/", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: obj.set_text("/"))
        division.grid(row=2, column=3)

        # ------------------------------------------------------------------------

        seven = Button(window, text="7", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("7"))
        seven.grid(row=3, column=0, pady=1, padx=1)

        eight = Button(window, text="8", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("8"))
        eight.grid(row=3, column=1)

        nine = Button(window, text="9", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("9"))
        nine.grid(row=3, column=2)

        multi = Button(window, text="X", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("*"))
        multi.grid(row=3, column=3)

        # ------------------------------------------------------------------------

        four = Button(window, text="4", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("4"))
        four.grid(row=4, column=0, pady=1, padx=1)

        five = Button(window, text="5", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("5"))
        five.grid(row=4, column=1)

        six = Button(window, text="6", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("6"))
        six.grid(row=4, column=2)

        minus = Button(window, text="-", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("-"))
        minus.grid(row=4, column=3)

        # --------------------------------------------------------------------------

        one = Button(window, text="1", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("1"))
        one.grid(row=5, column=0, pady=1, padx=1)

        two = Button(window, text="2", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("2"))
        two.grid(row=5, column=1)

        three = Button(window, text="3", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("3"))
        three.grid(row=5, column=2)

        plus = Button(window, text="+", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("+"))
        plus.grid(row=5, column=3)

        # --------------------------------------------------------------------------

        zero = Button(window, text="0", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("0"))
        zero.grid(row=6, column=1, pady=1, padx=1)

        dot = Button(window, text=".", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.dot_operator())
        dot.grid(row=6, column=0)

        delete = Button(window, text="\u232b", width=7, height=2, bg="#494949", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda: obj.delete())
        delete.grid(row=6, column=2)

        equals = Button(window, text="=", width=7, height=2, bg="#FEC208", border=0, fg="black",
                        font=('Helvetica', '14'), command=lambda: obj.equals_function())
        equals.grid(row=6, column=3)


window = tkinter.Tk()
window.resizable(0, 0)
window.attributes('-alpha', 0.96)
window.configure(bg="#5A5A5A")
obj = Calculator(window)
window.mainloop()
