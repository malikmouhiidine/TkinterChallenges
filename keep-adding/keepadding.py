# importing the tkinter library
from tkinter import *

# defining "num" to use it later
num = 0


# adding num to user input 
def Call():
    # accessing global variable "num"
    global num
    # getting what in the entry box and seeing if it's empty
    if entry_box.get() == '':
        # returning false but that will not exit from the program
        return False
    # now if the input is not an empty string
    else:
        # adding num to user input(in the entry box)
        num = num + int(entry_box.get())
        # displaying message variable "num" and  background and font color and place proprietes
        msg = Label(window, text = str(num))
        msg["bg"] = "blue"
        msg["fg"] = "white"
        msg.place(relx=0.5, rely=0.4, width = 100, height = 25, anchor=CENTER)
        # changing the background color and font color of the button
        add_button["bg"] = "blue"
        add_button["fg"] = "white"


def Reset():
    # accessing global variable "num"
    global num
    # reseting num to 0
    num = 0
    msg = Label(window, text = str(num))
    # displaying message to show  that it's been reset to 0
    msg.place(relx=0.5, rely=0.4, width = 100, height = 25, anchor=CENTER)


# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=300, width=300)

# entry box widget
entry_box = Entry (text = 0)
# configuration "place and height and width"
entry_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)

# button widget that going to call the "Call" function when clicked
add_button = Button(text = "Add", command=Call)
# configuration "place and height and width"
add_button.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)


# button widget that going to call the "Reset" function when clicked
reset_button = Button(text = "Reset", command=Reset)
# configuration "place and height and width"
reset_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()