# Getting char code (ord)
print('ord("A") =', ord("A"))
# Getting a char based on the code (order)
print("chr(65) =", chr(65))

print("chr(50896) =", chr(50896))

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz0123456789"
print(s)
for i in range(0, len(s)):
    print(f"{s[i]} = {ord(s[i])}")

for i in range(371, 400):
    print(f"{i} = {chr(i)}")

