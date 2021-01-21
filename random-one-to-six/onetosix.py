# importing the tkinter library
from tkinter import *
# importing random for random integer 
from random import randint

def Call():
    # displaying the random number
    msg = Label(window, text = "it's "+ str(randint(1, 6)))
    # background and font color and place proprietes
    msg["bg"] = "blue"
    msg["fg"] = "white"
    msg.place(relx=0.5, rely=0.4, width = 100, height = 25, anchor=CENTER)
    # changing the background color and font color of the button
    button["bg"] = "blue"
    button["fg"] = "white"

# Daddy widget
window = Tk()
# configuration of the window "height and width"
window.config(height=300, width=300)

# button widget that going to call the "Call" function when clicked
button = Button(text = "Let's see!", command=Call)
# configuration of the button "place and height and width"
button.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()