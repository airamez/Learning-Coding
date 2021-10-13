'''
if statement is a programming conditional statement that: 
  - if proved true, executes a set of commands
  - and optionally if false executes another set of commands

Python indentation is a way of telling a Python interpreter that the group of statements
belongs to a particular block of code. A block is a combination of all these statements.
'''

number = int(input("Integer Number : "))

if number < 10:
    print("{number}", end='')
    print(" is less than 10")

if number % 2 == 0:
    print(f'{number} is ', end='')
    print("EVEN")
else:
    print(f'{number} is ', end='')
    print("ODD")

if number < 10:
    print(f'{number} is ', end='')
    print("Less than 10")
elif number < 20:
    print(f'{number} is ', end='')
    print("Between 10 and 20")
elif number < 30:
    print(f'{number} is ', end='')
    print("between 20 and 30")
else:
    print(f'{number} is ', end='')
    print("Greater than 30")

# Inline if expression
age = int(input('Type your age: '))
message = "Adult" if age >= 18 else "Young"
print(message)

# Practices
'''
# 1 - Read the age of a person and print the age classification using the table below
    Fetus/unborn
    Infants: < 1
    Children: 1 to 12 years
    Teens: 13 to 17
    Adults: 18 to 55
    Senior: 55 to 75
    Old: 76+
  2 - Read an year and print if it is a Leap Year or Not

'''
