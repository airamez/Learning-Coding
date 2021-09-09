number = int(input("Number : "))

if number < 10:
  print("Less than 10")

if number % 2 == 0:
  print("EVEN")
else:
  print("ODD")

if number < 10:
  print(f"The Number {number} is ", end='')
  print("Less than 10")
elif number < 20:
  print(f"The Number {number} is ", end='')
  print("Between 10 and 20")
elif number < 30:
  print(f"The Number {number} is ", end='')
  print("between 20 and 30")
else:
  print(f"The Number {number} is ", end='')
  print("Greater than 30")

