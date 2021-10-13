# Declaring a list
my_list = []
print('Type:', type(my_list))

# Reading data to a list
while True:
    my_string = input("Type something [EMPTY to end] = ")
    if my_string:
        my_list.append(my_string)
    else:
        break

print("List =", my_list)
print("List length =", len(my_list))

print("First =", my_list[0])
print("Last =", my_list[len(my_list) - 1])
