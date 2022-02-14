from itertools import permutations

def check(matrix):
  row0 = row1 = row2 = col0 = col1 = col2 = diagPrin = diagSec = 0
  for i in range(3):
    row0 += matrix[0][i]
    row1 += matrix[1][i]
    row2 += matrix[2][i]
    col0 += matrix[i][0]
    col1 += matrix[i][1]
    col2 += matrix[i][2]
    diagPrin += matrix[i][i]
    diagSec += matrix[i][3 - (i + 1)]
  return row0 == row1 == row2 == col0 == col1 == col2 == diagPrin == diagSec

def generateSolutions():
  solutions = list()
  digits = [1,2,3,4,5,6,7,8,9]
  perms = list(permutations(digits))
  for perm in perms:
    matrix = [[0,0,0], [0,0,0], [0,0,0]]
    index = 0
    for i in range(3):
      for j in range(3):
        matrix[i][j] = perm[index]
        index += 1
    if check(matrix):
      print(matrix)
      solutions.append(matrix)
  return solutions

# print(check([[2,7,6],[9,5,1],[4,3,8]]))

print(generateSolutions())
