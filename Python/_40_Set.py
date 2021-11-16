import random

# Declaring a Set
prime_numbers = {1, 2, 3, 5, 7, 11, 17, 1, 2, 3, 5}
print("Type: ", type(prime_numbers))
print("Prime Number =", prime_numbers)
print(len(prime_numbers))

# Using just {} does not create a Set but a Dictionary instead
not_a_set = {}
print("Type: ", type(not_a_set))

# Declaring an empty Set and adding elements
prime_numbers = set()
prime_numbers.add(1)
prime_numbers.add(2)
prime_numbers.add(3)
prime_numbers.add(5)
prime_numbers.add(7)
prime_numbers.add(11)
prime_numbers.add(17)
prime_numbers.add(1)
prime_numbers.add(2)
prime_numbers.add(3)
print(f'Set size: {len(prime_numbers)}')
print("Prime Number =", prime_numbers)

print('Removing 17')
prime_numbers.remove(17)
print("Prime Number =", prime_numbers)

try :
  prime_numbers.remove(17)
except KeyError as ex:
  print(type(ex), ex)

# Creating a set of random values
set_a = set()
for i in range(0, 10):
    set_a.add(random.randint(1, 20))
print("Set A = ", set_a)

# Creating a set of random values
set_b = set()
for i in range(0, 5):
    set_b.add(random.randint(1, 20))
print("Set B =", set_b)

# Union
union = set.union(set_a, set_b)
print("Union =", union)

# Difference A - B
diff_a_b = set.difference(set_a, set_b)
print("A diff B =", diff_a_b)

# Difference B - A
diff_b_a = set.difference(set_b, set_a)
print("B diff A =", diff_b_a)

# Intersection
intersection = set.intersection(set_a, set_b)
print("Intersection = ", intersection)

# Checking if a element exist in a Set
print("Set A = ", set_a)
for i in range(0, 10):
    rnd = random.randint(1, 20)
    found = rnd in set_a  # Check if an element exists in the Set
    print(f'{rnd} => ', end='')
    if (found):
        print("Found")
    else:
        print("Not Found")

# Creating a set from a list
numbers = [5, 7, 6, 2, 2, 3, 4, 5, 4, 3, 4, 1]
unique_numbers = set(numbers)
print(numbers)
print(unique_numbers)