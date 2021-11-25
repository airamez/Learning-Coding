'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
The command range can be used to generate a sequence:
  range(i,j) => i = inclusive; j = exclusive
Observations: 
  1 - Python for is different from C like languages: C, C++, C#, Java, JavaScript, etc
  2 - It is more like a foreach
'''

print('All interval')
for i in range(0, 10):
    print(f'{i}, ', end='')
    # All commands aligned inside the for it part of the for loopingprint("This is after the for")

print('\nOnly ODD')
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

print('Range in reverse')
for i in range(10, 1, -1):
    print(f"{i}, ", end='')

print()

# Nested loops
# Prints the multiplication table
start = 0
end = 10
for i in range(start, end + 1):
    print(f'Mutiplication table of {i}')
    for j in range(start, end + 1):
        print("{0} x {1} = {2}".format(i, j, i * j))
'''
Practices:
1 - Read two integer numbers representing an interval and print all numbers in the interval
2 - Print the first 50 terms of Fibonacci series
'''

'''
The Fibonacci series is calculated using two initial terms: 0 and 1 and each new term is
the addition of the two previous ones.
'''
term_left = 0
term_right = 1
print(term_left, term_right, end=' ') # Printing the first two terms
for i in range(0, 50):                # Looping 50 times
  new_term = term_left + term_right   # Calculate the new term
  print(new_term, end=' ')            # Printing the new term
  term_left = term_right              # Updating the term_left with the term_right value
  term_right = new_term               # Updating the term_right with the new_term value