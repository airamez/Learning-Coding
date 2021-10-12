# Function to demonstrate Unit Testing


def factorial(n: int):
    """
    Calculate the factional of a number
    :param n: n
    :return: factorial
    """
    fat = 1
    while n >= 2:
        fat *= n
        n -= 1
    return fat