# The equal sign means assignment.
# We already used it multiple times :)
name = "José Santos"

# Multiple assigments in one line (PLEASE AVOID IT)
n1, n2, n3, name = 5, 10, 15, "José Santos"
print(n1, n2, n3, name)

# One value to multiple variables
a = b = c = d = e = 15
print(a, b, c, d, e)

# Python way to switch variables :P
# no need to aux = n1; n1 = n2; n2 = aux
print('n1 AND n2:', n1, n2)
n1, n2 = n2, n1
print('n1 AND n2:', n1, n2)

print("n1 =", n1)

n1 += 1
print("n1 atfer += 1 =", n1)

n1 -= 3
print("n1 after -= 3 =", n1)

n1 *= 2
print("n1 after *2 =", n1)

n1 /= 2
print("n1 after /=2 =", n1)

n1 = -n1
print("n1 after -n1 =", n1)

# THERE IS NO ++ OR -- IN PYTHON :)

print("OPERATION PRIORITY")
average = (n1 + n2 + n3) / 3
print("The average of", n1, ",", n2, "and", n3, "is", average)
