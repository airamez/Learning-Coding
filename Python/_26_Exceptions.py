"""
When a program is executing even if the program has no errors caused by syntax or logic, some errors can potentially occur. Examples: lost connection, wrong data entry, disk failure, timeout, etc.
Those errors are called Exceptions and every program language offer a mechanism to deal with them to avoid the program to crash.
The majority of programing languages use a mechanism following the concept of TRY / CATCH
try     -> commands are executed normally
catch   -> the potential exceptions/errors are handled
finally -> some cleanup code
This way the "real" code stays separated from the code to deal with the errors 
"""


def read_integer(prompt: str = "Type an integer number = ") -> int:
    """
    Read an integer number
    :param prompt: Input label
    :return: An integer number
    """
    while True:
      try:
          # if the conversion to int fails, an exception will be reaised
          number = int(input(prompt))
          return number
      except ValueError:
          print("Invalid number. Please try again!")


my_int = read_integer()
print("My int", my_int)
my_age = read_integer("Age = ")
print("My age =", my_age)
