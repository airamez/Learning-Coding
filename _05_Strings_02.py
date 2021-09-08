first_name = "Jose"
last_name = "Santos"

# Concatanation
full_name = first_name + " " + last_name
print(full_name)

# Interpolation
full_name = f"{first_name} {last_name}"
print(full_name)

n1 = 10
n2 = 5
n3 = 3
avg = (n1 + n2 + n3) / 3
print(f"{n1} + {n2} + {n3} = {avg}")

# Length
print(len(full_name))

# Acessing String by indexes. A string is a collection of characters
print(full_name[0]) # Zero based: zero is the first index
print(full_name[5])

# Negative indexes come from the end
print(full_name[-1])
print(full_name[-2])
print(full_name[-3])

# Slicing
# |0|1|2|3|4|5|6|7|8|9|10
# |J|o|s|e| |S|a|n|t|o|s
#  ...-9-8-7-6-5-4-3-2-1
print(full_name[0:5])
print(full_name[:5])
print(full_name[5:])
print(full_name[2:7])
print(full_name[1:-1])
print(full_name[5:])

print(full_name[0:100])
# Error: print(full_name[5:])
print(full_name[11])