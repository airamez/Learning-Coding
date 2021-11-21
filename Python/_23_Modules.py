"""
A module is just a file with functions that we can referenced from other Python files
When we import a module the function names must have the module name plus . as a suffix: module.function
"""
import _22_Modules  # Name of the module file

current_salary = 100000
new_salary = _22_Modules.increase_salary(current_salary, 20)
print(current_salary, new_salary)
