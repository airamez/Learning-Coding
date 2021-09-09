for i in range(10):
  print(i)
  if i >= 50:
    break

for i in range(10):
  print(i)
else:
  print('for is over')

for i in range(10):
  print(i)
  if i >= 5:
    break
else: # else not executed when break is executed
  print('for is over')

while True:
  number = int(input("Type a number between 5 and 10: "))
  if number > 5 and number < 10:
    break
else:
  print(number)

for i in range(10):
  if i % 2 == 0:
    continue
  print(i)
