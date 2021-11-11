# Class definition:
class claseName:
    # class content
    pass  # Indication of a emtpy class


# A class has attributes: Data and Method atributes
class MyClass:
    """This is a demo class"""  # docstring

    attribute_1 = "Attribute 1"

    def hello_world(self):
        return 'Hello World'


print(MyClass.__doc__)  # Special Attribute with docstring to the class

myObject = MyClass()  # An object is a instance of a class
print(myObject.attribute_1)
print(myObject.hello_world())
myObject.attribute_1 = 'Attribute 1.1'
print(myObject.attribute_1)


#A class with constructor
class MyClass:
    def __init__(self, attribute_1, attribute_2):  # Definition of a constructor method
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2


myObjectA = MyClass("Attr 1a", "Attr 2a")
myObjectB = MyClass("Attr 1b", "Attr 2b")

print(myObjectA.attribute_1)
print(myObjectA.attribute_2)

print(myObjectB.attribute_1)
print(myObjectB.attribute_2)
