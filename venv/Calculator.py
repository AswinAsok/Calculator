import tkinter
from tkinter import *


class Calculator:

    def delete(self):

        if not self.equals_clicked:
            self.label_value.set(str(self.display.cget("text")[:-1]))

    def clear(self):
        self.label_value.set("")

    def set_text(self, toadd):
        self.label_value.set(str(self.display.cget("text")) + toadd)

    def equals_function(self):
        self.label_value.set(eval(self.display.cget("text")))



    def __init__(self, window):
        window.geometry("325x427")
        window.title("The Hilarious Calculator")
        self.equals_clicked = False
        self.label_value = StringVar()

        self.display = Label(window, width=29, bg="#5A5A5A", textvariable=self.label_value, fg="white",
                             font=("Calibri", 16), anchor="se")
        self.display.grid(ipady=55, columnspan=4, rowspan=1, padx=0, pady=0, sticky="W")

        Clear = Button(window, text="C", width=7, height=2, bg="#494949", fg="white", border=0, relief=GROOVE,
                       font=('Helvetica', '14'), command=lambda: obj.clear())
        Clear.grid(row=1, column=0)

        pi = Button(window, text="π", width=7, height=2, bg="#494949", fg="white", border=0, relief=GROOVE,
                    font=('Helvetica', '14'))
        pi.grid(row=1, column=1)

        plusminus = Button(window, text="+/-", width=7, height=2, bg="#494949", fg="white", border=0,
                           relief=GROOVE, font=('Helvetica', '14'))
        plusminus.grid(row=1, column=2)

        division = Button(window, text="/", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                          font=('Helvetica', '14'), command=lambda: obj.set_text("/"))
        division.grid(row=1, column=3)

        # ------------------------------------------------------------------------

        seven = Button(window, text="7", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("7"))
        seven.grid(row=2, column=0)

        eight = Button(window, text="8", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("8"))
        eight.grid(row=2, column=1)

        nine = Button(window, text="9", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("9"))
        nine.grid(row=2, column=2)

        multi = Button(window, text="X", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("*"))
        multi.grid(row=2, column=3)

        # ------------------------------------------------------------------------

        four = Button(window, text="4", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("4"))
        four.grid(row=3, column=0)

        five = Button(window, text="5", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("5"))
        five.grid(row=3, column=1)

        six = Button(window, text="6", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("6"))
        six.grid(row=3, column=2)

        minus = Button(window, text="-", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("-"))
        minus.grid(row=3, column=3)

        # --------------------------------------------------------------------------

        one = Button(window, text="1", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("1"))
        one.grid(row=4, column=0)

        two = Button(window, text="2", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("2"))
        two.grid(row=4, column=1)

        three = Button(window, text="3", width=7, height=2, bg="#494949", fg="white", border=0,
                       font=('Helvetica', '14'), command=lambda: obj.set_text("3"))
        three.grid(row=4, column=2)

        plus = Button(window, text="+", width=7, height=2, bg="#5E4BB6", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("+"))
        plus.grid(row=4, column=3)

        # --------------------------------------------------------------------------

        zero = Button(window, text="0", width=7, height=2, bg="#494949", fg="white", border=0,
                      font=('Helvetica', '14'), command=lambda: obj.set_text("0"))
        zero.grid(row=5, column=0)

        dot = Button(window, text=".", width=7, height=2, bg="#494949", fg="white", border=0,
                     font=('Helvetica', '14'), command=lambda: obj.set_text("."))
        dot.grid(row=5, column=1)

        delete = Button(window, text="del", width=7, height=2, bg="#494949", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda: obj.delete())
        delete.grid(row=5, column=2)

        equals = Button(window, text="=", width=7, height=2, bg="#FEC208", border=0, fg="white",
                        font=('Helvetica', '14'), command=lambda:obj.equals_function())
        equals.grid(row=5, column=3)


window = tkinter.Tk()
window.resizable(0, 0)
obj = Calculator(window)
window.mainloop()
