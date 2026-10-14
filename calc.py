import matplotlib as plt
import tkinter as tk

#set up the window
window = tk.Tk()
window.title("Graphical Calculator")
window.geometry("300x400")
window.configure(background = "gray12")

#declaring variables
num = tk.IntVar()
number = ""

#button functions
def buttonPress9():
    global number
    number = number + str(9)
    num.set(number)

def buttonPress8():
    global number
    number = number + str(8)
    num.set(number)

def buttonPress7():
    global number
    number = number + str(7)
    num.set(number)

def buttonPress6():
    global number
    number = number + str(6)
    num.set(number)

def buttonPress5():
    global number
    number = number + str(5)
    num.set(number)

def buttonPress4():
    global number
    number = number + str(4)
    num.set(number)

def buttonPress3():
    global number
    number = number + str(3)
    num.set(number)

def buttonPress2():
    global number
    number = number + str(2)
    num.set(number)

def buttonPress1():
    global number
    number = number + str(1)
    num.set(number)

def buttonPress0():
    global number
    number = number + str(0)
    num.set(number)

def buttonPressAdd():
    global number
    number = number + "+"
    num.set(number)

def buttonPressSub():
    global number
    number = number + "-"
    num.set(number)

def buttonPressMul():
    global number
    number = number + "x"
    num.set(number)

def buttonPressDiv():
    global number
    number = number + "÷"
    num.set(number)

def buttonPressDot():
    global number
    number = number + "."
    num.set(number)

def buttonPressEq():
    global number

#declaring the buttons
button0 = tk.Button(window, text="0", command=buttonPress0, font=("Arial",50))
button1 = tk.Button(window, text="1", command=buttonPress1, font=("Arial",50))
button2 = tk.Button(window, text ="2", command=buttonPress2, font=("Arial",50))
button3 = tk.Button(window, text="3", command=buttonPress3, font=("Arial",50))
button4 = tk.Button(window, text ="4", command=buttonPress4, font=("Arial",50))
button5 = tk.Button(window, text="5", command=buttonPress5, font=("Arial",50))
button6 = tk.Button(window, text ="6", command=buttonPress6, font=("Arial",50))
button7 = tk.Button(window, text="7", command=buttonPress7, font=("Arial",50))
button8 = tk.Button(window, text ="8", command=buttonPress8, font=("Arial",50))
button9 = tk.Button(window, text="9", command=buttonPress9, font=("Arial",50))
#operator buttons/extras
buttonAdd = tk.Button(window, text="+", command=buttonPressAdd, font=("Arial", 25))
buttonSub = tk.Button(window, text ="-", command=buttonPressSub, font=("Arial",25))
buttonMul = tk.Button(window, text="x", command=buttonPressMul, font=("Arial",25))
buttonDiv = tk.Button(window, text ="÷", command=buttonPressDiv, font=("Arial",25))
buttonEq = tk.Button(window, text="=", command=buttonPressEq, font=("Arial",25))
buttonDot = tk.Button(window, text=".", command=buttonPressDot, font=("Arial", 25))

#making a label to display the numbers
numdisplay = tk.Label(window, textvariable=num, fg="white", bg="gray12", font=("Arial",50))


#displaying the elements
buttonAdd.place(x=211,y=80)
button0.place(x=70,y=335)
button1.place(x=0,y=250)
button2.place(x=70,y=250)
button3.place(x=140,y=250)
buttonSub.place(x=211,y=123)
buttonAdd.place(x=211,y=80)
button0.place(x=70,y=335)
button1.place(x=0,y=250)
button2.place(x=70,y=250)
button3.place(x=140,y=250)
button4.place(x=0,y=165)
button5.place(x=70,y=165)
button6.place(x=140,y=165)
button7.place(x=0,y=80)
button8.place(x=70,y=80)
button9.place(x=140,y=80)
numdisplay.grid(row=0,column=0)
window.mainloop()