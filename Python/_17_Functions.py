"""
A function is a block of code that is used to perform an action.
Functions help to keep your code clean, easy to understand and test, provide better modularity for your application and a high degree of code reusing.
A Function represents a "mini-program" that can be executed with or without parameters and returns a value.
The "return" statement indicates the value that will be returned by he Function.
The return statement of a function terminate the function execution and return the value.
Every function in python returns a value even if the function does not have a return statement
In this case the special value "None" will be return at the end of the Function execution.
In computer programming when a Function doesn't not have a return statement it is called a Procedure. However in Python there is no concept of Procedure.
"""

# Two blank likes are required before a function


def average(number1, number2, number3):
    """
    ATTENTION: This documention will be used to assist the programmer
    Function to return the average of 3 numbers
    :param number1: Number 1
    :param number2 : Number 2
    :param number3 : Number 3
    :return: The average of the three numbers
    """
    return (number1 + number2 + number3) / 3


# Try to re-type the first parentesis and observe the documentation
print(average(5, 15, 25))
print(average(15, 25, 5))
print(average(number3=25, number1=15, number2=5))

num1 = float(input("Number 1 = "))
num2 = float(input("Number 2 = "))
num3 = float(input("Number 3 = "))

# The parameter os a functions can be passed in order
avg = average(num1, num2, num3)
print(avg)

# The parameters of a function can be passed by the name
avg = average(number1=num1, number2=num2, number3=num3)
print(avg)

avg = average(number3=num1, number2=num2, number1=num3)
print(avg)
