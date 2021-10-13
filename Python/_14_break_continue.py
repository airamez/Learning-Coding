'''
The break and continue statement afftect a loop command: for and while
break     : exit the loop. (Ends the loop)
continue  : skip the current interaction and jump to the next one (continues the loop)

'''
for i in range(10):
    print(f'{i}, ', end='')
    if i >= 5:
        break

print()

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Simulating a 'do while'
while True:
    number = int(input("Type a number between 5 and 10: "))
    if number > 5 and number < 10:
        break
print(number)

# Using else for repetition commands
for i in range(10):
    print(f'{i}, ', end='')
else:
    print('for is over')

for i in range(10):
    print(f'{i}, ', end='')
    if i >= 5:
        break
else:  # else not executed when break is executed
    print('for is over')
