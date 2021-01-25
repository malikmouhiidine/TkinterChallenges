# importing the tkinter library
from tkinter import *
# importing csv module to write .csv files
import csv


# defining "list"(this list content that will be added to csv file)
list = []

# the function that will create or append a csv file contains what in the list
def Save():
    # Calling Call() function to check the input and add it to the list
    Call()
    # then check if list is empty
    if list == []:
        # if it is return false but that will not exit from the program
        return False
    # now if it's not an empty list
    # so we have to save what in the "list"
    else:
        # now creating the list.csv file and if there is a "list.csv" file in the Downloads directory it's just going to append content in it
        with open('C:\\Users\\frank\\Downloads\\list.csv', 'a', newline= '') as file:
            writer = csv.writer(file, dialect='excel')
            # going trough the data and writing it
            for i in list:
                # you notice the brackets around i
                # that is because witout them every char going to be saved to it's own column
                # e.g:
                    # without brackets    123 --> | 1 | 2 | 3 |
                    # with brackets       123 --> | 123 |
                writer.writerow([i[0],i[1]])
            # closing file
            file.close()

# function that going to get the content of two entry boxes and add it to the list
def Call():
    #accessing global variable "list"
    global list
    # getting what in the two entry boxes and seeing if one of them is empty
    # if it's empty return false
    if name_box.get() == '' or age_box.get() == '':
        # returning false but that will not exit from the program
        return False
    # now cheking if the age entry box contains non int value 
    elif not age_box.get().isdigit():
        # if it is return false
        return False
    # now if the values survive all these conditions they deserve to be rewarded
    else:
        # appending(adding) it to the list(both of them as a tuple)
        list.append(tuple((str(name_box.get()),int(age_box.get()))))

# the function that going to clear the list and the entry boxes
# NOTE: we need this Again function because if we don't clear the list the for loop in the Save() function going to append every time all the data in the list to the csv file
def Again():
    #accessing global variable "list"
    global list

    # clearing the entry boxes by getting first the length of the input and then starting by the first char to the last one
    name_box.delete(first=0,last=len(name_box.get()))
    age_box.delete(first=0,last=len(age_box.get()))
    
    # clearing the list
    list = []



# Daddy widget
window = Tk()
# configuration "height and width" of the window
window.config(height=300, width=300)

# name box widget
name_box = Entry ()
# configuration "place and height and width"
name_box.place(relx=0.5, rely=0.5, width = 100, height = 25, anchor=CENTER)
# a label next to the box like a title
name_label = Label(window, text = 'name')
name_label.place(relx=0.75, rely=0.5, width = 45, height = 25, anchor=CENTER)

# age box widget
age_box = Entry()
# configuration "place and height and width"
age_box.place(relx=0.5, rely=0.6, width=100, height=25, anchor=CENTER)
# a label next to the box like a title
age_label = Label(window, text = 'age')
age_label.place(relx=0.79, rely=0.6, width = 58, height = 25, anchor=CENTER)

# save button widget that going to call the "Save" function when clicked
save_button = Button(text = "Save", command=Save)
# configuration "place and height and width"
save_button.place(relx=0.5, rely=0.7, width=100, height=25, anchor=CENTER)

# again button widget that going to call the "Again" function when clicked
again_button = Button(text = "Again", command=Again)
# configuration "place and height and width"
again_button.place(relx=0.5, rely=0.8, width=100, height=25, anchor=CENTER)

# Daddy loop
window.mainloop()