n1, n2, n3, name = 5, 10, 15, "José Santos"
print(f"{n1} {n2} {n3} {name}")

# One value to multiple variables
a = b = c = d = e = 15
print(a, b, c, d, e)

# Python way to switch variables :P
# no need to aux = n1; n1 = n2; n2 = aux
n1, n2 = n2, n1
print(f"{n1} {n2}")

n1 += 1
print(n1)

n1 -= 1
print(n1)

n1 *= 2
print(n1)

n1 /= 2
print(n1)

n1 = -n1;
print(n1)

# THERE IS NO ++ OR -- IN PYTHON

print("OPERATION PRIORITY")
average = (number1 + number2 + number3) / 3
print("The average of {0}, {1} and {2} is {3}".format(number1, number2, number3, average))