# Learning-Coding
Introduction to computer programming using Python

# Basic Types:
- int
- float
- bool
- str

# Integer division:
| Description | Code |
| --- | --- |
| Div A per B | ```A // B``` |
| Mod A per B | ```A % B``` |
| Div and Mod of A per B | ```div, mod = divmod(A, B)```

# Length of string or collection:
```
len(string/collection)
```

# If statement
```
if [logical_expression]:
  # statements
elif [logical_expression]:
  # statements
elif [logical_expression]:
  # statements
else:
  # statements

# Inline
[result if true] if [logical_expression] else [result if false]

```

# Null value
- None
```
# Check null: 
if variable/expression is None:
  # statements
```

# For looping
```
  for i in range(0, len(collection)):
    # statements
  for item in collection
    # statements
```

# While looping
```
while [logical_expression]:
  # statements
```

# Break and Continue Looping
- break
- continue

# Functions
```
def function_name (params list):
  # Function Body
  return [return value]

def function_name (param1: type, param2: type) -> return_type:
  # Function Body
  return [return value]

```

# Exceptions
```
try:
  # statements
except [ExceptionType]:
  # statements
except [ExceptionType]:
  # statements
else: # only excecuted if no exceptions
  # statements
finally: # always executed
  # statements

# Raise exception
raise Exception(exception_details)
```

# List
| Description  | Code |
|---|---|
| Constructor |```[] or list()``` |
| Add a list | ```listA + listB or listA.extend(listB) ```|
| Add element | ```append(e)``` |
| Remove first ocurrence | ```remove(e)``` |
| Remove last | ```pop()``` |
| Remove by range | ```del list[start[:end]]``` |
| Remove at and return | ```pop(i)``` |
| Sort | ```list.sort()``` |
| Sort with lambda | ```list.sort(key = lambda e: e.field)``` |
| Sort to new | ```sorted()``` |
| Insert at | ```insert(i, e)``` |
| Find index | ```index(e, [start, end])``` |
| Count elements | ```count(e)``` |
| Reverse | ```reverse()``` |

# Set
| Description  | Code |
|---|---|---|
| Constructor | ```set() or set(list)``` |
| Union |``` set.union(a,b)``` |
| Difference | ```set.difference(a,b)``` |
| Intersection | ```set.intersection(a,b)``` |
| Check if exists | ```element in set``` |

# Dictionary
| Description | Code
|---|---|---|
| Constructor | ```dict()``` |
| Keys| ```keys()``` |
| Check if key exists | ```k in dict.keys()``` |
| Values | ```values()``` |
| Access | ```dict[key]``` |
| Access with default| ```dict.get(key, [default])``` |
| Check | ```key_value in dict.keys()``` |
| Delete| ```del dict[key]```
| Remove| ```dict.pop(key)``` |
| Remove with default | ```dict.pop(key, [default]))``` |
| Keys in inserted order | ```list(dictionary)``` |
| Looping | ```for key, value in dictionary:``` |

# Map Function
Applies a function to all elements in a list and returns a new list
```
result = list(map(lambda e: function(e), input_list))
```

# Filter Function
Creates a list of elements for which a function returns true
```
result = list(filter(lambda e: expression(e), input_list))
```

# Zip Function
The zip(lists) function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
```
names = ['Jose', 'Leila', 'Artur']
ages = [49, 44, 19]
for name, age in zip(names, ages):
  print(name, 'is', age, 'years old')
```

# Class
```
class ClassName:
  # Constructor
  def __init__ (self, param1, param2):
    self.Attribute1 = param1
    self.Attribute2 = param2

  def Function(self, param1, param2):
    # statements
    return value
  
obj = ClassName(param1, param2)
```