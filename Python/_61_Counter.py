# A Counter is a dict subclass for counting hashable objects.
from collections import Counter

c = Counter('abracadabra')
print(type(c))
print(c)
print("'a' in c.keys() = ", 'a' in c.keys())
print("c['a'] =", c['a'])
most_common = c.most_common(3)
print(type(most_common))
print(most_common)
print(most_common[0])
print(most_common[1])
print(most_common[2])
print(most_common[0][0], most_common[0][1])
