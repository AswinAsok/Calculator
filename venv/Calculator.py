import tkinter
from tkinter import *


window = tkinter.Tk()
window.geometry("350x430")

display = Entry( window, width=32,fg="#494949",bg="white",font=("Calibri",16 ))
display.grid(ipady=50,padx=0,pady=0,columnspan=4,rowspan=1)


Clear = Button(window, text="C", width=11, height=3,bg="#494949",fg="white")
Clear.grid(row=1,column=0,sticky="W")

plusminus = Button(window, text="C", width=11, height=3,bg="#494949",fg="white")
plusminus.grid(row=1,column=1,padx=0)

percentage = Button(window, text="%", width=11, height=3,bg="#494949",fg="white")
percentage.grid(row=1,column=2,padx=0)

division = Button(window, text="%", width=11, height=3)
division.grid(row=1,column=3,padx=0)

#------------------------------------------------------------------------

seven = Button(window, text="7", width=11, height=3,bg="#494949",fg="white")
seven.grid(row=2,column=0,sticky="W")

eight = Button(window, text="8", width=11, height=3,bg="#494949",fg="white")
eight.grid(row=2,column=1,padx=0)

nine = Button(window, text="9", width=11, height=3,bg="#494949",fg="white")
nine.grid(row=2,column=2,padx=0)

multi = Button(window, text="X", width=11, height=3)
multi.grid(row=2,column=3,padx=0)

#------------------------------------------------------------------------

four = Button(window, text="4", width=11, height=3,bg="#494949",fg="white")
four.grid(row=3,column=0,sticky="W")

five = Button(window, text="5", width=11, height=3,bg="#494949",fg="white")
five.grid(row=3,column=1,padx=0)

six = Button(window, text="6", width=11, height=3,bg="#494949",fg="white")
six.grid(row=3,column=2,padx=0)

minus = Button(window, text="-", width=11, height=3)
minus.grid(row=3,column=3,padx=0)

#--------------------------------------------------------------------------

one = Button(window, text="1", width=11, height=3,bg="#494949",fg="white")
one.grid(row=4,column=0,sticky="W")

two = Button(window, text="2", width=11, height=3,bg="#494949",fg="white")
two.grid(row=4,column=1,padx=0)

three = Button(window, text="3", width=11, height=3,bg="#494949",fg="white")
three.grid(row=4,column=2,padx=0)

plus = Button(window, text="+", width=11, height=3)
plus.grid(row=4,column=3,padx=0)

#--------------------------------------------------------------------------

zero = Button(window, text="0", width=11, height=3,bg="#494949",fg="white")
zero.grid(row=5,column=0,sticky="W")

dot = Button(window, text=".", width=11, height=3,bg="#494949",fg="white")
dot.grid(row=5,column=1,padx=0)

delete = Button(window, text="del", width=11, height=3,bg="#494949",fg="white")
delete.grid(row=5,column=2,padx=0)

equals = Button(window, text="=", width=11, height=3)
equals.grid(row=5,column=3,padx=0)











window.mainloop()