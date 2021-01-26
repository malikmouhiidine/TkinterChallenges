# importing the tkinter library
from tkinter import *
# importing csv to read csv file
import csv
# defining list to use it later
list = []

# main function(reading then adding csv rows to the list and displaying it in a list_box)
def Call():
    global list
    # getting what in the entry box and seeing if it's empty
    # if it's empty return false
    if filename_box.get() == '':
        # returning false but that will not exit from the program
        return False
    # here where trying so if file not found we raise an exception
    try:
        # now if the user enter the file extention too
        if filename_box.get()[-4:] == '.csv':
            # so we pick the input without extension Then we add it ourselves 
            # both ways work change it if you like too  
            # of course change the path to be your downloads directory  
            with open(f'C:\\Users\\frank\\Downloads\\{filename_box.get()[:len(filename_box.get())-4]}.csv', 'r', newline= '') as file:
                csv_reader = csv.reader(file, delimiter=',')
                # here where adding every row in the file to the list
                for row in csv_reader:
                    list.append(row)
        else:
            # and if he didn't add the extention we just concating it with "".csv"
            with open(f'C:\\Users\\frank\\Downloads\\{filename_box.get()}.csv', 'r', newline= '') as file:
                csv_reader = csv.reader(file, delimiter=',')
                # here where adding every row in the file to the list
                for row in csv_reader:
                    list.append(row)
    # and here if file not found error occurs
    except FileNotFoundError:
        file_notfound_label = Label(window, text = "File not found." )
        file_notfound_label.place(relx=0.4, rely=0.54, width = 100, height = 25, anchor=CENTER)
        return False

    

    # here is the listbox that going to show the content of the "list"
    list_box = Listbox(window)
    # place, width and height proprietes
    list_box.place(relx=0.5, rely=0.35, width = 440, height = 150, anchor=CENTER)
    # defining j to use it in the for loop
    j = 0
    # starting the fore loop
    for i in list:
        # going into every element in the list and inserting it into the list_box
        list_box.insert(j,i)
        # increment 'j' for the next loop
        j+=1
    # changing the background color and font color of the button
    open_button["bg"] = "blue"
    open_button["fg"] = "white"


# Daddy widget
window = Tk()
# configuration "height and width"
window.config(height=250, width=450)

# the file name box widget
filename_box = Entry (text = 0)
# configuration "place and height and width"
filename_box.place(relx=0.4, rely=0.74, width = 100, height = 25, anchor=CENTER)
# a label next to the box like a title
filename_label = Label(window, text = "the name of the file" )
filename_label.place(relx=0.68, rely=0.75, width = 150, height = 25, anchor=CENTER)

# button widget that going to call the "Call" function when clicked
open_button = Button(text = "Open", command=Call)
# configuration "place and height and width"
open_button.place(relx=0.4, rely=0.85, width=100, height=25, anchor=CENTER)
# a label next to the box like a title
open_label = Label(window, text = 'it should be in downloads folder')
open_label.place(relx=0.75, rely=0.85, width = 200, height = 25, anchor=CENTER)


# Daddy loop
window.mainloop()