months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]

print('#1 Printing a list')
print('Type =', type(months))
print(months)
for month in months:
    print(month)

# Declaring List
languages = list()

languages.append("Python")
languages.append("Java")
languages.append("C#")
languages.append("Python")
languages.append("JavaScript")
languages.append("Python")
languages.append("SQL")
languages.append("C")
languages.append("C++")
languages.append("COBOL")

print("\n#2 Printing the List")
print(languages)

print("\n#3 List length")
print("List length =", len(languages))
print("List length =", languages.__len__())

print("\n#4 Accessing elements")
for i in range(0, len(languages)):
    print(i, "=", languages[i])

print("\n#5 Printing the List in reversed order")
for i in range(len(languages) - 1, -1, -1):
    print(i, "=", languages[i])

first_index = 0
print("\n#6 First element index = ", first_index)
print("First:", languages[first_index])

last_index = len(languages) - 1
print("\n#7 Last element index = ", last_index)
print("Last:", languages[last_index])
print("Last:", languages[-1])

print("\n#8 Count")
pythonCount = languages.count("Python")
print("Python Count =", pythonCount)

print("\n#9 Changing elements")
print(languages)
languages[9] = "PHP"
print(languages)

print("\n#10 Removing an element at a specific index")
removed = languages.pop(3)
print("Removed element at index 3 =", removed)
print(languages)

print("\n#11 Removing the last_index element")
removed = languages.pop()
print("Removed element =", removed)
print(languages)

print("\n#12 Removing the first_index occurrence of a element based on the value")
languages.remove("Python")
print("First Python removed")
print(languages)

print("\n#13 Remove raise an Error if the element doesn't not exist")
try:
    languages.remove("Ruby")
except ValueError as e:
    print(f'Element not found: {e}')

print("\n#14 Inserting an element at a specific index")
languages.insert(0, "Delphi")
languages.insert(4, "Lua")
languages.insert(len(languages), "Python")  # Insert at last_index index == Append
print(languages)

print("\n#15 Finding the first_index index of an element")
first_python = languages.index("Python")
print("First Python =", first_python)

print("\n#16 Index raise an Error if doesn't find")
try:
    first_cobol = languages.index("Cobol")
except ValueError as e:
    print(e)

print("\n#17 Checking if exists")
if "Python" in languages:
    print("Python found")
print("PythonXXX" in languages)

print("\n#18 Checking if NOT exists")
if "Cobol" not in languages:
    print("Cobol NOT found")

print("\n#19 Reversing the entire list")
print(languages)
languages.reverse()
print(languages)

print("\n#20 Sorting the list")
languages.sort()
print(languages)

print("\n#21 Slice")
'''
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
'''
languages_2_to_4_end = languages[2:5]
print("[2:5]", languages_2_to_4_end)
languages_5_to_end = languages[5:]
print("[5:]", languages_5_to_end)
languages_0_to_5 = languages[:6]
print("[:6]", languages_0_to_5)
languages_copy = languages[:]
print("Copy =", languages_copy)
print("List =", languages)

print("\n#22 Removing elements using del + slices")
print("Copy =", languages_copy)
del languages_copy[3:6]
print("Copy =", languages_copy)

print("\n#23 Cleaning the list")
languages.clear()
print(languages)

print("\n#24 Initializing a list with range")
months = list(range(1, 13))
print(months)

print("\n#25 Initializing a list with range")
even_from_1_10 = list(range(0, 11, 2))
print(even_from_1_10)

odd_from_1_10 = list(range(1, 11, 2))
print(odd_from_1_10)

print('\n26# Adding a list to a list')
full_list = list()
print(full_list)
full_list.extend(even_from_1_10)
print(full_list)
full_list.extend(odd_from_1_10)
print(full_list)
full_list.sort()  # Sorting
print(full_list)

# DANGER: Be careful when assiging values to a list because some functions doesn't return values and the list values will be lost
full_list = full_list.sort()
print(full_list)
