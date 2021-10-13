"""
Recursion: When a function calls itself
"""


def factorial(n: int):
    """
    Calculates the factorial
    :param n: number to calculate the factorial
    :return: factorial of n
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))

# A function can have no content (hopefully temporaraly) by using the pass statement


def emptyFunction():
    pass


print('emptyFunction():', emptyFunction())
