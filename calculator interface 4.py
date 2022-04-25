#imports tkinter and makes it so I won't have to contiune re-typing tkinter
from tkinter import *

expression = ""


def press(num):      #Has it so the display will add whatever commands I press (function)
    global expression
    expression = expression +str(num)
    equation.set(expression)
    

def equalpress():   #Has is so when the equal sign is pressed it gives the answer (function)
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set('error')
        expression.set("")

def clear():     #Has it so when the clear is pressend the display will clear  (function)
    global expression
    expression = ""
    equation.set("")  

import CalMod  #imports CalMod that has the background function


if __name__ == "__main__":   #Has the layout for the calculator
    gui = Tk()
    gui.configure(CalMod.back()) #uses the background function
    gui. title("Calculator")
    gui.geometry("250x230")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    gui.iconphoto(False,PhotoImage(file='downloadtry1.png'))

    
#all the button controls
    
    button7 = Button(gui, text = '7', fg='white', bg='black',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=2, column=0)
    button8 = Button(gui, text = '8', fg='white', bg='black',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=2, column=1)
    button9 = Button(gui, text = '9', fg='white', bg='black',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=2, column=2)
    button4 = Button(gui, text = '4', fg='white', bg='black',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(gui, text = '5', fg='white', bg='black',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(gui, text = '6', fg='white', bg='black',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button1 = Button(gui, text = '1', fg='white', bg='black',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=4, column=0)
    button2 = Button(gui, text = '2', fg='white', bg='black',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1)
    button3 = Button(gui, text = '3', fg='white', bg='black',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=4, column=2)
    button0 = Button(gui, text = '0', fg='white', bg='black',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
    decimal = Button(gui, text='.', fg='white', bg='black',
                     command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=5,column=1)
    timeten = Button(gui, text = 'x10**', fg='white', bg='black',
                    command=lambda: press('*10**'), height=1, width=7)
    timeten.grid(row=5, column=2)
    plus = Button(gui, text = '+', fg='white', bg='black',
                    command=lambda: press('+'), height=1, width=7)
    plus.grid(row=6, column=0)
    minus = Button(gui, text = '-', fg='white', bg='black',
                    command=lambda: press('-'), height=1, width=7)
    minus.grid(row=6, column=1)
    multiple = Button(gui, text = 'x', fg = 'white', bg='black',
                    command=lambda: press('*'), height=1, width=7)
    multiple.grid(row=6,column=2)
    divide = Button(gui, text = '/', fg='white', bg='black',
                    command=lambda: press('/'), height=1, width=7)
    divide.grid(row=7, column=0)
    squared = Button(gui, text = '**2', fg='white', bg='black',
                     command=lambda: press('**2'), height=1, width=7)
    squared.grid(row=7, column=1)
    powerof = Button(gui, text = '**', fg='white', bg='black',
                     command=lambda: press('**'), height=1, width=7)
    powerof.grid(row=7, column=2)
    pi = Button(gui, text='pi', fg='white', bg='black',
                command=lambda: press('3.141592654'), height=1, width=7)
    pi.grid(row=8, column=0)
    equal = Button(gui, text = '=', fg='white', bg='black',
                     command=equalpress, height=1, width=7)
    equal.grid(row=8, column=1)
    clear = Button(gui, text = 'Clear', fg='white', bg='black',
                     command=clear, height=1, width=7)
    clear.grid(row=8, column=2)
    openbracket = Button(gui, text = '(', fg='white', bg='black',
                         command=lambda: press('('), height=1, width=7)
    openbracket.grid(row=9, column=0)
    closebracket = Button(gui, text = ')', fg='white', bg='black',
                          command=lambda: press(')'), height=1, width=7)
    closebracket.grid(row=9, column=1)
    
