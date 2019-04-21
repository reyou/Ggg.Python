from heapq import heappush
from heapq import heappop
"""
This is similar to sorted(iterable), but unlike sorted(), 
this implementation is not stable. Heap elements can be tuples. 
This is useful for assigning comparison values (such as task priorities) 
alongside the main record being tracked:
"""
h = []
res = h
heappush(h, (5, 'write code'))
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
heappush(h, (7, 'release product'))
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
heappush(h, (1, 'write spec'))
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
heappush(h, (3, 'create tests'))
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = heappop(h)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
