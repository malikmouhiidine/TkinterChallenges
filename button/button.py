# importing the tkinter library
from tkinter import *

# action function 
def Call():
    # displaying a label (message)
    msg = Label(window, text = "You pressed the button")
    # message configuration "place"
    msg.place(x= 30, y= 50)
    # changing the background color and font color of the button
    button["bg"] = "blue"
    button["fg"] = "white"

# Daddy widget
window = Tk()
# configuration "height and width"
window.geometry("200x110")

# button widget that going to call the "Call" function when clicked
button = Button(text = "Press me", command=Call)
# configuration "place and height and width"
button.place(x= 30, y=20, width=120, height=25)

# Daddy loop
window.mainloop()