import tkinter
from tkinter import *


#-----------------------------FUNCTIONS--------------------

def clear():
    display.delete(0, END)
    display.insert(0, "")


def set_text(toadd):
    new_text = display.get()+toadd
    display.delete(0, END)
    display.insert(0,new_text)

def del_function():
    new_text = display.get()[:-1]
    display.delete(0, END)
    display.insert(0, new_text)



#------------------------------Class-------------------


class Calculator():


    def __init__(self,window):
        window.geometry("350x420")
        #window.configure(bg="#494949")
        window.title("The Hilarious Calculator")
        global display
        display = Entry( window, width=31,fg="#494949",bg="white",font=("Calibri",16 ),justify=RIGHT)
        display.grid(ipady=55,padx=0,pady=0,columnspan=4,rowspan=1)



        Clear = Button(window, text="C", width=11, height=3,bg="#494949",fg="white",command=clear)
        Clear.grid(row=1,column=0,sticky="W")

        plusminus = Button(window, text="π", width=11, height=3,bg="#494949",fg="white")
        plusminus.grid(row=1,column=1,padx=0)

        percentage = Button(window, text="+/-", width=11, height=3,bg="#494949",fg="white")
        percentage.grid(row=1,column=2,padx=0)

        division = Button(window, text="/", width=11, height=3,bg="#5E4BB6",fg="white")
        division.grid(row=1,column=3,padx=0)

        #------------------------------------------------------------------------

        seven = Button(window, text="7", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("7"))
        seven.grid(row=2,column=0,sticky="W")
        seven.grid_propagate(False)

        eight = Button(window, text="8", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("8"))
        eight.grid(row=2,column=1,padx=0)

        nine = Button(window, text="9", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("9"))
        nine.grid(row=2,column=2,padx=0)

        multi = Button(window, text="X", width=11, height=3,bg="#5E4BB6",fg="white")
        multi.grid(row=2,column=3,padx=0)

        #------------------------------------------------------------------------

        four = Button(window, text="4", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("4"))
        four.grid(row=3,column=0,sticky="W")

        five = Button(window, text="5", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("5"))
        five.grid(row=3,column=1,padx=0)

        six = Button(window, text="6", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("6"))
        six.grid(row=3,column=2,padx=0)

        minus = Button(window, text="-", width=11, height=3,bg="#5E4BB6",fg="white")
        minus.grid(row=3,column=3,padx=0)

        #--------------------------------------------------------------------------

        one = Button(window, text="1", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("1"))
        one.grid(row=4,column=0,sticky="W")

        two = Button(window, text="2", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("2"))
        two.grid(row=4,column=1,padx=0)

        three = Button(window, text="3", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("3"))
        three.grid(row=4,column=2,padx=0)

        plus = Button(window, text="+", width=11, height=3,bg="#5E4BB6",fg="white")
        plus.grid(row=4,column=3,padx=0)

        #--------------------------------------------------------------------------

        zero = Button(window, text="0", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("0"))
        zero.grid(row=5,column=0,sticky="W")

        dot = Button(window, text=".", width=11, height=3,bg="#494949",fg="white",command=lambda :set_text("."))
        dot.grid(row=5,column=1,padx=0)

        delete = Button(window, text="del", width=11, height=3,bg="#494949",fg="white",command=lambda :del_function())
        delete.grid(row=5,column=2,padx=0)

        equals = Button(window, text="=", width=11, height=3,bg="#FEC208",fg="black")
        equals.grid(row=5,column=3,padx=0)





window = tkinter.Tk()
obj = Calculator(window)
window.mainloop()