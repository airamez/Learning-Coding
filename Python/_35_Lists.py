my_list = list()

my_list.append(10)
my_list.append(3.14)
my_list.append(100.45)
my_list.append("Python")
my_list.append("Java")
my_list.append(23)
my_list.append("C#")
my_list.append(45.49)
my_list.append("Python")
my_list.append(99)

print("Type =", type(my_list))
print(my_list)

for i in range(0, len(my_list)):
    print(i, my_list[i], type(my_list[i]))

print("Only integer")
for i in range(0, len(my_list)):
    if isinstance(my_list[i], int):
        print(i, my_list[i], type(my_list[i]))

print("Only float")
for i in range(0, len(my_list)):
    if isinstance(my_list[i], float):
        print(i, my_list[i], type(my_list[i]))

print("Only string")
for i in range(0, len(my_list)):
    if isinstance(my_list[i], str):
        print(i, my_list[i], type(my_list[i]))

for item in my_list:
  print(item)