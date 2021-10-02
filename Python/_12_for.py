'''
A for loop is used for iterating over a sequence
The command range can be used to generate a sequence
range(i,j) => i = inclusive; j = exclusive
OBS: Python for is different from C like languages: C, C++, C#, Java, JavaScript, etc
'''

print('All interval')
for i in range(0, 10):
  print(f'{i}, ', end='')
   # All commands aligned inside the for it part of the for loopingprint("This is after the for")

print('Only ODD')
for i in range(0, 10):
  if i % 2 == 0:
    print(f'{i}, ', end='')

print('Step 5')
for i in range(0, 50, 5):
  print(f'{i}, ', end='')

print('Characters from string')
text = "I LOVE PYTHON!"
for c in text:
  print(c, end='')

print('Characters by index')
for i in range(len(text)):
  print(f"text[{i}]={text[i]}")

# Nested loops
# Prints the multiplication table
start = 0
end = 10
for i in range(start, end + 1):
    for j in range(start, end + 1):
        print("{0} x {1} = {2}".format(i, j, i * j))


'''
Practices:
1 - Read two integer numbers representing an interval and print all numbers in the interval
2 - 
'''
