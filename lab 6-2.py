"""
Create a Python file named lab_6-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a variable my_row and set it equal to a list that contains the names of 2 people in your row.
Using slices, add your name to the end of the list.
Create another variable my_row2 and set it equal to my_row.
Add a statement that prints my_row2
Add a statement that removes the value at index 1 from my_row
Add a statement that prints my_row. What do you notice happens and why?

"""
#created a variable my_row and set it equal to a list that contians 
my_row = ["naz","jon","matt"]
# used slices, add my name to the end of list.
my_row += "naz"
# created another variadle my_row2 and ste it eqaul to my_row
my_row2 = my_row
#prints my_row2
print("my_row2:", my_row2)
#removes the value at index 1 from my_row
del my_row[1]
# print my_row
print("my_row:",my_row)

