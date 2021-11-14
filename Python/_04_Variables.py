"""
VARIABLES
A computer is a special machine that operates on data (information) and variables are the basic structures to store data/information.
"""
"""
IDENTIFIERS
An identifier is a name used to identify something in a program.
In Python an identifier is case sensitive, and starts with a letter, or
an underscore (_) followed by zero or more letters, underscores or digits (0 to 9)
PS: An identifier can't start with a number (This is valid for all languages I know)
RESERVED WORDS:
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
"""

# Integer
age = 44  # Declaring and assigning an integer value
print(type(age), 'age = ', age)  # Prints to the default output

# Floating point
payment = 345.67
print(type(payment), 'payment = ', payment)

# Boolean
approved = True
print(type(approved))
print("approved =", approved)
approved = False
print("approved =", approved)

# String
name = "José Maria"
print(type(name), "name =", name)

last_name = 'Rodrigues Santos Júnior'
print('full name =', name, last_name)
