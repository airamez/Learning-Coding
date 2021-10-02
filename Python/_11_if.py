'''
An if statement is a programming conditional statement that: 
  	if proved true, executes a set of commands
    and optionally if false executes another set of commands
'''

number = int(input("Number : "))

# If statment
if number < 10:
  print(f"{number} is less than 10")

print(f'{number} is ', end='')
if number % 2 == 0:
  print("EVEN")
else:
  print("ODD")

  print(f"The Number {number} is ", end='')
if number < 10:
  print("Less than 10")
elif number < 20:
  print("Between 10 and 20")
elif number < 30:
  print("between 20 and 30")
else:
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