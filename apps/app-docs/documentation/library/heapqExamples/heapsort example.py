# https://en.wikipedia.org/wiki/Heapsort
"""
Heap queue algorithm (a.k.a. priority queue).
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k,
counting elements from 0. For the sake of comparison, non-existing elements
are considered to be infinite. The interesting property of a heap is that
a[0] is always its smallest element.
"""
from heapq import heappush
from heapq import heappop


def heapsort(iterable):
    h = []
    for value in iterable:
        # Push item onto heap, maintaining the heap invariant.
        heappush(h, value)
        # Pop the smallest item off the heap, maintaining the heap invariant.
    return [heappop(h) for i in range(len(h))]


res = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
