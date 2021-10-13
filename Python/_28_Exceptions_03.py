"""
It is possible to catch multiple exceptions 
"""


def my_division(number_1: float, number_2: float) -> float:
    try:
        return float(number_1) / float(number_2)
    except ValueError:
        raise Exception(f"Invalid parameters: {number_1}/{number_2}")
    except ZeroDivisionError:
        raise Exception(f"Division by zero: {number_1}/{number_2}")


try:
    print('my_division(10, 4) =', my_division(10, 4))
except Exception as ex:
    print("ERROR =>", ex)

try:
    div = my_division("Python", 2)
except Exception as ex:
    print("ERROR =>", ex)

try:
    div = my_division(10, 0)
except Exception as ex:
    print("ERROR =>", ex)

while True:
    try:
        number1 = float(input("Number 1 = "))
        number2 = float(input("Number 2 = "))
        division = my_division(number1, number2)
        print("Division = ", division)
        break
    except Exception as my_exception:
        print("ERROR =>", my_exception)

# An exception not caught will stop the program
print('my_division("Python", 2) =', my_division("Python", 2))
