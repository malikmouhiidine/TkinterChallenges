# importing the tkinter library
from tkinter import *


# adding num to user input 
def Call():
    mile = mile_box.get()
    kilo = kilo_box.get()
    if mile == '' and kilo == '':
        return False
    elif mile != '':
        if not mile.isdigit():
            return False
        mile = float(mile)
        # 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres.
        mile = mile * 1.6093
        msg = Label(window, text = str(round(mile, 2)))
        msg.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)
    else:
        if not kilo.isdigit():
            return False
        kilo = float(kilo)
        # 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres.
        kilo = kilo * 0.6214
        msg = Label(window, text = str(round(kilo, 2)))
        msg.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)
    msg["bg"] = "blue"
    msg["fg"] = "white"

    # changing the background color and font color of the button
    convert_button["bg"] = "blue"
    convert_button["fg"] = "white"


# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=300, width=300)

# entry box widget
mile_box = Entry ()
# configuration "place and height and width"
mile_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)
mile_label = Label(window, text = 'miles')
mile_label.place(relx=0.75, rely=0.5, width = 45, height = 25, anchor=CENTER)

# button widget that going to call the "Call" function when clicked
kilo_box = Entry()
# configuration "place and height and width"
kilo_box.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)
kilo_label = Label(window, text = 'kilometres')
kilo_label.place(relx=0.79, rely=0.6, width = 58, height = 25, anchor=CENTER)

# button widget that going to call the "Reset" function when clicked
convert_button = Button(text = "Convert", command=Call)
# configuration "place and height and width"
convert_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()