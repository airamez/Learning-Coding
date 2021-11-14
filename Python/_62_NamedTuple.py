'''
- Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
- They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
- Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules
'''
from collections import namedtuple

Customer = namedtuple('Customer', 'ID Name Email')
c1 = Customer(1, 'José', 'jose@noemail.com')
c2 = Customer(2, 'Leila', 'leila@noemail.com')
c3 = Customer(3, 'Artur', 'artur@noemail.com')
print(c1)
print(f'ID = {c1.ID}; Name = {c1.Name}; Email = {c1.Email}')