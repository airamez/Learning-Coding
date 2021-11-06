"""
Function that does not return a value.
In many programming languages when a function doesn't not return a value it is called "procedure"
"""


def my_print(name: str, salary: float, age: int):
    if not name:
        # Even the function not returning a value the return statement ends the function and the especial value
        # None is returned
        return
    print(f'{{"Name":{name}, "Salary":{salary}, "Age": {age}}}')


return_value = my_print("José Santos", 150000, 45)

# Remember that every function in Python returns a value. None if not specified
print(return_value)

my_print(age=45, name="José Santos", salary=150000)

my_print("Michael Jordan", 999999999, 50)
my_print("", 1000, 18)
my_print(None, 1000, 18)
