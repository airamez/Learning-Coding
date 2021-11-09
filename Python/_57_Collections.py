'''
Lambda expression
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''
multiply = lambda a, b : a * b
print(multiply(2, 5))
print(multiply(3, 7))

months = [
    "january", "february", "march", "april", "may", "june", "july", "august",
    "september", "october", "november", "december"
]

'''
Map: applies a function to all the items in an input_list
'''
print(months)
months = list(map(lambda month: month.capitalize(), months))
print(months)
months_initials = list(map(lambda month: month[0:3], months))
print(months_initials)

'''
Filter: creates a list of elements for which a function returns true
'''
months_starting_with_m = list(filter(lambda month: month.startswith('M'), months))
print(months_starting_with_m)

'''
Reduce: Apply function of two arguments cumulatively to the items of iterable, 
from left to right, so as to reduce the iterable to a single value
'''
import functools
numbers = [1, 3, 5, 7, 9]
result = functools.reduce(lambda x, y: x + y, numbers)
print(result)
print(sum(numbers))
result = functools.reduce(lambda x, y: x * y, numbers)
print(result)

'''
Sorting a list of objects
'''

class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary
    def __repr__(self):  # Special method to return a string representation of the object
        return f'[{self.name}, {self.dept}, {str(self.salary)}]'

employees = []
employees.append(Employee('Jose', 'IT', 150000))
employees.append(Employee('Leila', 'RH', 250000))
employees.append(Employee('Artur', 'R&D', 750000))
employees.append(Employee('Thor', 'R&D', 750000))
employees.append(Employee('Maya', 'R&D', 750000))

print(employees)

employees.sort(key = lambda e: e.name) # Sort by name
print(employees)

employees.sort(key = lambda e: (e.dept, e.name)) # Sort by dept and name
print(employees)

employees.sort(key = lambda e: e.salary) # Sort by salary
print(employees)
