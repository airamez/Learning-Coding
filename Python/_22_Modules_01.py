"""
A module is just a file with functions that we can referenced from other Python files/programs
When we import a module the function names must have the module name plus . as a suffix: module.function
"""


def increase_salary(current_salary, increase_percent):
    """
    Increase a salary based on a percentage value
    :param current_salary: current salary
    :param increase_percent: increase percentage value
    :return: increased salary
    """
    return current_salary + current_salary * increase_percent / 100


def add_bonus(current_salary, age, years_of_work, dependents):
    """
    Add bonus do a salary
    :param current_salary: current salary
    :param age: age
    :param years_of_work: years working for the company
    :param dependents: number of dependents
    :return: new salary with bonus added
    """
    bonus = 0
    if age > 40:
        bonus += 10
    else:
        bonus += 5
    bonus += years_of_work
    bonus += dependents / 2
    return increase_salary(current_salary, bonus)
