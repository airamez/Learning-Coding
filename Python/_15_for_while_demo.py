"""
Game to find a random number from 0 to 9
"""

# Importing a python module to use a function to return a random number
import random

# Generating a random number between 0 and 8 (inclusive)
rnd = random.randint(0, 9)

count = 0

while True:  # Infinite looping. It will require a break to interrupt
    guess = int(input("Type a number between (inclusive) 0 and 9 = "))
    if guess < 0 or guess > 9:  # Ignoring if the guess is outside of the interval [0..9]
        print('INVALID VALUE! READ THE INPUT MESSAGE')
        continue
    count += 1
    if guess == rnd:
        break
print("Congratulations! You found the number with {0} attempts".format(count))
