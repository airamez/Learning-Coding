from collections import deque
my_deque = deque()
my_deque.append("Brazil") # Add to the right side (End/Tail)
my_deque.appendleft("Canada") # Add to the left (Start/Head)
my_deque.insert(1, 'USA') # insert at specific position
print(my_deque)
first = my_deque.popleft() # Remove from the left (Start/Head)
print(first)
print(my_deque)
last = my_deque.pop() # Remove from the right (End/Tail)
print(last)
print(my_deque)