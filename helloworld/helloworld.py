# importing the tkinter library
from tkinter import *

# action function 
def Call():
    # getting what in the entry box
    name = str(entry_box.get())
    # displaying message with variable "name" and  background and font color and place proprietes
    msg = Label(window, text = "Hello "+ name)
    msg["bg"] = "blue"
    msg["fg"] = "white"
    msg.place(relx=0.5, rely=0.4, width = 100, height = 25, anchor=CENTER)
    # changing the background color and font color of the button
    button["bg"] = "blue"
    button["fg"] = "white"

# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=300, width=300)

# entry box widget
entry_box = Entry (text = 0)
# configuration "place and height and width"
entry_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)

# button widget that going to call the "Call" function when clicked
button = Button(text = "Press me", command=Call)
# configuration "place and height and width"
button.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()