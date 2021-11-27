# A logical expression is a statement that can either be true or false.
# It is the fundation of computer programming decision making
# Comparison Operators
# >   : greather than
# >=  : greater than or equal
# <   : less than
# <=  : less than or equal
# ==  : equal
# !=  : not equal

# Logical Operator: and or not

# Tip:
# and: is True only if all expressions are true. Just need one false to return false
# or: is False only if all expressions are false. Just need one true to return true

n1 = 5
n2 = 3
n3 = 2
print(f"{n1} == 5: {n1 == 5}")
print(f"{n1} >= {n2} + 3: {n1 >= n2 + 3}")
print(f"{n1} > {n2} and {n1} > {n3}: {n1 > n2 and n1 > n3}")
print(f"{n2} > {n1} or {n2} > {n3}: {n2 > n1 or n2 > n3}")

print(f"n3 < n2 < n1 = {n3 < n2 < n1}")

print("True = ", True)
print("False = ", False)
print("not True = ", not True)
print("not False = ", not False)

