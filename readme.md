# <p align = "center">The Hilarious Calculator</p>
Author : Aswin Asok<br>
Mail   : aswinasokofficial@gmail.com<br>

##  Labels
---------
### Row 0
1) display_all => To display all th calculations done untill equals or clear key has been pressed<br> textvariable=self.label_value_all.

### Row 1
2) display => To display the last entered numeric value<br> textvariable=self.label_value.

## Buttons<br>
--------------
### Row 2

* left_bracket => add '(' to display_all label.
* right_bracket => add ')' to display_all label.
* sqr => To find square root.
* square => To find square.
* reciprocal => To find reciprocal.

### Row 3

* clear => Clears both the labels.
* pi => Multiplies the value from display label with '3.14'.
* plus_minus => Multiplies the value from display label with '-'.
* division => To Divide.

### Row 4

* seven => To set_text as 7.
* eight => To set_text as 8.
* nine => To set_text as 9.
* multi => To Multiply.


### Row 5
 
* four => To set_text as 4.
* five => To set_text as 5.
* six => To set_text as 6.
* minus => To Subtract.

### Row 6
 
* one => To set_text as 1.
* two => To set_text as 2.
* three => To set_text as 3.
* plus => To Add.

### Row 7
 
* dot => To add to display label '.'.
* zero => To set_text as 0.
* delete => To delete thr last character from display label.
* equals => To calculate the result using eval() .

## Functions
---------

### def _ _ init _ _();<br>
* Constructor which has an argument named _**window**_ which recives the parameter _**root**_ pass at the time of object creation.
<br><br>
Function : To initalize all the buttons,varibles and labels.
<br><br>
Note : The binding functions for hover feature are declared inside the constructor.

### def set_text ():<br>
* Takes an argument named _**to_add**_ from each button when they are clicked and stores them in respective labels according the button which was clicked.

###  def equals_function():
* This function takes no arguments and is used to calculate and display the result in _**display label**_,if the conditions requried are met.

###  def pi():<br>
* This function has no arguments and is executed when the _**π**_ button has been clicked and multiples 3.14 to the existing display label if the _if:_ conditions are true.

### def clear():<br>
* This function has no arguments and is executed when the clear button has been pressed and clears both the labels.

### def delete():
* This function has no arguments and is executed when the  **⌫** is clicked and removes the last character from the display label if it isn't null.

### def dot_operator():
* This function has no arguments and is executed when the dot button has been pressed and add a '.' to the display_label if the _if:_ conditions are true.

### def negate():
* This function has no argument and is executed when the "+/-" button has been clicked and multiple -1 with the value in the display label if it isn't null

### def reciprocal():
* This function has no argument and is executed when the "1/x" button has been clicked and this function takes value from the display label and changes it into 1/(x) and sets it in display_all label,if the _if:_ conditions are true.

### def square():
* This function has no argument and is executed when the "x²" has been clciked and this function takes value from the display label finds its square and sets it into the display_all label,
if the _if:_ conditions are true.

### def sqr():
* This function has no argument and is executed when the "√" button has been clicked and this function takes value from the display label and sets it as sqrt(x) into the display_all label ,if the _if:_ conditions are true.

## Variables
-----
* count1 : To Count the number of '('.
* count2 : To Count the number of ')'.
* equals_clicked : To check whether equals button was clicked.
* squared : To check whether square button was clicked.
* square_root : To check whether squareroot button was clicked.
* label_value : To store the string to be displayed at display label.
* label_value_all : To store the string to be displayed at display_all label.
* last_operand : To store the last operand when a new oprand has been clicked.


 









