phrase = "I Love Computer Programming"

print("#1 Accessing a character at a specific index")
first_character = phrase[0]
last_character = phrase[len(phrase) - 1]
print(f"First = {first_character}; Last = {last_character}")
# An exception is raised if an invalid index is accessed
try:
    print(phrase[100])
except IndexError as e:
    print(e)

print("\n#2 String concatenation")
first_name = "José"
last_name = "Santos"
full_name = first_name + " " + last_name
print("Full Name =", full_name)
# The concatenation requires all types to be converted to string
integer = 10
try:
    new_string = phrase + integer
except TypeError as e:
    print(e)
new_string = phrase + str(integer)
print(new_string)

print("\n#3 Looping through all characters of a string")
for c in first_name:
    print(c)
for i in range(0, len(first_name)):
    print(f"first_name[{i}] = {first_name[i]}")

print("\n#4 Is Alphabetic")
print("abcd".isalpha())
print("abcd.".isalpha())
print("abcd123".isalpha())
print("".isalpha())

print("\n#5 Is Numeric")
print("123456789".isnumeric())
print("12334abc".isnumeric())
print(" 123 ".isnumeric())
print(" ".isnumeric())
print("".isnumeric())

print("\n#6 Is AlphaNumeric")
print("123".isalnum())
print("12334abc".isalnum())
print(" 123 ".isalnum())
print("$123 ".isalnum())

print("\n#7 Is Space")
print(" ".isspace())
print("       ".isspace())
print("  coding    ".isspace())
print("".isspace())