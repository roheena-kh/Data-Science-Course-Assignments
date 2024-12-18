'''Numpy is a python open_source library that used for numerical and scientific computing.
it needs to be imported in the top of python file.'''
import numpy as np
num = np.array([2, 4, 3, 7, 1])
c = num ** 2
print(c)


'''What is concatenation?
Concatenation is a process to connect strings, variables, structures and numbers.'''
numbers_1 = [1, 3, 5, 6, 7, 9]
numbers_2 = [5, 7, 5, 8, 3, 8, 2]
new_list = numbers_1 + numbers_2
print(new_list)

# Concatenating strings
name = "Roheena"
l_name = "Khairi"
print(name + " " + l_name)


# what is File Handling.
# File handling is the process for creating and deleting files as well as reading from  and writing in them
with open('first_file.txt', 'w') as file:
    file.write("Hello, This is Roheena!")

# Read from the file
with open('first_file.txt', 'r') as file:
    content = file.read()
    print(content)


'''OOP(Object oriented programming): is a programming language module that revolves around objects instead of function and logic.
combining a group of objects and functions to a unit.
OOP is efficient for code reusability. '''

'''Class, Constructor, self method, object
Class: A class is a blueprint that objects can be created based on it.

Constructor: is a specific method that is used for instantiating an object, and initialize the object's attributes.

Self: used to refer to an objects and allow to used the object methods and attributes.

object:In OOP programming and object is an instance from a class the consist property and behavior
'''


class Jeans:
    # constructor for initializing the object attributes.
    def __init__(self, style, color):
        # Here, self is used to access style and color as the class attributes
        self.style = style
        self.color = color

    def info(self):
        return f"This is a {self.style} style jean in {self.color} color. "

    def buy(self):
        return f"For buying the {self.style} in {self.color} color you can click the link bellow."


# Creating an object for the Jeans class
The_Jean = Jeans("Buggy", "Black")
print(The_Jean.info())
print(The_Jean.buy())

''' What is a inheritance?
Inheritance is a mechanism that allow one class(child class) to use the attributes and methods from another class(parent class).
'''


# this is a class that contain literary piece.
class Art_piece:
    def _init_(self, name, genre):
        self.name = name
        self.genre = genre

    def art_info(self):
        return f"{self.name} is an example of {self.genre} gener."


class Book(Art_piece):
    def __init__(self, name, genre, author):
        # need to call the parent class constructor
        super()._init_(name, genre)
        self.author = author

    def art_info(self):
        return f"{self.name} is an example of {self.genre} gener which is written by {self.author}"


# creating an object
my_book = Book("The 5 Second rule", "Personal developments ", "Mel Robbins")
print(my_book.art_info())


