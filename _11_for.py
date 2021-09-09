# range(i,j) => i = inclusive; j = exclusive

for i in range(0, 10):
  print(i)

print()

for i in range(0, 50, 5):
  print(i)

text = "I love python!"
for c in text:
  print(c, end='')
  
print()
for i in range(len(text)):
  print(f"text[{i}]={text[i]}")
