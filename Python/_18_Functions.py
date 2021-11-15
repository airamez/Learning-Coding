"""
Function with default parameter
"""


def repeat(string, times=10):  # Default parameter
    """
    Function to repeat a string N times
    :param string: string
    :param times: how many times the string will be repeated
    :return: repeated string
    """
    result = ''
    for i in range(1, times + 1):
        result += string
    return result


print(repeat('*'))
print(repeat('*', 5))
print(repeat('*', 1))
print(repeat('='))
print(repeat('=', 80))
print(repeat(' ', 35), end='')
print('This is a function in action')
print(repeat('=', 80))
print(repeat('='))

"""
Function with undefined list of parameters
"""

def my_print(*values):
  for v in values:
    print(v) 

my_print('José')
my_print('José', 'Leila', 'Artur')