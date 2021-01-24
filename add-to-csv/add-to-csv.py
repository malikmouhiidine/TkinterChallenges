# importing the tkinter library
from tkinter import *
# importing csv module to write .csv files
import csv


# defining list_box(this will end up as a list box widget)
list_box = []
# defining "list"(this list will be the content that the list box will show)
list = []

# main function(adding to the int to the list and displaying a list_box)
def Call():
    #accessing global variable "list" and "list_box"
    global list, list_box
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

# the function that will create and save a csv file contains what in the list_box widget
def Save():
    # first if it's assigned to an empty list that maeans that the user still didn't enter something
    if list_box == []:
        # so return false but that will not exit from the program
        return False
    # now if it's not an empty list
    # so we have to save what in the "list"
    else:
        # assigning list_box.get() just for short  !(it's going to be a tuple) e.g (1, 2, 3)
        list = list_box.get(0,END)
        # now opening the list.csv file and by opening it i mean creating the list.csv file
        # create list.csv in the Downloads directory 
        with open('C:\\Users\\frank\\Downloads\\list.csv', 'w', newline= '') as file:
            writer = csv.writer(file, dialect='excel')
            # going trough the data and writing it
            for i in list:
                # you notice the brackets around i
                # that is because witout them every char going to be saved to it's own column
                # without brackets    123 --> | 1 | 2 | 3 |
                # with brackets       123 --> | 123 |
                writer.writerow([i])
            # closing file
            file.close()


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

# add button widget that going to call the "Call" function when clicked
add_button = Button(text = "Add", command=Call)
# configuration "place and height and width"
add_button.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)

# save button widget that going to call the "Save" function when clicked
save_button = Button(text = "Save", command=Save)
# configuration "place and height and width"
save_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)

# reset button widget that going to call the "Reset" function when clicked
reset_button = Button(text = "Reset", command=Reset)
# configuration "place and height and width"
reset_button.place(relx=0.5, rely=0.8, width=100, height=25, anchor=CENTER)


# Daddy loop
window.mainloop()