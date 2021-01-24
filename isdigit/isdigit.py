# importing the tkinter library
from tkinter import *

# defining "list"
list = []


# main function(adding to the int to the list and displaying a list_box)
def Call():
    #accessing global variable "list"
    global list
    # getting what in the entry box and seeing if it's empty
    # if it's empty return false
    if entry_box.get() == '':
        # returning false but that will not exit from the program
        return False
    # now if it's not a digit A.K.A integer
    # that will clear the entry box
    elif not entry_box.get().isdigit():
        # calling .delete() function to clear the entry_box
        entry_box.delete(0, 'end')
    # now if the input is not an empty string and it's a digit
    else:
        # appending(adding) the input to the list
        list.append(str(entry_box.get()))
        # showing a listbox to list what in the [list]
        list_box = Listbox(window)
        # place, width and height properties
        list_box.place(relx=0.5, rely=0.28, width = 100, height = 100, anchor=CENTER)
        # defining j to use it in the for loop
        j = 0
        # starting the for loop
        for i in list:
            # going into every element in the list and inserting it into the list_box
            list_box.insert(j,i)
            # increment 'j' for the next loop
            j+=1
        # changing the background color and font color of the button
        add_button["bg"] = "blue"
        add_button["fg"] = "white"

# reset function(clearing the list and displaying an empty list_box)
def Reset():
    # accessing global variable "list"
    global list
    # clearing list
    list = []
    # showing that the list has been cleared
    list_box = Listbox(window)
    # place, width and height properties
    list_box.place(relx=0.5, rely=0.28, width = 100, height = 100, anchor=CENTER)


# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=300, width=300)

# entry box widget
entry_box = Entry (text = 0)
# configuration "place and height and width"
entry_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)

# button widget that going to call the "Call" function when clicked
add_button = Button(text = "Add integer", command=Call)
# configuration "place and height and width"
add_button.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)


# button widget that going to call the "Reset" function when clicked
reset_button = Button(text = "Reset", command=Reset)
# configuration "place and height and width"
reset_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()