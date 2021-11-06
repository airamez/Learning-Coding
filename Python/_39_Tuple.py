import random

MIN = 0
MAX = 99
numbers_tuple = (random.randint(MIN, MAX), random.randint(MIN, MAX),
                 random.randint(MIN, MAX), random.randint(MIN, MAX),
                 random.randint(MIN, MAX), random.randint(MIN, MAX),
                 random.randint(MIN, MAX), random.randint(MIN, MAX))

# Min and Max
print(numbers_tuple)
print("MAX =", max(numbers_tuple))
print("MIN =", min(numbers_tuple))

# Create a list from a tuple
numbers_list = list(numbers_tuple)

numbers_list[0] = 1
numbers_list[1] = 2
numbers_list[len(numbers_list) - 1] = 9

print(numbers_list)
print(numbers_tuple)

# Creating a tuple from a list
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
