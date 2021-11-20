first_name = "Jose"
last_name = "Santos"

# Concatanation
full_name = first_name + " " + last_name
print('Fullname: ', full_name)

# Interpolation (Awsome feature)
full_name = f"{first_name} {last_name}"
print(full_name)

n1 = 10
n2 = 5
n3 = 3
avg = (n1 + n2 + n3) / 3
print(f"The Average of {n1}, {n2} and {n3} is {avg}")

# Interpolation with formating
name = 'Jose Santos'
age = 49
salary = 175000.49345
formated_string = f'name: {name}; age: {age}, salary: {salary: ,.2f}'
print(formated_string)

# Length
print('len(full_name):', len(full_name))

# Acessing String by indexes. A string is a collection of characters
# Zero based: zero is the first index
print("012345678910")
print(full_name)
print('full_name[0]:', full_name[0])
print('full_name[5]', full_name[5])

# Negative indexes come from the end
print('full_name[-1]:', full_name[-1])
print('full_name[-2]:', full_name[-2])
print('full_name[-3]', full_name[-3])

# Slicing (VERY POWERFUL)
# string[start, end]: start inclusive; end exclusive
# |0|1|2|3|4|5|6|7|8|9|10
# |J|o|s|e| |S|a|n|t|o|s
#  ...-9-8-7-6-5-4-3-2-1
print('full_name[0:5]:', full_name[0:5])
print('full_name[:5]:', full_name[:5])
print('full_name[5:]:', full_name[5:])
print('full_name[2:7]:', full_name[2:7])
print('full_name[1:-1]:', full_name[1:-1])

# The slicing doesn't not raise exception with invalid indexes
print('full_name[0:100]:', full_name[0:100])
# Direct access does raise exception with invalid indezes
#print(full_name[11])

# String are immutable.
# Try to assign a value to a index causes an error:
# 'str' object does not support item assignment
# full_name[0] = 'j'
# full_name[5] = 's'
# If you need to change a string, you need to generate a new one
new_full_name = f"j{full_name[1:5]}s{full_name[6:]}"
print(new_full_name)

### Excercises
# 1. Create an expression to generated an inverted version of a string
#    e.g: abcde -> edcba
# 2. Create an expression to generate a new string from "a_b_c_d_e" without the '_' characters
#    response: abcde
