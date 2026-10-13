import matplotlib as plt
import tkinter as tk
from tkinter import ttk

#set up the window
window = tk.Tk()
window.title("Graphical Calculator")
window.geometry("300x400")
window.configure(background = "gray12")

#declaring variables
number = ""
num = tk.IntVar()

#button functions
def buttonPress7(number):
    number = str(7) + number
    num.set(number)

def buttonPress8():
    num.set(8)

#declaring the buttons
button7 = ttk.Button(window, text="7", command=buttonPress7)
button8 = ttk.Button(window, text ="8", command=buttonPress8)

#making a label to display the numbers
numdisplay = tk.Label(window, textvariable=num, fg="white", bg="gray12", font=("Arial",25))


#displaying the elements
button8.grid(row=1, column=1)
button7.grid(row=1,column=0)
numdisplay.grid(row=0,column=0)
window.mainloop()