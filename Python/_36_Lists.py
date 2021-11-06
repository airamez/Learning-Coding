"""
Bi-dimensional lists
Most of programming languages offer a bi-dimensional collection called Matrix however Python doesn't not
offer an built-in matrix component. Like Arrays it is possible to simulate an Matrix by creating a list of lists.
"""
import random

matrix = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

print("#1 Using print with a 'matrix'")
print('Type = ', type(matrix))
print(matrix)

print("\n#2 Printing a matrix")
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], "", end="")
    print()

# Creating a "matrix" 5 x 10
lines = 5
rows = 10
matrix = [[0 for i in range(rows)] for j in range(lines)]
print(matrix)

# Filling a matrix with random numbers
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        matrix[i][j] = random.randint(100, 500)

print("\n#3 Printing the matrix 5 x 10")
print(matrix)

print("\n#4 Printing the matrix 5 x 10")
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], "", end="")
    print()

# Creating an empty "matrix" and adding values to it
matrix = list()

matrix.append([])
matrix[0].append(1)
matrix[0].append(2)
matrix[0].append(3)

matrix.append([])
matrix[1].append(4)
matrix[1].append(5)
matrix[1].append(6)

matrix.append([])
matrix[2].append(7)
matrix[2].append(8)
matrix[2].append(9)

print('\n#5Printing the matrix')
print(matrix)
