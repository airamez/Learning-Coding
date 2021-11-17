# Declaring a dictionary
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print('Type = ', months)
print(type(months))

print('#1 printing a dictionary')
print("Months =", months)

print('\n#2 Acessing the key the keys')
for key in months.keys():
    print(f'{key}, ')

print('\n#3. Acessing the Values')
for value in months.values():
  print(value)

print('\n#4 Accessing element using the key')
print("months[3] =", months[3])
print("months[5] =", months[5])
print("months[11] =", months[11])

print("\n#5 Accessing a key that doesn't exist raise an exception")
try:
    print(months[99])  # Raise an exception
except KeyError as e:
    print(type(e), e)

print("\n#6 Testing if a key exist before access")
if 3 in months:
    print(months[3])
else:
    print('3 Not found')

if 99 in months.keys():
    print(months[99])
else:
    print('99 Not found')

print('\n#7 Accessing a value from a key using the get method')
print("months.get(3) =", months.get(3))
# Accessing a key that doesn't exist
print("months.get(99) =", months.get(99))  # Doesn't raise exception
# Accessing a value from a key using the get method and using a default value
print('months.get(99, "N/A") =', months.get(99, "N/A"))

print('\n#8 Deleting an Key/Value')
print("Months =", months)
del months[5]
print("Months =", months)
try:
    del months[5]  # Raise an exception
except KeyError as e:
    print(type(e), e)

print('\n#9 Replacing a Value')
months[5] = "Maio"
print("Months =", months)
months[5] = "May"
print("Months =", months)

print('\n#10 Removing elements')
may = months.pop(5)
print(may)
print("Months =", months)
try:
    may = months.pop(5)  # Raise an exception
except KeyError as e:
    print(type(e), e)

print('\n#11 Removing an element using a Default value')
may = months.pop(5, "N/A")
print(may)
may = months.pop(5, None)
print(may)

print('\n#12 Initializing a Dictionary')
countries = dict()
# Adding elements
countries["BRA"] = "Brazil"
countries["CAN"] = "Canada"
countries["USA"] = "United States of America"
countries["MEX"] = "Mexico"

print('\n#13 Testing if a a Key exists in the Dictionary')
print("Countries =", countries)
print("BRA = ", countries["BRA"])
if "CAN" in countries.keys():
    print(countries["CAN"])
if "BR" not in countries:
    print("BR not found")

print('\n#14 Cleaning a dict')
countries.clear()
print("Countries =", countries)

print('\n#15 Looping a dictionary acessing key, value and items()')
for key, value in months.items():
  print(key, value)
