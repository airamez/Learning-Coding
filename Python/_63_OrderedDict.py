'''
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. 
They have become less important now that the built-in dict class gained the ability to remember insertion order
Algorithmically, OrderedDict can handle frequent reordering operations better than dict. This makes it suitable for tracking recent accesses (for example in an LRU cache). LRU = Least Recently Used 
'''

from collections import OrderedDict

cache = OrderedDict()
cache[6] = "F"
cache[2] = "B"
cache[4] = "D"
cache[1] = "A"
cache[5] = "E"
cache[3] = "C"
cache[7] = "H"
print(cache)

for key,value in cache.items():
  print(f'{key}={value}')

print(cache[1])
least = cache.popitem(False)
print(least)
print(cache)
