"""
It is possible to import specific functions directly from a module
"""
from _22_Modules import add_bonus, increase_salary

current_salary = 100000

new_salary = increase_salary(current_salary, 20)
print(current_salary, new_salary)

new_salary = add_bonus(current_salary, 44, 2, 1)
print(current_salary, new_salary)