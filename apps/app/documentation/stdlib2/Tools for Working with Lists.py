# https://docs.python.org/3/tutorial/stdlib2.html#tools-for-working-with-lists
from array import array

a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

"""The collections module provides a deque() object that 
is like a list with faster appends and pops from the left side 
but slower lookups in the middle. These objects are well suited 
for implementing queues and breadth first tree searches:"""

from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

 