import _22_Modules_01
"""
If a function will be used multiple time we can assign a local name for it
"""
bonus = _22_Modules_01.add_bonus

current_salary = 100000
new_salary = bonus(current_salary, 44, 2, 1)
print(current_salary, new_salary)