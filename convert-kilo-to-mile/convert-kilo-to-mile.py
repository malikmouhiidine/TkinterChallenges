# importing the tkinter library
from tkinter import *

# defining msg variable and where going to use it in two functions
msg = ''

# converting kilo to mile or mile to kilo
def Call():
    # accessing msg global variable
    global msg
    # assigning mile and kilo just for short
    mile = mile_box.get()
    kilo = kilo_box.get()
    # checking if both inputs are empty
    if mile == '' and kilo == '':
        # if so return false
        return False
    # now if mile input is not empty so where going to convert from mile to kilo
    elif mile != '':
        # but first let see if it's digit
        if not mile.isdigit():
            # if false return false
            return False
        # else: convert the input to float and assing it to mile
        mile = float(mile)
        # mile_input * 1.6093 is the formula to get the kilo value
        mile = mile * 1.6093
        # showing a message with the result
        msg = Label(window, text = str(round(mile, 3)))
        # place, width and height properties
        msg.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)
    # now if kilo input is not empty so where going to convert from kilo to mile
    else:
        # but first let see if it's digit
        if not kilo.isdigit():
            # if false return false
            return False
        # else: convert the input to float and assing it to kilo
        kilo = float(kilo)
        # kilo_input * 0.6214 is the formula to get the mile value 
        kilo = kilo * 0.6214
        # showing a message with the result
        msg = Label(window, text = str(round(kilo, 3)))
        # place, width and height properties
        msg.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)
    # set the color, background of the message
    msg["bg"] = "blue"
    msg["fg"] = "white"

    # changing the color, background of the button
    convert_button["bg"] = "blue"
    convert_button["fg"] = "white"

# again function to remove the result Label
def Again():
    # destroying the label
    msg.destroy()


# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=300, width=300)

# mile box widget
mile_box = Entry ()
# configuration "place and height and width"
mile_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)
# a label next to the box like a title
mile_label = Label(window, text = 'miles')
mile_label.place(relx=0.75, rely=0.5, width = 45, height = 25, anchor=CENTER)

# kilo box widget
kilo_box = Entry()
# configuration "place and height and width"
kilo_box.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)
# a label next to the box like a title
kilo_label = Label(window, text = 'kilometres')
kilo_label.place(relx=0.79, rely=0.6, width = 58, height = 25, anchor=CENTER)

# convert button widget that going to call the "Call" function when clicked
convert_button = Button(text = "Convert", command=Call)
# configuration "place and height and width"
convert_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)

# again button widget that going to call the "Again" function when clicked
again_button = Button(text = "Again", command=Again)
# configuration "place and height and width"
again_button.place(relx=0.5, rely=0.8, width=100, height=25, anchor=CENTER)

# Daddy loop
window.mainloop()