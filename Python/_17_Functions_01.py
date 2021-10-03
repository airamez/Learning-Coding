"""
A function is a block of code that is used to perform an action.
Functions help to keep your code clean, easy to understand, provide better modularity for your application and a high degree of code reusing.
A Function represents a "mini-program" that can be executed with or without parameters and returns a value.
The "return" statement indicates the value that will be returned by he Function.
The return statement of a function terminate the function execution and return the value.
Every function in python returns a value even if the function does not have a return statement
In this case the special value "None" will be return at the end of the Function execution.
In computer programming when a Function doesn't not have a return statement it is called a Procedure. However in Python there is no concept of Procedure.
"""

# Two blank likes are required before a function


def average(number1, number2, number3):
    return (number1 + number2 + number3) / 10

print(average(5, 15, 25))
print(average(15, 25, 5))
print(average(number3=25, number1=15, number2=5))

num1 = int(input("Number 1 = "))
num2 = int(input("Number 2 = "))
num3 = int(input("Number 3 = "))

# The parameter os a functions can be passed in order
avg = average(num1, num2, num3)
print(avg)

# The parameters of a function can be passed by the name
avg = average(number1=num1, number2=num2, number3=num3)
print(avg)

avg = average(number3=num1, number2=num2, number1=num3)
print(avg)