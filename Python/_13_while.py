'''
A while loop executes a set of statements as long as the condition is true.
'''

count = 1
while count <= 10:
    print(count)
    count += 1

number = int(input("Type a number between 10 and 100: "))
while number < 10 or number > 100:
    number = int(input("Type a number between 10 and 100: "))
print(number)
